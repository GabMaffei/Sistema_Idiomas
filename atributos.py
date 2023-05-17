# atributos e seus pesos correspondentes usados pra calcular a similaridade entre os casos
atributos = {
    'idioma_alvo': 0.3, #é um atributo importante que influencia na escolha de recurso e métodos de ensino que quer se aprender
    'nivel_idioma': 0.2, #influencia na escolha de conteúdos do ensino e velocidade no aprendizado
    'objetivo_aprendizagem': 0.4, #atributo crítico que define as metas e expectativas em relação ao usuário na questão do plano de ensino
    'tempo_disponivel': 0.05, #tem a ver com o ritmo do cronograma das aulas, tendo a ver com a frequencia e duração das sessões
    'recursos_aprendizagem': 0.05, #podendo afetar a eficácia do método de ensino utilizado e a forma como o conteúdo é apresentado
    'comunidade': 0.1 #indica a comunidade de aprendizagem à qual o usuário pertence ou deseja interagir.
}

# valores possíveis para idioma_alvo_valores/recursos_aprendizagem/nivel_idioma_valores que são mapeados para números usando dicionários de modo que possam ser comparados numericamente
idioma_alvo_valores = ['Alemão', 'Inglês', 'Italiano', 'Francês', 'Japonês', 'Espanhol']
recursos_aprendizagem_valores = ['musicas', 'filmes', 'series', 'livros']
nivel_idioma_valores = ['Iniciante', 'Intermediario', 'Avançado']
comunidade_valores = ['acadêmicos', 'professores', 'funcionários']

# dicionário pra mapear os rótulos de texto para valores idioma_alvo/recursos_aprendizagem/nivel_idioma
idioma_alvo_dic = {valor: i for i, valor in enumerate(idioma_alvo_valores)}
recursos_aprendizagem_dic = {valor: i for i, valor in enumerate(recursos_aprendizagem_valores)}
nivel_idioma_dic = {valor: i for i, valor in enumerate(nivel_idioma_valores)}
comunidade_dic = {valor: i for i, valor in enumerate(comunidade_valores)}
