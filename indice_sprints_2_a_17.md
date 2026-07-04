# PyData Academy — Índice Completo dos Sprints 2 a 17

*Python para Ciência de Dados · v1.0 · 2026*

Este documento é o índice de referência para o restante da grade curricular do curso. Para cada
sprint, você encontra o título, a lista exata de capítulos (mesma contagem do plano original), os
objetivos de aprendizagem, uma descrição do que será estudado e o nome do projeto integrador. O
Sprint 2 já tem notebook completo (`sprint2_exercicios.ipynb`); os Sprints 3 a 17 aparecem no site
como "Em desenvolvimento", usando este índice como especificação para a produção futura do conteúdo.

---

## Sprint 2 — Continuação de Python Básico (7 capítulos)

**Capítulos:**
1. Compreensão de Listas (List Comprehensions)
2. Manipulação Avançada de Strings
3. Tratamento de Exceções (try/except)
4. Módulos e Pacotes
5. Trabalhando com Arquivos
6. Programação Orientada a Objetos I
7. Projeto Prático: Consolidando o Básico

**Objetivos de aprendizagem:**
- Escrever código mais conciso e "pythônico" com list comprehensions.
- Tratar erros de forma controlada com try/except, em vez de deixar o programa quebrar.
- Organizar código em módulos e pacotes reutilizáveis.
- Ler e escrever arquivos de texto, e dar os primeiros passos em Programação Orientada a Objetos (classes e objetos).

**Descrição:** Este sprint fecha o ciclo de "Python puro" antes de o curso mergulhar em dados de
verdade. A ideia central é pegar tudo que foi aprendido no Sprint 1 e reescrever de um jeito mais
elegante e seguro: laços que viram list comprehensions em uma linha, erros que passam a ser tratados
com `try/except` em vez de derrubar o programa, e código que sai de um único arquivo bagunçado para
módulos organizados.

Também é aqui que o aluno é apresentado à Programação Orientada a Objetos (POO) pela primeira vez —
não de forma acadêmica, mas como uma ferramenta prática para organizar dados e comportamentos juntos
(uma classe `Produto`, por exemplo, em vez de um dicionário solto). O sprint termina com um projeto
que consolida tudo: pegar um script simples do Sprint 1 e refatorá-lo usando essas novas ferramentas.

**Projeto integrador:** *Projeto Prático — Consolidando o Básico* (refatoração de um script em
módulos, com tratamento de exceções e ao menos uma classe).

---

## Sprint 3 — Manipulação de Dados (7 capítulos)

**Capítulos:**
1. Introdução ao NumPy
2. Introdução ao Pandas
3. Leitura e Escrita de Arquivos (CSV, Excel, JSON)
4. Limpeza de Dados
5. Filtragem e Agrupamento de Dados
6. Junção de Tabelas (merge, join, concat)
7. Visualização de Dados com Matplotlib

**Objetivos de aprendizagem:**
- Operar com arrays NumPy e entender por que eles são mais rápidos que listas puras.
- Carregar, explorar e limpar dados tabulares com pandas (DataFrames e Series).
- Filtrar, agrupar e combinar tabelas de dados de diferentes fontes.
- Criar visualizações básicas (linhas, barras, dispersão) com Matplotlib.

**Descrição:** Este é o sprint em que o curso realmente "vira" para Ciência de Dados. NumPy entra
como a base numérica de tudo que vem depois (inclusive de bibliotecas de Machine Learning), e pandas
se torna a ferramenta do dia a dia para carregar uma planilha, entender o que tem nela e arrumar o
que estiver "sujo" — valores faltantes, tipos errados, duplicatas.

Na segunda metade do sprint, o foco passa a ser combinar e resumir dados: agrupar vendas por região,
juntar duas tabelas pela chave em comum, e por fim visualizar tudo isso em gráficos simples, mas
informativos, com Matplotlib — a base para comunicar qualquer achado de dados.

