"""
PyData Academy — Backend de Correção Automática (Sprint 1)
============================================================

Backend simples em Flask para:
  - Receber o código de um exercício enviado pelo aluno            (POST /run)
  - Executar esse código em um subprocesso isolado, com timeout e limites
    básicos de CPU/memória
  - Rodar os testes automatizados (asserts) daquele exercício
  - Devolver {"status": "ok"} ou {"status": "error", "message": "..."}
  - Registrar o resultado em um banco SQLite simples
  - Expor estatísticas de progresso do aluno                        (GET /progresso)

⚠️  AVISO DE SEGURANÇA — LEIA ANTES DE COLOCAR EM PRODUÇÃO
------------------------------------------------------------
Este backend executa código Python arbitrário enviado por quem chamar a API.
As proteções aqui (subprocesso separado, timeout, rlimits de CPU/memória/
processos, ambiente e PATH mínimos, modo `-I` isolado) são um nível BÁSICO
de proteção — adequadas para um MVP didático, mas NÃO equivalem a uma
sandbox completa. Elas não bloqueiam acesso à rede de dentro do subprocesso,
por exemplo. Para uso em produção com tráfego público, prefira uma sandbox
de verdade (Docker + gVisor/Firecracker, nsjail, ou serviços prontos como
Judge0 / Piston) rodando em um worker isolado do processo web principal.

Deploy: pronto para o Render (free tier). Veja README.md para o passo a passo.
"""

import os
import sqlite3
import subprocess
import sys
import tempfile
import textwrap
from datetime import datetime, timezone

from flask import Flask, jsonify, request
from flask_cors import CORS

try:
    import resource  # disponível apenas em sistemas Unix (Linux/Mac) — é o que o Render usa
except ImportError:
    resource = None

app = Flask(__name__)
CORS(app, origins=["https://walasy1w-source.github.io"])

# ------------------------------------------------------------------
# Configurações
# ------------------------------------------------------------------
TIMEOUT_SEGUNDOS = 5          # tempo máximo de execução do código do aluno
MEMORIA_MAXIMA_MB = 128       # limite de memória do subprocesso
TAMANHO_MAXIMO_CODIGO = 20_000  # caracteres
PONTOS_POR_EXERCICIO = 10
DB_PATH = os.environ.get("DB_PATH", "progresso.db")

