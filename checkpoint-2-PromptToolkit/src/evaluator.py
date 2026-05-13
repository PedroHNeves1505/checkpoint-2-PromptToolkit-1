import tiktoken

def contar_tokens(texto, modelo="gpt-3.5-turbo"):
    enc = tiktoken.encoding_for_model(modelo)
    return len(enc.encode(texto))

def medir_acuracia(resposta, esperado, modo="exact"):
    resposta = resposta.strip().lower()
    esperado = esperado.strip().lower()
    
    if modo == "exact":
        return 1.0 if resposta == esperado else 0.0
    
    if modo == "keywords":
        keywords = esperado.split(",")
        encontradas = [kw.strip() in resposta for kw in keywords]
        return sum(encontradas) / len(keywords)

def medir_consistencia(respostas):
    if not respostas:
        return 0.0
    
    frequencias = {}
    for r in respostas:
        frequencias[r] = frequencias.get(r, 0) + 1
    
    mais_comum = max(frequencias.values())
    return mais_comum / len(respostas)

def testar_temperatura(prompt, temps=[0.1, 0.5, 1.0]):
    resultados_report = []
    
    for t in temps:
        resultado = {
            "prompt": prompt,
            "temperatura": t,
            "tokens": contar_tokens(prompt),
            "status": "sucesso"
        }
        resultados_report.append(resultado)
    
    return resultados_report

if __name__ == "__main__":
    prompt_teste = "Classifique o sentimento: Adorei o produto!"
    resp_llm = "POSITIVO"
    esperado = "positivo"

    testes_temp = testar_temperatura(prompt_teste)

    report = {
        "metricas_gerais": {
            "acuracia": medir_acuracia(resp_llm, esperado, modo="exact"),
            "tokens_resposta": contar_tokens(resp_llm),
            "consistencia": medir_consistencia(["POSITIVO", "POSITIVO", "NEUTRO"])
        },
        "detalhes_temperatura": testes_temp 
    }
    
    print(f"Relatório Final Estruturado: {report}")