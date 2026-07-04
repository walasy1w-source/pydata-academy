# Como usar este prompt com o Claude Code

1. Abre o aplicativo **Terminal** no seu Mac (Cmd+Espaço, digita "Terminal", Enter).
2. No Terminal, digita `cd ` (com um espaço depois) e **arrasta a pasta "outputs"** (a mesma do
   Finder, com o `index.html`, os notebooks, etc.) para dentro da janela do Terminal — o caminho
   completo da pasta aparece sozinho. Aperta Enter.
3. Digita `claude` e aperta Enter (isso abre o Claude Code nessa pasta).
4. Cola o prompt lá de baixo (tudo dentro da caixa cinza) e manda.
5. O Claude Code vai organizar e subir tudo pro GitHub sozinho — só vai te pedir autenticação na
   primeira vez (explico como resolver isso dentro do próprio prompt).

---

## O prompt (copie tudo dentro da caixa abaixo)

```
Você está na pasta local do projeto "PyData Academy" — um site de curso de Python para Ciência de
Dados, com index.html, notebooks Jupyter (sprintN_exercicios.ipynb), um backend Flask (app.py) e
documentos de apoio. Preciso que você suba TODO o conteúdo relevante desta pasta para o repositório
GitHub que já existe em https://github.com/walasy1w-source/pydata-academy (branch main).

Siga exatamente estes passos:

1. Confirme que está rodando dentro da pasta certa: ela deve conter index.html, app.py, README.md,
   render.yaml e vários arquivos sprintN_exercicios.ipynb. Se não encontrar esses arquivos no
   diretório atual, PARE e me avise em vez de continuar.

2. Verifique se já existe um repositório git aqui (pasta .git). Se não existir, rode:
   git init
   git branch -M main

3. Crie (ou atualize, sem duplicar linhas) um arquivo .gitignore na raiz contendo pelo menos:
   docxbuild/
   .DS_Store
   __pycache__/
   *.pyc
   progresso.db
   A pasta docxbuild/ é só uma pasta de build temporária (tem node_modules dentro) e NÃO deve ir
   para o repositório.

4. Confirme que existe o arquivo .github/workflows/deploy-pages.yml (é um arquivo dentro de uma
   pasta escondida, começando com ponto — use `ls -la` e `find . -name deploy-pages.yml` para
   procurar, não confie só no Finder). Se ele não existir, crie-o com exatamente este conteúdo:

   name: Deploy site no GitHub Pages

   on:
     push:
       branches: ["main"]
     workflow_dispatch:

   permissions:
     contents: read
     pages: write
     id-token: write

   concurrency:
     group: "pages"
     cancel-in-progress: true

   jobs:
     deploy:
       environment:
         name: github-pages
         url: ${{ steps.deployment.outputs.page_url }}
       runs-on: ubuntu-latest
       steps:
         - name: Baixar os arquivos do repositório
           uses: actions/checkout@v4
         - name: Preparar o GitHub Pages
           uses: actions/configure-pages@v4
         - name: Empacotar o site inteiro para publicação
           uses: actions/upload-pages-artifact@v3
           with:
             path: "."
         - name: Publicar no GitHub Pages
           id: deployment
           uses: actions/deploy-pages@v4

5. Configure o remoto do GitHub (se ainda não existir):
   git remote add origin https://github.com/walasy1w-source/pydata-academy.git
   Se o remoto já existir, só confirme que a URL está certa com `git remote -v` e corrija com
   `git remote set-url origin ...` se precisar.

6. Adicione, faça commit e envie tudo:
   git add .
   git commit -m "Publica o site da PyData Academy"
   git push -u origin main

7. Se o push pedir usuário e senha: o usuário é walasy1w-source. NÃO use a senha normal da conta —
   o GitHub exige um "Personal Access Token" no lugar da senha (gerado em
   https://github.com/settings/tokens, com permissão "repo"). Se o GitHub CLI (`gh`) estiver
   instalado, rode primeiro `gh auth login` e siga o passo a passo interativo, que resolve a
   autenticação sem precisar gerar token manualmente.

8. Ao final, rode `git log --oneline -5` e `git status`, e me mostre a saída para eu confirmar que
   o push funcionou sem erros.

9. IMPORTANTE: não apague, não renomeie e não sobrescreva o conteúdo de nenhum notebook, do
   index.html ou do docx da proposta — sua tarefa é só organizar (.gitignore, workflow) e enviar
   (git add/commit/push), nunca editar o conteúdo desses arquivos.

Quando terminar, me explique em português simples se deu tudo certo, e qual é o próximo passo
(ativar o GitHub Pages em Settings → Pages → Source → "GitHub Actions" no site do GitHub).
```
