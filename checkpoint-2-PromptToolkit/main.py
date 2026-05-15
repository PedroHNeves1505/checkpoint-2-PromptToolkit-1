import json
import os
import time
import pandas as pd
from src import LLMClient, montar_prompt, adicionar_exemplos, adicionar_cot
from src.tasks import tarefa_urgencia, tarefa_financeira, tarefa_erro
from src.report import gerar_tabela, grafico_acuracia, grafico_custo, grafico_temperatura, recomendar

os.makedirs('output/graficos', exist_ok=True)
client = LLMClient() 

def carregar_json(caminho):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, caminho)
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

try:
    personas = carregar_json('prompts/system_prompts.json')
except Exception:
    personas = {}

lista_tarefas = [tarefa_urgencia, tarefa_financeira, tarefa_erro]
resultados_finais = []

print("🚀 Iniciando Toolkit FIAP (Motor: Groq)...")

for i, tarefa in enumerate(lista_tarefas):
    print(f"\n📦 Executando: {tarefa['nome']} ({i+1}/{len(lista_tarefas)})")
    
    persona_dados = personas.get(tarefa['persona'], {})
    contexto_persona = f"{persona_dados.get('descricao', '')} {persona_dados.get('contexto', '')}"
    input_usuario = tarefa['exemplos_fewshot'][0]['input']
    
    prompt = montar_prompt(
        tipo_tarefa=tarefa['tipo'], 
        persona_texto=contexto_persona,
        instrucao=tarefa['instrucao'],
        input_dados=input_usuario,
        formato_output=tarefa['formato_output']
    )
    
    prompt = adicionar_exemplos(prompt, tarefa['exemplos_fewshot'])
    prompt = adicionar_cot(prompt, tarefa['passos_cot'])

    resposta = client.chat(
        prompt=prompt,
        system=persona_dados.get('descricao', 'Assistente Especialista'),
        temp=0.1
    )
    
    if resposta:
        resultados_finais.append({
            "tarefa": tarefa['nome'],
            "tecnica": tarefa['tipo'], 
            "resposta": resposta['resposta'],
            "tempo_ms": resposta['tempo_ms'],
            "tokens": resposta['tokens_prompt'] + resposta['tokens_resposta']
        })
        print(f"✅ Tarefa concluída.")
    else:
        print(f"❌ Erro na tarefa {tarefa['nome']}.")

    if i < len(lista_tarefas) - 1:
        time.sleep(10)

if resultados_finais:
    print("\n📊 Gerando relatórios e gráficos finais...")

    gerar_tabela(resultados_finais)     
    grafico_acuracia(resultados_finais)  
    grafico_custo(resultados_finais)   
    grafico_temperatura(resultados_finais)
    recomendar(resultados_finais)       
    
    print("\n✨ Checkpoint concluído com sucesso! Pasta /output atualizada.")
else:
    print("\n⚠️ Falha crítica: Nenhum dado processado para gerar relatórios.")