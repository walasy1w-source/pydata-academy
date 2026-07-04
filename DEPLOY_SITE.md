# Como publicar o site (de graça) — passo a passo

Este guia é só sobre colocar o **site do curso** (`index.html` + notebooks) no ar, sem pagar nada.
Ele não precisa do backend Flask (`app.py`) para funcionar — isso é opcional e fica no `README.md`.

Existem dois caminhos. Escolha **UM** dos dois (não precisa fazer os dois):

- **Opção A — GitHub Pages** (recomendado: mais simples, sempre gratuito, sem limite de tempo)
- **Opção B — Render (site estático)** (também gratuito, útil se você já for usar o Render para o backend)

---

## Antes de tudo: criar o repositório no GitHub

1. Crie uma conta grátis em [github.com](https://github.com) (se ainda não tiver).
2. Clique em **New repository** (botão verde). Dê um nome, por exemplo `pydata-academy`.
3. Marque como **Public** (necessário para o plano gratuito do GitHub Pages).
4. Suba todos os arquivos desta pasta para esse repositório (pelo site do GitHub mesmo, arrastando os
   arquivos em **Add file → Upload files**, ou usando `git push` se preferir linha de comando).
5. Anote seu nome de usuário do GitHub — você vai precisar dele no passo final.

---

## Opção A — GitHub Pages (recomendado)

1. Dentro do repositório que você acabou de criar, crie as pastas `.github/workflows/` e coloque lá
   dentro o arquivo `deploy-pages.yml` que já vem pronto nesta entrega (está em `.github/workflows/deploy-pages.yml`).
2. No repositório, vá em **Settings → Pages**.
3. Em **"Build and deployment" → Source**, escolha **"GitHub Actions"**.
4. Pronto. A cada vez que você atualizar o repositório (`git push` ou upload de um arquivo novo), o
   site é publicado sozinho — acompanhe o progresso na aba **Actions**.
5. Depois do primeiro deploy (leva 1-2 minutos), seu site estará em:
   `https://SEU-USUARIO.github.io/pydata-academy/`

---

## Opção B — Render (site estático)

1. Crie uma conta grátis em [render.com](https://render.com) e conecte sua conta do GitHub.
2. Clique em **New +** → **Static Site** (ou **Blueprint**, se quiser que o Render leia o
   `render.yaml` que já vem pronto nesta entrega e configure sozinho).
3. Se configurar manualmente:
   - **Build Command:** deixe em branco ou `echo "ok"`
   - **Publish directory:** `.` (a raiz do repositório)
4. Clique em **Create Static Site**. Em alguns minutos, o Render te dá uma URL do tipo
   `https://pydata-academy-site.onrender.com` — e ela já fica no ar para sempre, de graça.

---

## Depois de publicar: dois ajustes finais no `index.html`

Esses dois itens **não são obrigatórios para o site funcionar**, mas sem eles alguns botões ainda
apontam para exemplos fictícios:

1. **Botões de Colab/Binder/GitHub** (aparecem 38 vezes no arquivo): procure por `SEU-USUARIO` e troque
   pelo seu nome de usuário real do GitHub (o mesmo que você usou para criar o repositório acima).
2. **Botão "Comprar agora"**: procure por `CHECKOUT_URL` (perto do fim do arquivo) e troque o link de
   exemplo da Hotmart pelo link real do seu produto, assim que ele estiver cadastrado lá.

Pode me pedir para fazer essas duas trocas — é só me falar seu usuário do GitHub e o link de checkout
que eu já deixo tudo certo no arquivo.

---

## E o backend (app.py)?

Ele é **opcional** e serve só para um recurso extra de correção automática de 3 exercícios de exemplo
do Sprint 1. O site funciona 100% sem ele (a correção principal do curso já roda no navegador, via
Pyodide/JupyterLite). Só suba o backend (ver `README.md`) se e quando quiser esse recurso extra.
