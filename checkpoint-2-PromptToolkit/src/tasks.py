tarefa = {
    "nome": "classificacao_urgencia",
    "tipo": "classificacao",  #
    "instrucao": "Analise o ticket de suporte e classifique a urgência como BAIXA, MÉDIA ou ALTA.",
    "formato_output": "Responda APENAS com a classificação em caixa alta.",
    "exemplos_fewshot": [
        {"input": "Meu login não funciona e preciso entregar um relatório agora!", "output": "ALTA"},
        {"input": "Como mudo a cor do meu perfil?", "output": "BAIXA"}
    ],
    "passos_cot": [
        "Verifique se há palavras que indicam interrupção de serviço.",
        "Identifique expressões de tempo (ex: agora, urgente, prazo).",
        "Avalie o impacto emocional do usuário."
    ],
    "persona": "analista_suporte_senior"
}

tarefa = {
    "nome": "extracao_dados_financeiros",
    "tipo": "extracao",  #
    "instrucao": "Extraia o ativo, a operação e o valor mencionado no texto.",
    "formato_output": "Responda em formato JSON.",
    "exemplos_fewshot": [
        {"input": "Comprei 10 cotas de CPTS11 por 80 reais.", "output": "{\"ativo\": \"CPTS11\", \"operacao\": \"compra\", \"valor\": 80.00}"}
    ],
    "passos_cot": [
        "Localize o código do ativo (ticker).",
        "Identifique se o verbo indica compra ou venda.",
        "Normalize o valor numérico para ponto flutuante."
    ],
    "persona": "assistente_financeiro"
}

tarefa = {
    "nome": "sumarizacao_erro_sistema",
    "tipo": "sumarizacao",  #
    "instrucao": "Resuma o erro técnico em uma única frase explicativa para não-desenvolvedores.",
    "formato_output": "Um parágrafo de no máximo 20 palavras.",
    "exemplos_fewshot": [
        {"input": "Error 500: Connection timeout at database_cluster_01 via MySQL connector.", "output": "O sistema perdeu a conexão com o banco de dados principal."}
    ],
    "passos_cot": [
        "Identifique o componente que falhou (banco de dados, API, UI).",
        "Traduza termos técnicos para linguagem de negócios.",
        "Remova detalhes de endereços de memória ou caminhos de arquivo."
    ],
    "persona": "gerente_projetos_tech"
}