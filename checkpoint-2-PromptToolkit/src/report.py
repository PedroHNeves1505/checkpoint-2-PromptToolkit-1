import pandas as pd
import matplotlib.pyplot as plt

def gerar_tabela(resultados):
    df = pd.DataFrame(resultados)
    df.to_csv("relatorio_performance.csv", index=False)
    print("Tabela gerada e salva como 'relatorio_performance.csv'")
    return df

def grafico_acuracia(resultados):
    df = pd.DataFrame(resultados)
    acuracia_media = df.groupby('tecnica')['acuracia'].mean()
    
    acuracia_media.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'])
    plt.title('Acurácia Média por Técnica')
    plt.ylabel('Acurácia (0-1)')
    plt.xlabel('Técnica')
    plt.show()

def grafico_custo(resultados):
    df = pd.DataFrame(resultados)
    custo_medio = df.groupby('tecnica')['tokens'].mean()
    
    custo_medio.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição Média de Custo (Tokens) por Técnica')
    plt.ylabel('')
    plt.show()

def grafico_temperatura(resultados):
    df = pd.DataFrame(resultados)
    cons_temp = df.groupby('temperatura')['consistencia'].mean()
    
    plt.plot(cons_temp.index, cons_temp.values, marker='o', linestyle='--')
    plt.title('Impacto da Temperatura na Consistência')
    plt.xlabel('Temperatura')
    plt.ylabel('Consistência')
    plt.grid(True)
    plt.show()

def recomendar(resultados):
    df = pd.DataFrame(resultados)
    melhor = df.groupby('tecnica')['acuracia'].mean().idxmax()
    acuracia_val = df.groupby('tecnica')['acuracia'].mean().max()
    
    justificativa = f"A técnica '{melhor}' é a recomendada pois atingiu a maior acurácia média ({acuracia_val:.2f})."
    
    return {"melhor_tecnica": melhor, "justificativa": justificativa}

if __name__ == "__main__":
    dados_exemplo = [
        {"tecnica": "Few-shot", "acuracia": 0.85, "tokens": 450, "temperatura": 0.1, "consistencia": 0.95},
        {"tecnica": "Few-shot", "acuracia": 0.80, "tokens": 450, "temperatura": 0.7, "consistencia": 0.70},
        {"tecnica": "Zero-shot", "acuracia": 0.65, "tokens": 120, "temperatura": 0.1, "consistencia": 0.98},
        {"tecnica": "CoT", "acuracia": 0.95, "tokens": 800, "temperatura": 0.1, "consistencia": 0.90},
        {"tecnica": "CoT", "acuracia": 0.92, "tokens": 800, "temperatura": 0.5, "consistencia": 0.85}
    ]

    df_final = gerar_tabela(dados_exemplo)
    recomendacao = recomendar(dados_exemplo)
    
    print(f"\nRECOMENDAÇÃO: {recomendacao['melhor_tecnica']}")
    print(f"POR QUÊ? {recomendacao['justificativa']}")
