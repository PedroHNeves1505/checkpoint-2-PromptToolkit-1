import json

def montar_prompt(tipo_tarefa, persona_texto, instrucao, input_dados, formato_output):
    if not all([tipo_tarefa, persona_texto, instrucao, input_dados, formato_output]):
        raise ValueError("Todos os componentes do prompt devem ser preenchidos.")

    try:
        with open('prompts/templates.json', 'r', encoding='utf-8') as f:
            templates = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Arquivo templates.json não encontrado na pasta prompts/.")

    template_data = templates.get(tipo_tarefa)
    if not template_data:
        raise ValueError(f"Tipo de tarefa '{tipo_tarefa}' não encontrado no templates.json.")
    
    template_string = template_data.get("template")

    prompt_estruturado = template_string.format(
        contexto=persona_texto,
        instrucao=instrucao,
        input_dados=input_dados,
        formato_output=formato_output
    )

    return prompt_estruturado.strip()

def adicionar_exemplos(prompt, exemplos):
    if not exemplos:
        return prompt

    bloco_exemplos = "\n\n### EXEMPLOS"
    for ex in exemplos:
        bloco_exemplos += f"\nInput: {ex.get('input')} -> Output: {ex.get('output')}"
    
    return prompt + bloco_exemplos

def adicionar_cot(prompt, passos):
    if not passos:
        return prompt

    passos_formatados = "\n".join([f"- {passo}" for passo in passos])
    
    instrucao_cot = f"\n\n### RACIOCÍNIO PASSO A PASSO\nPor favor, execute a tarefa seguindo estes passos lógicos antes de fornecer a resposta final:\n{passos_formatados}"
    
    return prompt + instrucao_cot