**Projeto integrador:** *Análise Exploratória de um Dataset Público* (carregar um CSV real, limpar,
agrupar e visualizar os principais achados).

---

## Sprint 4 — Análise Estatística de Dados (6 capítulos)

**Capítulos:**
1. Estatística Descritiva
2. Distribuições de Probabilidade
3. Testes de Hipóteses
4. Correlação e Covariância
5. Amostragem e Intervalos de Confiança
6. Projeto de Análise Estatística

**Objetivos de aprendizagem:**
- Resumir um conjunto de dados com medidas de tendência central e dispersão.
- Reconhecer as distribuições de probabilidade mais comuns (normal, binomial, etc.).
- Formular e testar hipóteses estatísticas com significância.
- Entender correlação, covariância e a diferença entre correlação e causalidade.

**Descrição:** Antes de treinar qualquer modelo de Machine Learning, é preciso saber "ler" dados como
estatística — e é isso que este sprint ensina. Começamos com o vocabulário básico (média, mediana,
desvio padrão) e evoluímos para distribuições de probabilidade, a base teórica por trás de praticamente
todo teste estatístico.

Na sequência, o aluno aprende testes de hipótese (a pergunta "essa diferença é real ou é acaso?") e
correlação — sempre com o alerta de que correlação não implica causalidade. O sprint fecha com um
projeto que aplica essas ferramentas a um problema de negócio real, incluindo amostragem e intervalos
de confiança para comunicar incerteza de forma honesta.

**Projeto integrador:** *Projeto de Análise Estatística* (teste de hipótese e análise de correlação
sobre um conjunto de dados de negócio).

---

## Sprint 5 — Ferramentas de Desenvolvimento de Software (8 capítulos)

**Capítulos:**
1. Controle de Versão com Git e GitHub
2. Ambientes Virtuais
3. Boas Práticas e PEP 8
4. Testes Automatizados com Pytest
5. Depuração (Debugging)
6. Documentação de Código
7. Linha de Comando (Terminal)
8. Trabalhando com APIs

**Objetivos de aprendizagem:**
- Versionar código com Git e colaborar via GitHub.
- Isolar dependências de projetos com ambientes virtuais.
- Escrever código legível seguindo a PEP 8 e testá-lo com Pytest.
- Depurar erros com confiança e consumir APIs externas.

**Descrição:** Este sprint sai um pouco da "ciência" e entra na "engenharia" de dados — as ferramentas
que separam quem programa como hobby de quem trabalha em equipe. Git e GitHub deixam de ser
opcionais: são a forma como qualquer código profissional é versionado e compartilhado. Ambientes
virtuais evitam o clássico "na minha máquina funciona".

A segunda metade do sprint foca em qualidade: testes automatizados (Pytest) para garantir que o
código continue funcionando depois de mudanças, boas práticas de estilo (PEP 8), e a habilidade,
subestimada mas essencial, de depurar um erro com calma. O sprint termina com APIs — a porta de
entrada para consumir dados de serviços externos (clima, câmbio, redes sociais) direto do Python.

**Projeto integrador:** *Configuração de um Projeto Python Profissional* (repositório Git com
ambiente virtual, testes automatizados e consumo de uma API pública).

---

## Sprint 6 — Projeto Integrado 1 (5 capítulos)

**Capítulos:**
1. Definição do Problema
2. Coleta e Preparação dos Dados
3. Análise Exploratória
4. Construção de Relatório
5. Apresentação do Projeto

**Objetivos de aprendizagem:**
- Transformar uma pergunta de negócio vaga em um problema de dados bem definido.
- Conduzir um projeto de dados do início ao fim, sem instruções passo a passo.
- Construir um relatório claro que comunique achados para quem não é técnico.
- Apresentar um projeto de dados como parte de um portfólio profissional.

