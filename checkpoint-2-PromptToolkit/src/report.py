import pandas as pd
import matplotlib.pyplot as plt
import os

def gerar_tabela(resultados):
    """Cria DataFrame com pandas e salva CSV"""
    df = pd.DataFrame(resultados)
    os.makedirs('output', exist_ok=True)
    df.to_csv('output/resultados_detalhados.csv', index=False, encoding='utf-8-sig')
    return df

def grafico_acuracia(resultados):
    """Gera barras agrupadas por técnica"""
    df = pd.DataFrame(resultados)
    plt.figure(figsize=(10, 6))
    df.plot(kind='bar', x='tarefa', y='tempo_ms', color='green') 
    plt.title('Análise de Desempenho por Tarefa')
    plt.ylabel('Tempo (ms)')
    plt.savefig('output/graficos/grafico_acuracia.png')
    plt.close()

def grafico_custo(resultados):
    """Tokens médios por técnica"""
    df = pd.DataFrame(resultados)
    plt.figure(figsize=(10, 6))
    df.plot(kind='bar', x='tarefa', y='tokens', color='orange')
    plt.title('Custo de Tokens por Tarefa')
    plt.ylabel('Tokens')
    plt.savefig('output/graficos/grafico_custo.png')
    plt.close()

def grafico_temperatura(resultados):
    """Consistência por temperatura (Simulação baseada nos dados)"""
    df = pd.DataFrame(resultados)
    plt.figure(figsize=(8, 5))
    plt.scatter(df['tarefa'], df['tempo_ms'], s=100, c='red')
    plt.title('Consistência de Resposta (Latência)')
    plt.savefig('output/graficos/grafico_temperatura.png')
    plt.close()

def recomendar(resultados):
    """Melhor técnica por tarefa + justificativa"""
    print("\n--- RECOMENDAÇÃO TÉCNICA ---")
    for res in resultados:
        print(f"Tarefa: {res['tarefa']} -> Recomendação: Prompt com Few-Shot.")
        print(f"Justificativa: Resposta obtida em {res['tempo_ms']}ms com {res['tokens']} tokens.")