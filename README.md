# Interpretador de Expressões Aritméticas com IA

## Descrição

Este projeto utiliza um modelo de linguagem baseado em inteligência artificial para interpretar e avaliar expressões aritméticas. Ele emprega o modelo microsoft/phi-2 da biblioteca transformers para processar e calcular expressões matemáticas, mesmo quando escritas de forma não convencional.

A interface gráfica é construída com Gradio, permitindo que os usuários interajam facilmente com o interpretador de expressões.

## Instalação e Configuração

### 1. Criar um ambiente virtual (recomendado)
Para manter as dependências isoladas, crie um ambiente virtual com o seguinte comando:

python -m venv venv

### 2. Ativar o ambiente virtual

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate

### 3. Instalar dependências

Após ativar o ambiente virtual, instale todas as bibliotecas necessárias executando:

pip install -r requirements.txt

Isso instalará as seguintes bibliotecas:

gradio: Para construção da interface gráfica.
transformers: Para uso do modelo de linguagem microsoft/phi-2.
torch: Para suporte à execução do modelo.

Caso precise instalar manualmente, use:

pip install gradio transformers torch

## Executando o Projeto

Após configurar o ambiente, execute o script principal para iniciar a análise:

python programa.py

Isso inicializará a interface gráfica onde você poderá inserir expressões aritméticas para avaliação.

## Como Funciona

O usuário insere uma expressão matemática (exemplo: 2 + (3 * 4) / 2).

O modelo microsoft/phi-2 processa e interpreta a expressão.

O resultado é exibido na interface de Gradio.

## Autores

Lucas Ryuji Fujimoto
Britney Brevio dos Santos Lima
Thiago Vinicius Araújo

## Considerações Finais

Este projeto demonstra o poder dos modelos de linguagem na interpretação de cálculos matemáticos. A interface intuitiva e acessível permite que usuários experimentem a IA para resolver expressões aritméticas de maneira eficiente.
