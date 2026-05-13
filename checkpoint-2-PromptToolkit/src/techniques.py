from .prompt_builder import montar_prompt, adicionar_exemplos, adicionar_cot

def zero_shot(tarefa, input_dados):
    return montar_prompt(
        instrucao=tarefa,
        contexto="Execução direta de tarefa.",
        input_dados=input_dados,
        formato_output="Texto claro e direto."
    )

def few_shot(tarefa, input_dados, lista_exemplos):
    prompt_base = montar_prompt(tarefa, "Uso de exemplos para guia.", input_dados, "Seguir o padrão dos exemplos.")
    return adicionar_exemplos(prompt_base, lista_exemplos)

def chain_of_thought(tarefa, input_dados, passos):
    prompt_base = montar_prompt(tarefa, "Raciocínio lógico necessário.", input_dados, "Resposta final após raciocínio.")
    return adicionar_cot(prompt_base, passos)

def role_prompting(tarefa, input_dados, persona_dict):
    system_prompt = f"Você é {persona_dict.get('nome')}. {persona_dict.get('descricao')}"
    user_prompt = montar_prompt(tarefa, "Atuação de persona.", input_dados, "De acordo com o perfil da persona.")
    return (system_prompt, user_prompt)