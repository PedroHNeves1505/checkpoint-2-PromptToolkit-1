def montar_prompt(instrucao, contexto, input_dados, formato_output):

    if not all([instrucao, contexto, input_dados, formato_output]):
        raise ValueError("Todos os componentes do prompt devem ser preenchidos.")

    prompt_estruturado = f"Contexto: {contexto}\nInstruções: {instrucao}\nDados de Entrada: {input_dados}\nFormato de Saída: {formato_output}".strip()

    return prompt_estruturado

def adicionar_exemplos(prompt, exemplos):

    bloco_exemplos = "\n\n### EXEMPLOS"
    for ex in exemplos:
        bloco_exemplos += f"\nInput: {ex.get('input')} -> Output: {ex.get('output')}"
    
    return prompt + bloco_exemplos

def adicionar_cot(prompt, passos):

    instrucao_cot = f"\n\n### RACIOCÍNIO PASSO A PASSO\nPor favor, execute a tarefa seguindo estes {passos} passos lógicos antes de fornecer a resposta final."
    
    return prompt + instrucao_cot