**Descrição:** Depois de cinco sprints aprendendo ferramentas isoladas, chegou a hora de juntar tudo
em um projeto real, sem um roteiro de exercícios prontos. Este sprint é deliberadamente mais aberto:
o aluno escolhe (ou recebe) uma pergunta de negócio, define o escopo, coleta e prepara os dados, e
conduz uma análise exploratória usando tudo que aprendeu nos Sprints 1 a 5.

O diferencial deste sprint está na segunda metade: transformar a análise em um relatório e uma
apresentação que qualquer pessoa — inclusive alguém sem background técnico — consiga entender e usar
para tomar uma decisão. Comunicação é parte do trabalho de quem trabalha com dados, não um extra.

**Projeto integrador:** *Projeto Integrado 1* (um problema de negócio resolvido de ponta a ponta,
com relatório e apresentação final).

---

## Sprint 7 — Coleta e Armazenamento de Dados (SQL) (8 capítulos)

**Capítulos:**
1. Introdução a Bancos de Dados Relacionais
2. Consultas Básicas em SQL (SELECT)
3. Filtros e Ordenação (WHERE, ORDER BY)
4. Agregações (GROUP BY, HAVING)
5. JOINs entre Tabelas
6. Subconsultas
7. Conectando Python ao SQL
8. Projeto: Extraindo Insights com SQL

**Objetivos de aprendizagem:**
- Entender como dados são organizados em bancos relacionais (tabelas, chaves primárias/estrangeiras).
- Escrever consultas SQL para filtrar, ordenar e agregar dados.
- Combinar múltiplas tabelas com JOINs e subconsultas.
- Conectar Python a um banco de dados SQL e trazer os resultados para um DataFrame.

**Descrição:** Muitos dados do mundo real não vivem em um CSV — vivem em bancos de dados. Este sprint
ensina SQL do zero: o que é uma tabela, uma chave primária, e como escrever a consulta mais comum de
todas, o `SELECT ... WHERE ... ORDER BY`. Na sequência, o aluno aprende a agregar dados (totais,
médias por grupo) com `GROUP BY`, e a combinar tabelas com `JOIN` — a parte mais poderosa (e às vezes
confusa) do SQL.

O sprint fecha mostrando como tudo isso se conecta ao que já foi aprendido: Python pode se conectar
diretamente a um banco SQL, rodar consultas e trazer o resultado como um DataFrame do pandas, unindo
os dois mundos.

**Projeto integrador:** *Extraindo Insights com SQL* (consultas complexas com JOINs e agregações
sobre um banco de dados de exemplo, consumidas via Python).

---

## Sprint 8 — Introdução ao Aprendizado Automático (7 capítulos)

**Capítulos:**
1. O que é Machine Learning?
2. Tipos de Aprendizado
3. Preparação de Dados para Modelos
4. Métricas de Avaliação
5. Overfitting e Underfitting
6. Introdução ao Scikit-learn
7. Projeto: Primeiro Modelo Preditivo

**Objetivos de aprendizagem:**
- Entender o que é Machine Learning e diferenciá-lo de programação tradicional.
- Diferenciar aprendizado supervisionado, não supervisionado e por reforço.
- Preparar dados (normalização, codificação de categorias) para um modelo.
- Treinar e avaliar um primeiro modelo com scikit-learn.

**Descrição:** Este é o sprint da virada de chave: sair de "analisar dados que já aconteceram" para
"prever o que ainda vai acontecer". Começamos pela pergunta mais básica — o que é, de fato, Machine
Learning, e por que ele é diferente de simplesmente escrever regras `if/else`. Em seguida, o aluno
conhece os grandes tipos de aprendizado (supervisionado, não supervisionado) que vão estruturar o
resto do curso.

Antes de treinar qualquer modelo, é preciso preparar os dados corretamente — e é aqui que entram
conceitos como normalização e codificação de variáveis categóricas. O sprint termina com o
scikit-learn, a biblioteca padrão do mercado, usada para treinar e avaliar o primeiro modelo
preditivo do curso, já de olho em overfitting (quando o modelo "decora" os dados de treino).

