# PyData Academy — Backend de Correção Automática (Sprint 1)

Backend Flask, auto-contido, que recebe o código de um exercício enviado pelo aluno, roda em um
subprocesso isolado com timeout, executa os testes (asserts) daquele exercício e devolve o resultado
em JSON. Inclui progresso do aluno (SQLite) e está pronto para deploy gratuito no Render.

## Arquivos

| Arquivo | Para quê serve |
|---|---|
| `app.py` | Toda a aplicação Flask (rotas, exercícios, execução segura, banco de dados) |
| `requirements.txt` | Dependências (Flask, flask-cors, gunicorn) |
| `Procfile` | Comando de start usado pelo Render (`gunicorn app:app`) |
| `render.yaml` | Deploy "Infrastructure as Code" (opcional, um clique no Render) |
| `runtime.txt` | Versão do Python (fallback caso não use o render.yaml) |
| `.gitignore` | Ignora `progresso.db`, `__pycache__`, etc. |

## Rodando localmente

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py                    # sobe em http://localhost:5000
```

## Contrato da API

### `GET /`
Health check. Retorna status do serviço e lista de endpoints.

### `GET /exercicios`
Lista os exercícios disponíveis (id, título, enunciado, código-base para o aluno começar).

```bash
curl http://localhost:5000/exercicios
```

### `POST /run`
Executa o código do aluno contra os testes de um exercício.

**Body (JSON):**
```json
{
  "aluno_id": "walasy",
  "exercicio_id": "cap3_eh_par",
  "codigo": "def eh_par(n):\n    return n % 2 == 0\n"
}
```

**Resposta (sucesso):**
```json
{"status": "ok", "message": "✅ Todos os testes passaram!", "pontos_ganhos": 10}
```

**Resposta (erro no exercício — resposta errada, exceção, ou timeout):**
```json
{"status": "error", "message": "AssertionError: eh_par(4) deveria retornar True"}
```

```bash
curl -X POST http://localhost:5000/run \
  -H "Content-Type: application/json" \
  -d '{"aluno_id":"walasy","exercicio_id":"cap3_eh_par","codigo":"def eh_par(n):\n    return n % 2 == 0\n"}'
```

### `GET /progresso?aluno_id=walasy`
Estatísticas agregadas de um aluno, calculadas a partir de todas as submissões salvas no SQLite.

```json
{
  "aluno_id": "walasy",
  "exercicios_tentados": 3,
  "exercicios_corretos": 3,
  "total_submissoes": 6,
  "taxa_acerto": 50.0,
  "pontos_totais": 30,
  "exercicios": {
    "cap3_eh_par": {"titulo": "...", "tentativas": 3, "resolvido": true, "ultima_tentativa": "..."}
  }
}
```

## Os 3 exercícios de exemplo (Sprint 1)

| ID | Capítulo | O que o aluno implementa |
|---|---|---|
| `cap3_eh_par` | 3 — Operadores | `eh_par(n)` → `True`/`False` |
| `cap7_inverter_string` | 7 — Strings | `inverter_string(s)` → string invertida |
| `cap9_resumo_vendas` | 9 — Funções | `resumo_vendas(vendas)` → dict com total/média/máximo/mínimo |

Cada exercício tem uma lista de `assert`s em `EXERCICIOS[<id>]["testes"]`, dentro de `app.py`. Para
adicionar um novo exercício, basta acrescentar uma nova chave nesse dicionário — não precisa mexer em
mais nada.

## Como a execução seg️ura funciona

1. O código do aluno é concatenado com os testes do exercício e salvo em um arquivo temporário.
2. Esse arquivo roda em um **subprocesso separado** (`subprocess.run([sys.executable, "-I", ...])`),
   com:
   - **timeout de 5s** (`TIMEOUT_SEGUNDOS` em `app.py`);
   - **limite de memória** (128MB, via `RLIMIT_AS`);
   - **limite de processos filhos** (10, via `RLIMIT_NPROC` — mitiga fork bombs);
   - **limite de escrita em disco** (1MB, via `RLIMIT_FSIZE`);
   - **ambiente mínimo** (`env={"PATH": ...}`, sem variáveis do servidor);
   - **modo isolado do Python** (`-I`, ignora `PYTHONPATH`/pacotes do usuário).
3. Se o processo sair com erro, a última linha do `stderr` (geralmente a mensagem da exceção) vira o
   `message` da resposta.
4. Se os testes passarem, o script imprime um marcador (`__TESTES_OK__`) que o backend procura na
   saída padrão para decidir o status.

> ⚠️ **Isso é uma proteção básica, não uma sandbox completa.** Ela não isola rede nem impede 100% dos
> tipos de abuso. Para expor isso publicamente com tráfego real, troque a execução por uma sandbox de
> verdade (Docker + gVisor/Firecracker, nsjail, ou um serviço pronto como Judge0/Piston) rodando fora
> do processo web principal.

## Deploy no Render (plano free)

1. Suba estes arquivos para um repositório no GitHub/GitLab.
2. No [Render](https://render.com), clique em **New +** → **Web Service** e conecte o repositório.
   - Se o Render detectar o `render.yaml`, ele já preenche tudo — clique em **Apply**.
   - Caso configure manualmente:
     - **Environment:** Python 3
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn app:app --workers 2 --threads 4 --timeout 30`
     - **Plan:** Free
3. Aguarde o build. Ao final, o Render te dá uma URL pública, algo como
   `https://pydata-academy-backend.onrender.com`.
4. Teste: `curl https://pydata-academy-backend.onrender.com/`

**Observações do plano free do Render:**
- O serviço "dorme" após alguns minutos sem tráfego — a primeira requisição depois disso demora mais
  (cold start).
- O disco é **efêmero**: o arquivo `progresso.db` (SQLite) pode ser apagado a cada novo deploy ou
  reinício. Para manter o progresso entre deploys, troque o SQLite por um Postgres gerenciado (o
  próprio Render tem um free tier de Postgres) — a única mudança necessária é a função `get_db()` em
  `app.py`.

## Integrando com o site do curso

No `index.html` do curso, o Playground/exercícios podem chamar este backend com `fetch`:

```js
const resposta = await fetch("https://SEU-BACKEND.onrender.com/run", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ aluno_id: alunoId, exercicio_id: "cap3_eh_par", codigo: codigoDoAluno }),
});
const resultado = await resposta.json();
```

O `flask-cors` já vem habilitado (`CORS(app)`) para permitir chamadas de outra origem. Em produção,
restrinja para o domínio real do site: `CORS(app, origins=["https://seusite.com"])`.
