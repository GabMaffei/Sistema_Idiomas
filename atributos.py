# atributos e seus pesos correspondentes usados pra calcular a similaridade entre os casos
atributos = {
    'idioma_alvo': 0.5,  # é um atributo importante que influencia na escolha de recurso
    # e métodos de ensino que quer se aprender
    'nivel_idioma': 0.4,  # influencia na escolha de conteúdos do ensino e velocidade no aprendizado
    'objetivo_aprendizagem': 0.3,  # atributo crítico que define as metas e expectativas em relação
    # ao usuário na questão do plano de ensino
    'tempo_disponivel': 0.3,  # tem a ver com o ritmo do cronograma das aulas,
    # tendo a ver com a frequencia e duração das sessões
    'recursos_aprendizagem': 0.3,  # podendo afetar a eficácia do método de ensino utilizado
    # e como o conteúdo é apresentado
    'comunidade': 0.2  # indica a comunidade de aprendizagem à qual o usuário pertence ou deseja interagir.
}

# valores possíveis para idioma_alvo/recursos_aprendizagem/nivel_idioma/comunidade mapeados para números
# usando dicionários de modo que possam ser comparados numericamente
idioma_alvo_valores = ['Alemão', 'Inglês', 'Italiano', 'Francês', 'Japonês', 'Espanhol']
recursos_aprendizagem_valores = ['musicas', 'filmes', 'series', 'livros']
nivel_idioma_valores = ['Iniciante', 'Intermediario', 'Avançado']
comunidade_valores = ['acadêmicos', 'professores', 'funcionários']

# dicionário para mapear os rótulos de texto para valores idioma_alvo/recursos_aprendizagem/nivel_idioma/comunidade
idioma_alvo_dic = {valor: i for i, valor in enumerate(idioma_alvo_valores)}
recursos_aprendizagem_dic = {valor: i for i, valor in enumerate(recursos_aprendizagem_valores)}
nivel_idioma_dic = {valor: i for i, valor in enumerate(nivel_idioma_valores)}
comunidade_dic = {valor: i for i, valor in enumerate(comunidade_valores)}