**Projeto integrador:** *Primeiro Modelo Preditivo* (treinar e avaliar um modelo simples de
classificação ou regressão com scikit-learn).

---

## Sprint 9 — Aprendizado Supervisionado (8 capítulos)

**Capítulos:**
1. Regressão Linear
2. Regressão Logística
3. Árvores de Decisão
4. Florestas Aleatórias (Random Forest)
5. Máquinas de Vetores de Suporte (SVM)
6. Validação Cruzada
7. Ajuste de Hiperparâmetros
8. Projeto: Comparando Modelos Supervisionados

**Objetivos de aprendizagem:**
- Treinar modelos de regressão linear e logística para prever valores e categorias.
- Entender árvores de decisão e como florestas aleatórias combinam várias árvores.
- Usar SVM para problemas de classificação mais complexos.
- Validar modelos de forma robusta com validação cruzada e ajustar hiperparâmetros.

**Descrição:** Com as bases de Machine Learning estabelecidas, este sprint mergulha nos algoritmos de
aprendizado supervisionado mais usados no mercado. Regressão linear e logística abrem o caminho —
simples, interpretáveis e ainda assim extremamente usadas na prática. Em seguida, árvores de decisão
introduzem uma forma diferente de pensar (uma sequência de perguntas sim/não), que evolui para
florestas aleatórias, um dos algoritmos mais robustos e populares para dados tabulares.

A segunda metade do sprint foca em como comparar e melhorar modelos de forma justa: validação
cruzada (para não confiar em um único "corte" de treino/teste) e ajuste de hiperparâmetros (encontrar
a melhor configuração de cada algoritmo). O projeto final consolida tudo comparando vários modelos
lado a lado no mesmo problema.

**Projeto integrador:** *Comparando Modelos Supervisionados* (treinar e comparar ao menos 3
algoritmos diferentes no mesmo conjunto de dados).

---

## Sprint 10 — Aprendizado Automático para os Negócios (7 capítulos)

**Capítulos:**
1. ML Aplicado a Problemas de Negócio
2. Segmentação de Clientes
3. Previsão de Churn
4. Análise de Risco de Crédito
5. Otimização de Receita
6. Comunicação de Resultados para Stakeholders
7. Projeto: Caso de Negócio com ML

**Objetivos de aprendizagem:**
- Traduzir um problema de negócio em um problema de Machine Learning.
- Aplicar ML a casos clássicos: segmentação de clientes, churn e risco de crédito.
- Pensar em ML como ferramenta de otimização de receita, não só de previsão.
- Comunicar resultados de modelos para públicos não técnicos (stakeholders).

**Descrição:** Depois de dominar os algoritmos, este sprint responde a uma pergunta prática: como
tudo isso vira valor para uma empresa de verdade? O foco muda dos algoritmos para os casos de uso —
segmentar clientes para campanhas de marketing, prever quais clientes vão cancelar um serviço
(churn), e avaliar o risco de conceder crédito a alguém.

O sprint termina onde muitos cursos técnicos param cedo demais: como comunicar um modelo de Machine
Learning para quem vai decidir se usa (ou paga por) ele. Um modelo tecnicamente excelente que
ninguém entende não gera impacto — e esse é o principal aprendizado deste sprint.

**Projeto integrador:** *Caso de Negócio com ML* (um problema de negócio resolvido com ML e
apresentado como recomendação executiva).

---

## Sprint 11 — Álgebra Linear (7 capítulos)

**Capítulos:**
1. Vetores
2. Matrizes e Operações
3. Determinantes
4. Sistemas Lineares
5. Autovalores e Autovetores
6. Espaços Vetoriais
7. Aplicações em Machine Learning

**Objetivos de aprendizagem:**
- Entender vetores e matrizes como estruturas fundamentais de dados numéricos.
- Realizar operações matriciais (soma, multiplicação, transposição, inversão).
- Resolver sistemas lineares e calcular autovalores/autovetores.
- Conectar esses conceitos ao que já foi usado (sem perceber) em Machine Learning.

