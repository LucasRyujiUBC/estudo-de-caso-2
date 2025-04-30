import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Define o nome do modelo a ser utilizado
model_name = "microsoft/phi-2"  
tokenizer = AutoTokenizer.from_pretrained(model_name)  # Carrega o tokenizador do modelo
model = AutoModelForCausalLM.from_pretrained(model_name)  # Carrega o modelo para processamento de linguagem natural


def interpretar(expressao: str) -> str:
    """
    Função que recebe uma expressão matemática como entrada e a interpreta utilizando um modelo de IA.
    """
    prompt = f"Calcule o seguinte: {expressao}\nResposta:"  # Define o prompt para o modelo
    inputs = tokenizer(prompt, return_tensors="pt")  # Tokeniza o prompt e o transforma em tensores compatíveis com PyTorch
    
    with torch.no_grad():  # Desativa o cálculo de gradientes para economizar recursos computacionais
        outputs = model.generate(
            **inputs,
            max_new_tokens=30,  # Limita a quantidade de novos tokens gerados
            do_sample=False,  # Garante que a geração seja determinística
            temperature=0.2,  # Define a temperatura para controlar a aleatoriedade da geração
            pad_token_id=tokenizer.eos_token_id  # Define o token de preenchimento para evitar erros
        )
    
    resultado = tokenizer.decode(outputs[0], skip_special_tokens=True)  # Decodifica a saída gerada pelo modelo
    
    # Processa a resposta para extrair apenas o resultado final
    if "Resposta:" in resultado:
        resposta = resultado.split("Resposta:")[-1].strip()  # Se houver "Resposta:", extrai apenas o resultado
    else:
        resposta = resultado.strip()  # Caso contrário, apenas remove espaços extras
    
    return resposta  # Retorna o resultado final


def iniciar_interface():
    """
    Função que inicializa a interface gráfica utilizando Gradio.
    """
    with gr.Blocks() as demo:
        gr.Markdown("## 🧠 Interpretador de Expressões Aritméticas com IA")  # Adiciona um título à interface
        gr.Markdown("Digite uma expressão matemática com ou sem erros. A IA tentará interpretá-la corretamente.")  # Adiciona uma descrição
        
        entrada = gr.Textbox(label="Expressão Aritmética", placeholder="Exemplo: 2 + (3 * 4) / 2")  # Campo de entrada
        saida = gr.Textbox(label="Resultado")  # Campo de saída
        
        botao = gr.Button("Avaliar")  # Botão de execução
        botao.click(fn=interpretar, inputs=entrada, outputs=saida)  # Define a ação do botão para chamar a função interpretar

    demo.launch(share=True)  # Inicia a interface e a torna acessível via link externo


iniciar_interface()  # Chama a função para iniciar a interface gráfica
