def zero_shot(tarefa, input):
    prompt = f'Terefaa: {tarefa}\nDados: {input}'
    return prompt


def few_shot(tarefa, input, exemplos):
    prompt = f'Tarefa: {tarefa}\nDados: {input}\nExemplos: {exemplos}'
    return prompt

def chain_of_thought(tarefa, input, passos):
    prompt: f'Tarfea: {tarefa}\nDados: {input}\nPasso a Passo: {passos}'
    return prompt


def role_prompting(tarefa, input, persona):
    prompt = f'Persona: {persona}\nTarefa: {tarefa}\nDados: {input}'
    return prompt