**Descrição:** Depois de usar bibliotecas prontas para treinar modelos, este sprint abre o capô e
mostra a matemática por trás delas. Álgebra Linear é a linguagem em que dados, imagens e modelos de
Machine Learning são efetivamente representados — cada linha de um DataFrame já é, matematicamente,
um vetor.

O sprint constrói esse entendimento de forma incremental: vetores, depois matrizes e suas operações,
sistemas lineares (resolver várias equações ao mesmo tempo) e autovalores/autovetores — o conceito
por trás de técnicas como PCA (redução de dimensionalidade), que o aluno vai reencontrar mais adiante
no curso. Cada capítulo fecha conectando a teoria a um uso real em ML.

**Projeto integrador:** *Aplicações de Álgebra Linear em Machine Learning* (implementar do zero,
com NumPy, uma operação usada internamente por um algoritmo de ML).

---

## Sprint 12 — Métodos Numéricos (8 capítulos)

**Capítulos:**
1. Introdução aos Métodos Numéricos
2. Interpolação
3. Diferenciação Numérica
4. Integração Numérica
5. Resolução de Equações Não Lineares
6. Otimização Numérica
7. Gradiente Descendente
8. Projeto: Otimização Aplicada

**Objetivos de aprendizagem:**
- Entender por que métodos numéricos (aproximados) são necessários quando não há solução exata.
- Interpolar valores e aproximar derivadas/integrais numericamente.
- Resolver equações não lineares e problemas de otimização.
- Implementar o algoritmo de gradiente descendente, usado no treino de quase todo modelo de ML.

**Descrição:** Muitos problemas em Ciência de Dados não têm uma fórmula fechada para resolver — é
preciso aproximar a resposta numericamente, passo a passo. Este sprint apresenta essa forma de
pensar: interpolar pontos entre dados conhecidos, aproximar derivadas e integrais quando a função não
é conhecida explicitamente, e resolver equações que não têm solução algébrica simples.

O ponto alto do sprint é o **gradiente descendente**: o algoritmo de otimização usado, por baixo dos
panos, para treinar praticamente todo modelo de Machine Learning e rede neural. Entender como ele
funciona (dar passos na direção que reduz o erro) tira o "mistério" de como um modelo realmente
aprende.

**Projeto integrador:** *Otimização Aplicada* (implementar gradiente descendente do zero para
ajustar os parâmetros de um modelo simples).

---

## Sprint 13 — Séries Temporais (5 capítulos)

**Capítulos:**
1. Fundamentos de Séries Temporais
2. Decomposição de Séries Temporais
3. Modelos ARIMA
4. Previsão com Séries Temporais
5. Projeto: Previsão de Demanda

**Objetivos de aprendizagem:**
- Reconhecer o que torna uma série temporal diferente de outros tipos de dados.
- Decompor uma série em tendência, sazonalidade e ruído.
- Treinar modelos ARIMA para prever valores futuros.
- Avaliar a qualidade de uma previsão de série temporal.

**Descrição:** Dados que mudam com o tempo — vendas mensais, temperatura diária, acessos a um site —
exigem uma abordagem própria, diferente dos modelos vistos até aqui. Este sprint começa mostrando por
que a ordem dos dados importa (algo que embaralharíamos sem pensar em outros contextos) e como
decompor uma série em três componentes: tendência, sazonalidade e ruído.

Com essa base, o aluno aprende os modelos ARIMA, uma família clássica e amplamente usada para
previsão de séries temporais, e fecha o sprint aplicando tudo isso a um problema muito comum no
mercado: prever a demanda futura de um produto ou serviço a partir do histórico.

**Projeto integrador:** *Previsão de Demanda* (modelo de série temporal treinado sobre um histórico
de vendas, com previsão para os próximos períodos).

---

