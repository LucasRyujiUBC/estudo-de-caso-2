import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


model_name = "microsoft/phi-2"  
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


def interpretar(expressao: str) -> str:
    prompt = f"Calcule o seguinte: {expressao}\nResposta:"
    inputs = tokenizer(prompt, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=30,
            do_sample=False,
            temperature=0.2,
            pad_token_id=tokenizer.eos_token_id
        )
    
    resultado = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    
    if "Resposta:" in resultado:
        resposta = resultado.split("Resposta:")[-1].strip()
    else:
        resposta = resultado.strip()
    
    return resposta


def iniciar_interface():
    with gr.Blocks() as demo:
        gr.Markdown("## 🧠 Interpretador de Expressões Aritméticas com IA")
        gr.Markdown("Digite uma expressão matemática com ou sem erros. A IA tentará interpretá-la corretamente.")

        entrada = gr.Textbox(label="Expressão Aritmética", placeholder="Exemplo: 2 + (3 * 4) / 2")
        saida = gr.Textbox(label="Resultado")

        botao = gr.Button("Avaliar")
        botao.click(fn=interpretar, inputs=entrada, outputs=saida)

    demo.launch(share=True)


iniciar_interface()