# ------------------------------------------------------------------
# Banco de dados (SQLite) — guarda cada submissão para calcular o progresso
# ⚠️ O disco do plano free do Render é efêmero: o arquivo .db pode ser
#    resetado a cada novo deploy/reinício. Para persistência real entre
#    deploys, troque por um Postgres gerenciado (o Render oferece um free tier).
# ------------------------------------------------------------------
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS submissoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_id TEXT NOT NULL,
                exercicio_id TEXT NOT NULL,
                status TEXT NOT NULL,
                mensagem TEXT,
                criado_em TEXT NOT NULL
            )
            """
        )
        conn.commit()


init_db()

# ------------------------------------------------------------------
# Banco de exercícios do Sprint 1 (3 exemplos, um de cada bloco do curso:
# operadores, strings e funções). Cada exercício tem um enunciado e uma
# bateria de testes (asserts) que é concatenada ao código do aluno antes
# de rodar. Se todos os asserts passarem, o script imprime o marcador
# "__TESTES_OK__", que o backend procura na saída para decidir o status.
# ------------------------------------------------------------------
EXERCICIOS = {
    "cap3_eh_par": {
        "titulo": "Capítulo 3 — Verificar se um número é par",
        "enunciado": "Crie uma função eh_par(n) que retorne True se n for par e False caso contrário.",
        "codigo_base": "def eh_par(n):\n    # Escreva sua resposta aqui\n    pass\n",
        "testes": textwrap.dedent(
            """
            assert eh_par(4) == True, "eh_par(4) deveria retornar True"
            assert eh_par(7) == False, "eh_par(7) deveria retornar False"
            assert eh_par(0) == True, "eh_par(0) deveria retornar True"
            assert eh_par(-3) == False, "eh_par(-3) deveria retornar False"
            print("__TESTES_OK__")
            """
        ),
    },
    "cap7_inverter_string": {
        "titulo": "Capítulo 7 — Inverter uma string",
        "enunciado": "Crie uma função inverter_string(s) que retorne a string s invertida.",
        "codigo_base": "def inverter_string(s):\n    # Escreva sua resposta aqui\n    pass\n",
        "testes": textwrap.dedent(
            """
            assert inverter_string("python") == "nohtyp", "inverter_string('python') deveria ser 'nohtyp'"
            assert inverter_string("arara") == "arara", "inverter_string('arara') deveria ser um palíndromo"
            assert inverter_string("") == "", "inverter_string('') deveria retornar string vazia"
            print("__TESTES_OK__")
            """
        ),
    },
    "cap9_resumo_vendas": {
        "titulo": "Capítulo 9 — Resumo de vendas",
        "enunciado": (
            "Crie uma função resumo_vendas(vendas) que receba uma lista de números e "
            "retorne um dicionário com as chaves total, media, maximo e minimo."
        ),
        "codigo_base": "def resumo_vendas(vendas):\n    # Escreva sua resposta aqui\n    pass\n",
        "testes": textwrap.dedent(
            """
            r = resumo_vendas([120, 340, 95, 210, 180])
            assert r["total"] == 945, f"total incorreto: {r.get('total')}"
            assert abs(r["media"] - 189.0) < 0.01, f"media incorreta: {r.get('media')}"
            assert r["maximo"] == 340, f"maximo incorreto: {r.get('maximo')}"
            assert r["minimo"] == 95, f"minimo incorreto: {r.get('minimo')}"
            print("__TESTES_OK__")
            """
        ),
    },
}

# ------------------------------------------------------------------
# Execução segura do código do aluno
# ------------------------------------------------------------------
def _limitar_recursos():
    """Roda dentro do processo filho (preexec_fn), antes do exec.
    Define limites de CPU, memória, nº de processos e escrita em disco."""
    try:
        resource.setrlimit(resource.RLIMIT_CPU, (TIMEOUT_SEGUNDOS, TIMEOUT_SEGUNDOS + 1))
        mem_bytes = MEMORIA_MAXIMA_MB * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (mem_bytes, mem_bytes))
        resource.setrlimit(resource.RLIMIT_NPROC, (10, 10))
        resource.setrlimit(resource.RLIMIT_FSIZE, (1024 * 1024, 1024 * 1024))  # máx. 1MB gravado em disco
    except Exception:
        # setrlimit pode falhar dependendo de permissões do ambiente — nesse
        # caso seguimos apenas com o timeout do subprocess como proteção.
        pass


def executar_codigo_aluno(codigo_aluno: str, exercicio_id: str):
    """Roda `codigo_aluno` + os testes do exercício em um subprocesso isolado.
    Retorna a tupla (ok: bool, mensagem: str)."""

    exercicio = EXERCICIOS.get(exercicio_id)
    if exercicio is None:
        return False, f"Exercício '{exercicio_id}' não encontrado."

    programa_completo = (
        codigo_aluno.strip()
        + "\n\n# --- Testes automáticos (não enviados pelo aluno) ---\n"
        + exercicio["testes"]
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        script_path = os.path.join(tmpdir, "solucao.py")
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(programa_completo)

        try:
            resultado = subprocess.run(
                [sys.executable, "-I", script_path],  # -I: modo isolado (ignora env/site-packages do usuário)
                cwd=tmpdir,
                timeout=TIMEOUT_SEGUNDOS,
                capture_output=True,
                text=True,
                env={"PATH": os.environ.get("PATH", "")},  # ambiente mínimo, sem variáveis do servidor
                preexec_fn=_limitar_recursos if (os.name == "posix" and resource) else None,
            )
        except subprocess.TimeoutExpired:
            return False, f"⏱️ Tempo limite excedido ({TIMEOUT_SEGUNDOS}s). Verifique se há loops infinitos."
        except OSError as e:
            return False, f"Não foi possível executar o código: {e}"

        if resultado.returncode != 0:
            linhas_erro = resultado.stderr.strip().splitlines()
            ultima_linha = linhas_erro[-1] if linhas_erro else "Erro desconhecido ao executar o código."
            return False, ultima_linha

        if "__TESTES_OK__" in resultado.stdout:
            return True, "✅ Todos os testes passaram!"

        return False, "O código rodou, mas não passou nos testes esperados."


# ------------------------------------------------------------------
# Rotas
# ------------------------------------------------------------------
@app.route("/", methods=["GET"])
def index():
    return jsonify(
        {
            "servico": "PyData Academy — Backend de Correção Automática",
            "status": "online",
            "endpoints": {
                "POST /run": "Envia {aluno_id, exercicio_id, codigo} e roda os testes",
                "GET /exercicios": "Lista os exercícios disponíveis",
                "GET /progresso?aluno_id=...": "Estatísticas de progresso do aluno",
            },
        }
    )


@app.route("/exercicios", methods=["GET"])
def listar_exercicios():
    return jsonify(
        {
            eid: {
                "titulo": ex["titulo"],
                "enunciado": ex["enunciado"],
                "codigo_base": ex["codigo_base"],
            }
            for eid, ex in EXERCICIOS.items()
        }
    )


@app.route("/run", methods=["POST"])
def run_codigo():
    dados = request.get_json(silent=True) or {}
    aluno_id = str(dados.get("aluno_id", "")).strip()
    exercicio_id = str(dados.get("exercicio_id", "")).strip()
    codigo = dados.get("codigo", "")

    if not aluno_id:
        return jsonify({"status": "error", "message": "Campo 'aluno_id' é obrigatório."}), 400
    if not exercicio_id:
        return jsonify({"status": "error", "message": "Campo 'exercicio_id' é obrigatório."}), 400
    if not codigo or not isinstance(codigo, str):
        return jsonify({"status": "error", "message": "Campo 'codigo' é obrigatório e deve ser texto."}), 400
    if exercicio_id not in EXERCICIOS:
        return jsonify({"status": "error", "message": f"Exercício '{exercicio_id}' não existe."}), 404
    if len(codigo) > TAMANHO_MAXIMO_CODIGO:
        return jsonify({"status": "error", "message": "Código muito longo (máx. 20.000 caracteres)."}), 400

    ok, mensagem = executar_codigo_aluno(codigo, exercicio_id)
    status = "ok" if ok else "error"

    with get_db() as conn:
        conn.execute(
            "INSERT INTO submissoes (aluno_id, exercicio_id, status, mensagem, criado_em) VALUES (?, ?, ?, ?, ?)",
            (aluno_id, exercicio_id, status, mensagem, datetime.now(timezone.utc).isoformat()),
        )
        conn.commit()

    resposta = {"status": status, "message": mensagem}
    if ok:
        resposta["pontos_ganhos"] = PONTOS_POR_EXERCICIO

    # 200 mesmo quando status="error" de teste: o aluno errou o exercício,
    # o que é uma resposta de negócio válida, não uma falha da API.
    # Erros de validação de entrada (acima) usam 400/404, esses sim erros da API.
    return jsonify(resposta), 200


@app.route("/progresso", methods=["GET"])
def progresso():
    aluno_id = request.args.get("aluno_id", "").strip()
    if not aluno_id:
        return jsonify({"status": "error", "message": "Informe ?aluno_id=... na URL."}), 400

    with get_db() as conn:
        linhas = conn.execute(
            "SELECT * FROM submissoes WHERE aluno_id = ? ORDER BY criado_em ASC",
            (aluno_id,),
        ).fetchall()

    if not linhas:
        return jsonify(
            {
                "aluno_id": aluno_id,
                "exercicios_tentados": 0,
                "exercicios_corretos": 0,
                "total_submissoes": 0,
                "taxa_acerto": 0,
                "pontos_totais": 0,
                "exercicios": {},
            }
        )

    por_exercicio = {}
    for linha in linhas:
        eid = linha["exercicio_id"]
        info = por_exercicio.setdefault(
            eid,
            {
                "titulo": EXERCICIOS.get(eid, {}).get("titulo", eid),
                "tentativas": 0,
                "resolvido": False,
                "ultima_tentativa": None,
            },
        )
        info["tentativas"] += 1
        info["ultima_tentativa"] = linha["criado_em"]
        if linha["status"] == "ok":
            info["resolvido"] = True

    total_tentados = len(por_exercicio)
    total_corretos = sum(1 for v in por_exercicio.values() if v["resolvido"])
    total_submissoes = len(linhas)
    submissoes_corretas = sum(1 for l in linhas if l["status"] == "ok")
    taxa_acerto = round((submissoes_corretas / total_submissoes) * 100, 1) if total_submissoes else 0

    return jsonify(
        {
            "aluno_id": aluno_id,
            "exercicios_tentados": total_tentados,
            "exercicios_corretos": total_corretos,
            "total_submissoes": total_submissoes,
            "taxa_acerto": taxa_acerto,
            "pontos_totais": total_corretos * PONTOS_POR_EXERCICIO,
            "exercicios": por_exercicio,
        }
    )


if __name__ == "__main__":
    # Uso local: python app.py (produção usa gunicorn — ver Procfile)
    porta = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=porta, debug=False)