## Sprint 14 — Aprendizado Automático para Textos (5 capítulos)

**Capítulos:**
1. Introdução ao Processamento de Linguagem Natural
2. Pré-processamento de Texto
3. Vetorização (Bag of Words, TF-IDF)
4. Classificação de Texto
5. Projeto: Análise de Sentimentos

**Objetivos de aprendizagem:**
- Entender os desafios específicos de trabalhar com texto em vez de números.
- Limpar e pré-processar texto (tokenização, remoção de stopwords, etc.).
- Transformar texto em vetores numéricos com Bag of Words e TF-IDF.
- Treinar um classificador de texto, aplicado a um problema de análise de sentimentos.

**Descrição:** Texto é, provavelmente, o tipo de dado mais abundante do mundo — reviews, comentários,
tickets de suporte, redes sociais — mas modelos de Machine Learning só entendem números. Este sprint
resolve esse problema em duas etapas: primeiro, limpar e padronizar o texto (removendo pontuação,
colocando tudo em minúsculas, eliminando palavras pouco informativas); depois, transformar esse texto
em vetores numéricos que um modelo consegue processar, usando técnicas como Bag of Words e TF-IDF.

Com o texto já "traduzido" para números, o sprint fecha treinando um classificador — aplicado ao caso
clássico de análise de sentimentos: dado um comentário, o modelo prevê se ele é positivo, negativo ou
neutro.

**Projeto integrador:** *Análise de Sentimentos* (classificador de texto treinado sobre um conjunto
de comentários/avaliações).

---

## Sprint 15 — Visão Computacional (6 capítulos)

**Capítulos:**
1. Fundamentos de Imagens Digitais
2. Processamento de Imagens com OpenCV
3. Redes Neurais Convolucionais (CNNs)
4. Classificação de Imagens
5. Detecção de Objetos
6. Projeto: Classificador de Imagens

**Objetivos de aprendizagem:**
- Entender como uma imagem é representada numericamente (pixels, canais de cor).
- Processar e transformar imagens com a biblioteca OpenCV.
- Entender a intuição por trás das Redes Neurais Convolucionais (CNNs).
- Treinar um classificador de imagens simples e reconhecer objetos em uma imagem.

**Descrição:** Assim como texto, imagens não são números "prontos" para um modelo — mas podem ser
representadas como uma grade de pixels, cada um com seus valores de cor. Este sprint começa por aí:
entender essa representação e aprender a manipular imagens (recortar, redimensionar, ajustar cores)
com a biblioteca OpenCV.

Na sequência, o aluno é apresentado às Redes Neurais Convolucionais (CNNs), a arquitetura por trás da
maioria dos avanços recentes em visão computacional, e usa esse conhecimento para treinar um
classificador de imagens simples, encerrando com uma introdução (conceitual) à detecção de objetos.

**Projeto integrador:** *Classificador de Imagens* (modelo treinado para distinguir entre duas ou
mais categorias de imagens).

---

## Sprint 16 — Aprendizado Não Supervisionado (4 capítulos)

**Capítulos:**
1. Clusterização com K-Means
2. Clusterização Hierárquica
3. Redução de Dimensionalidade (PCA)
4. Projeto: Segmentação sem Rótulos

**Objetivos de aprendizagem:**
- Entender a diferença entre aprendizado supervisionado e não supervisionado.
- Agrupar dados semelhantes com K-Means e clusterização hierárquica.
- Reduzir a dimensionalidade de um conjunto de dados com PCA (o mesmo conceito visto em Álgebra Linear).
- Interpretar clusters sem ter rótulos prévios para validar o resultado.

**Descrição:** Nem sempre os dados vêm com "respostas certas" para o modelo aprender — às vezes o
objetivo é simplesmente encontrar padrões e agrupamentos escondidos nos dados. Este sprint, mais
curto, é focado e direto: K-Means (o algoritmo de clusterização mais usado do mercado) e clusterização
hierárquica são apresentados lado a lado, com suas vantagens e limitações.

