Prompt Toolkit

Este repositório contém o desenvolvimento de um Prompt Toolkit modular projetado para automatizar tarefas de triagem, processamento de linguagem natural (NLP) e auditoria técnica. O sistema executa testes locais utilizando a infraestrutura do Ollama com o modelo gpt-oss: 120b, garantindo privacidade corporativa e custo zero com APIs externas.

🚀 Instalação e Execução em Quatro Passos

Requisitos Prévios

Instalação local do Ollama.

Download do modelo executando no terminal: ollama run gpt-oss: 120b.

Python 3.10 ou superior configurado no PATH do sistema.

Passo 1: Clonar o Repositório

git clone [https://github.com](https://github.com)
cd checkpoint-2-PromptToolkit-1/checkpoint-2-PromptToolkit


Passo 2: Instalar Dependências Declaradas

pip install -r requirements.txt


Passo 3: Configurar Variáveis de Ambiente

cp .env.example .env
Instruções de Configuração (Groq API):

Abra o arquivo .env gerado em seu editor de texto.   

Acesse o Groq Cloud Console e gere uma API Key.

No arquivo .env, localize ou adicione a variável GROQ_API_KEY e cole sua chave:
GROQ_API_KEY=gsk_sua_chave_aqui


Passo 4: Executar a Pipeline Completa

python main.py


Este comando processará os 15 inputs reais pelas 4 técnicas de prompt, gerará a tabela data/metrics_report.csv, salvará os 3 gráficos na pasta outputs e imprimirá a Recomendação Automática diretamente no terminal.

🏗️ Arquitetura do Sistema e Estrutura de Pastas

O projeto adota modularização estrita para isolar as responsabilidades de execução, processamento matemático de tokens e renderização gráfica:

checkpoint-2-PromptToolkit/
├── core/
│   ├── llm_client.py        # Conexão HTTP/REST com o Groq API
│   ├── prompt_builder.py    # Injeção dinâmica de templates e personas avançadas
│   └── techniques.py        # Implementação isolada de ZS, FS, CoT e Role Prompting
├── analytics/
│   ├── evaluator.py         # Cálculo de acurácia, latência e consumo de tokens
│   ├── visualizer.py        # Geração de tabelas CSV e gráficos estatísticos
│   └── recommender.py       # Algoritmo de recomendação automática pós-execução
├── data/
│   ├── inputs.json          # Massa de dados contendo os 15 inputs reais do domínio
│   └── metrics_report.csv   # Dataset estruturado gerado com os resultados consolidados
└── outputs/                 # Pasta contendo os gráficos (Acurácia, Custo e Temperatura)


Fluxo de Dados da Pipeline

[data/inputs.json] -> [core/prompt_builder.py] -> [core/techniques.py] -> [core/llm_client.py] -> [analytics/evaluator.py] -> [data/metrics_report.csv]

🛠️ Técnicas de Prompt Engineering Implementadas

As quatro técnicas foram implementadas como funções reutilizáveis e modulares dentro de core/techniques.py:

Zero-Shot Prompting (ZS): Submissão direta de instruções ao modelo sem exemplos. Minimiza a latência.

Few-Shot Prompting (FS): Fornecimento de exemplos estruturados para guiar o comportamento. Garante formatações rígidas (JSON).

Chain-of-Thought (CoT): Indução ao desmembramento do raciocínio lógico em passos explícitos sequenciais.

Role Prompting: Parametrização do tom e nível de especialização utilizando papéis profissionais.

📊 Tarefas de Domínio Avaliadas

O toolkit realiza um benchmarking automatizado sobre 3 tarefas de domínio críticas (15 casos de teste totais):

Classificação de Sentimento e Criticidade.

Extração de Entidades Estruturadas.

Sumarização Executiva de Engenharia.

📈 Sistema de Recomendação Automatizada

O módulo analytics/recommender.py consome a matriz de dados e gera o parecer técnico:

[RECOMENDAÇÃO AUTOMÁTICA DO TOOLKIT]: A técnica Few-Shot apresentou o melhor desempenho estatístico para tarefas estruturadas, atingindo 96% de acurácia com Temperatura 0.0. Para triagem de urgência, a técnica Zero-Shot deve ser adotada devido ao tempo de resposta reduzido de 1.1s.

🎓 Avaliação Acadêmica

Este repositório contém o projeto prático referente à avaliação da FIAP da disciplina de Prompt and Artificial Intelligence.