O sprint fecha revisitando PCA — já visto conceitualmente em Álgebra Linear — agora como ferramenta
prática para reduzir a dimensionalidade de um conjunto de dados antes de agrupá-lo ou visualizá-lo.

**Projeto integrador:** *Segmentação sem Rótulos* (agrupar um conjunto de dados sem categorias
prévias e interpretar os clusters encontrados).

---

## Sprint 17 — Projeto Final (3 capítulos)

**Capítulos:**
1. Definição e Planejamento do Projeto Final
2. Desenvolvimento e Modelagem
3. Apresentação e Portfólio

**Objetivos de aprendizagem:**
- Planejar um projeto de Ciência de Dados do zero, escolhendo problema e dados.
- Aplicar, de forma integrada, tudo o que foi aprendido nos 16 sprints anteriores.
- Construir um artefato de portfólio (notebook, relatório e/ou app) pronto para mostrar no mercado.
- Apresentar o projeto de forma clara para uma banca ou recrutador.

**Descrição:** O sprint de encerramento do curso é, propositalmente, o mais aberto de todos: o aluno
escolhe (com apoio da mentoria) um problema de dados que realmente lhe interesse, e o desenvolve do
zero — da definição do problema à modelagem — usando qualquer combinação das ferramentas vistas ao
longo dos 16 sprints anteriores (Python, pandas, SQL, Machine Learning, séries temporais, texto,
imagens, o que fizer sentido para o problema escolhido).

O resultado final não é só um notebook: é a peça central do portfólio profissional do aluno, com
documentação, relatório e uma apresentação pensada para impressionar recrutadores ou validar uma
transição de carreira para a área de dados.

**Projeto integrador:** *Projeto Final de Portfólio* (projeto de dados completo, do problema à
apresentação, escolhido e conduzido pelo próprio aluno).

---

## Status de produção do conteúdo

| Sprint | Status | Notebook |
|---|---|---|
| 1 — Python Básico | ✅ Completo (5 aulas) | `sprint1_exercicios.ipynb` + `aula2..5_*.ipynb` |
| 2 — Continuação de Python Básico | ✅ Completo | `sprint2_exercicios.ipynb` |
| 3 — Manipulação de Dados | ✅ Completo | `sprint3_exercicios.ipynb` |
| 4 — Análise Estatística de Dados | ✅ Completo | `sprint4_exercicios.ipynb` |
| 5 — Ferramentas de Desenvolvimento de Software | ✅ Completo | `sprint5_exercicios.ipynb` |
| 6 — Projeto Integrado 1 | ✅ Completo | `sprint6_exercicios.ipynb` |
| 7 — Coleta e Armazenamento de Dados (SQL) | ✅ Completo | `sprint7_exercicios.ipynb` |
| 8 — Introdução ao Aprendizado Automático | ✅ Completo | `sprint8_exercicios.ipynb` |
| 9 — Aprendizado Supervisionado | ✅ Completo | `sprint9_exercicios.ipynb` |
| 10 — Aprendizado Automático para os Negócios | ✅ Completo | `sprint10_exercicios.ipynb` |
| 11 — Álgebra Linear | ✅ Completo | `sprint11_exercicios.ipynb` |
| 12 — Métodos Numéricos | ✅ Completo | `sprint12_exercicios.ipynb` |
| 13 — Séries Temporais | ✅ Completo | `sprint13_exercicios.ipynb` |
| 14 — Aprendizado Automático para Textos | ✅ Completo | `sprint14_exercicios.ipynb` |
| 15 — Visão Computacional | ✅ Completo | `sprint15_exercicios.ipynb` |
| 16 — Aprendizado Não Supervisionado | ✅ Completo | `sprint16_exercicios.ipynb` |
| 17 — Projeto Final | ✅ Completo | `sprint17_exercicios.ipynb` |

*PyData Academy © 2026 — Licença MIT.*
