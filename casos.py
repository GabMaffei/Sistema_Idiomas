from atributos import *

# base de casos registrados como uma lista de 50 casos
base_casos = [
    {
        'idioma_alvo': idioma_alvo_dic['Espanhol'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 7,
        'tempo_disponivel': 1.3,
        'recursos_aprendizagem': recursos_aprendizagem_dic['musicas'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Japonês'],
        'nivel_idioma': nivel_idioma_dic['Intermediario'],
        'objetivo_aprendizagem': 4,
        'tempo_disponivel': 4,
        'recursos_aprendizagem': recursos_aprendizagem_dic['series'],
        'comunidade': comunidade_dic['professores']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Francês'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 8,
        'tempo_disponivel': 6,
        'recursos_aprendizagem': recursos_aprendizagem_dic['livros'],
        'comunidade': comunidade_dic['professores']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Inglês'],
        'nivel_idioma': nivel_idioma_dic['Intermediario'],
        'objetivo_aprendizagem': 6,
        'tempo_disponivel': 2,
        'recursos_aprendizagem': recursos_aprendizagem_dic['filmes'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Espanhol'],
        'nivel_idioma': nivel_idioma_dic['Avançado'],
        'objetivo_aprendizagem': 7,
        'tempo_disponivel': 3,
        'recursos_aprendizagem': recursos_aprendizagem_dic['filmes'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Italiano'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 6,
        'tempo_disponivel': 5,
        'recursos_aprendizagem': recursos_aprendizagem_dic['livros'],
        'comunidade': comunidade_dic['professores']
    },
     {
        'idioma_alvo': idioma_alvo_dic['Espanhol'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 9,
        'tempo_disponivel': 1.2,
        'recursos_aprendizagem': recursos_aprendizagem_dic['musicas'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Inglês'],
        'nivel_idioma': nivel_idioma_dic['Intermediario'],
        'objetivo_aprendizagem': 10,
        'tempo_disponivel': 0.30,
        'recursos_aprendizagem': recursos_aprendizagem_dic['series'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Italiano'],
        'nivel_idioma': nivel_idioma_dic['Avançado'],
        'objetivo_aprendizagem': 4,
        'tempo_disponivel': 5.5,
        'recursos_aprendizagem': recursos_aprendizagem_dic['musicas'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Alemão'],
        'nivel_idioma': nivel_idioma_dic['Avançado'],
        'objetivo_aprendizagem': 6,
        'tempo_disponivel': 7,
        'recursos_aprendizagem': recursos_aprendizagem_dic['series'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Espanhol'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 8,
        'tempo_disponivel': 1,
        'recursos_aprendizagem': recursos_aprendizagem_dic['livros'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Italiano'],
        'nivel_idioma': nivel_idioma_dic['Intermediario'],
        'objetivo_aprendizagem': 10,
        'tempo_disponivel': 2,
        'recursos_aprendizagem': recursos_aprendizagem_dic['filmes'],
        'comunidade': comunidade_dic['professores']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Espanhol'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 2,
        'tempo_disponivel': 1.5,
        'recursos_aprendizagem': recursos_aprendizagem_dic['musicas'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Alemão'],
        'nivel_idioma': nivel_idioma_dic['Intermediario'],
        'objetivo_aprendizagem': 8.2,
        'tempo_disponivel': 6,
        'recursos_aprendizagem': recursos_aprendizagem_dic['series'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Inglês'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 5,
        'tempo_disponivel': 2,
        'recursos_aprendizagem': recursos_aprendizagem_dic['livros'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Japonês'],
        'nivel_idioma': nivel_idioma_dic['Intermediario'],
        'objetivo_aprendizagem': 4,
        'tempo_disponivel': 4,
        'recursos_aprendizagem': recursos_aprendizagem_dic['series'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Italiano'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 9,
        'tempo_disponivel': 2.30,
        'recursos_aprendizagem': recursos_aprendizagem_dic['filmes'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Alemão'],
        'nivel_idioma': nivel_idioma_dic['Intermediario'],
        'objetivo_aprendizagem': 4,
        'tempo_disponivel': 3.30,
        'recursos_aprendizagem': recursos_aprendizagem_dic['livros'],
        'comunidade': 3
    },
    {
        'idioma_alvo': idioma_alvo_dic['Espanhol'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 9,
        'tempo_disponivel': 1,
        'recursos_aprendizagem': recursos_aprendizagem_dic['musicas'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Japonês'],
        'nivel_idioma': nivel_idioma_dic['Intermediario'],
        'objetivo_aprendizagem': 10,
        'tempo_disponivel': 3,
        'recursos_aprendizagem': recursos_aprendizagem_dic['livros'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Espanhol'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 7,
        'tempo_disponivel': 2,
        'recursos_aprendizagem': recursos_aprendizagem_dic['musicas'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Inglês'],
        'nivel_idioma': nivel_idioma_dic['Avançado'],
        'objetivo_aprendizagem': 10,
        'tempo_disponivel': 4,
        'recursos_aprendizagem': recursos_aprendizagem_dic['series'],
        'comunidade': comunidade_dic['professores']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Espanhol'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 3,
        'tempo_disponivel': 0.50,
        'recursos_aprendizagem': recursos_aprendizagem_dic['livros'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Italiano'],
        'nivel_idioma': nivel_idioma_dic['Avançado'],
        'objetivo_aprendizagem': 4,
        'tempo_disponivel': 2,
        'recursos_aprendizagem': recursos_aprendizagem_dic['series'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Alemão'],
        'nivel_idioma': nivel_idioma_dic['Avançado'],
        'objetivo_aprendizagem': 8,
        'tempo_disponivel': 1,
        'recursos_aprendizagem': recursos_aprendizagem_dic['filmes'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Japonês'],
        'nivel_idioma': nivel_idioma_dic['Avançado'],
        'objetivo_aprendizagem': 4,
        'tempo_disponivel': 2,
        'recursos_aprendizagem': recursos_aprendizagem_dic['filmes'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Alemão'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 8,
        'tempo_disponivel': 1.3,
        'recursos_aprendizagem': recursos_aprendizagem_dic['livros'],
        'comunidade': 3.3
    },
    {
        'idioma_alvo': idioma_alvo_dic['Inglês'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 8,
        'tempo_disponivel': 4,
        'recursos_aprendizagem': recursos_aprendizagem_dic['series'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Italiano'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 6,
        'tempo_disponivel': 1.3,
        'recursos_aprendizagem': recursos_aprendizagem_dic['filmes'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Japonês'],
        'nivel_idioma': nivel_idioma_dic['Intermediario'],
        'objetivo_aprendizagem': 6,
        'tempo_disponivel': 4,
        'recursos_aprendizagem': recursos_aprendizagem_dic['filmes'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Espanhol'],
        'nivel_idioma': nivel_idioma_dic['Avançado'],
        'objetivo_aprendizagem': 7,
        'tempo_disponivel': 1.3,
        'recursos_aprendizagem': recursos_aprendizagem_dic['musicas'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Japonês'],
        'nivel_idioma': nivel_idioma_dic['Intermediario'],
        'objetivo_aprendizagem': 4,
        'tempo_disponivel': 4,
        'recursos_aprendizagem': recursos_aprendizagem_dic['series'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Alemão'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 7,
        'tempo_disponivel': 1.3,
        'recursos_aprendizagem': recursos_aprendizagem_dic['musicas'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Japonês'],
        'nivel_idioma': nivel_idioma_dic['Intermediario'],
        'objetivo_aprendizagem': 6,
        'tempo_disponivel': 4,
        'recursos_aprendizagem': recursos_aprendizagem_dic['livros'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Espanhol'],
        'nivel_idioma': nivel_idioma_dic['Avançado'],
        'objetivo_aprendizagem': 7,
        'tempo_disponivel': 1.3,
        'recursos_aprendizagem': recursos_aprendizagem_dic['musicas'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Alemão'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 4.8,
        'tempo_disponivel': 4,
        'recursos_aprendizagem': recursos_aprendizagem_dic['series'],
        'comunidade': comunidade_dic['professores']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Alemão'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 5,
        'tempo_disponivel': 1.3,
        'recursos_aprendizagem': recursos_aprendizagem_dic['livros'],
        'comunidade': comunidade_dic['professores']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Japonês'],
        'nivel_idioma': nivel_idioma_dic['Avançado'],
        'objetivo_aprendizagem': 5,
        'tempo_disponivel': 4,
        'recursos_aprendizagem': recursos_aprendizagem_dic['series'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Espanhol'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 7,
        'tempo_disponivel': 1.3,
        'recursos_aprendizagem': recursos_aprendizagem_dic['musicas'],
        'comunidade': 4.2
    },
    {
        'idioma_alvo': idioma_alvo_dic['Francês'],
        'nivel_idioma': nivel_idioma_dic['Intermediario'],
        'objetivo_aprendizagem': 4,
        'tempo_disponivel': 4,
        'recursos_aprendizagem': recursos_aprendizagem_dic['series'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Espanhol'],
        'nivel_idioma': nivel_idioma_dic['Avançado'],
        'objetivo_aprendizagem': 7,
        'tempo_disponivel': 1.3,
        'recursos_aprendizagem': recursos_aprendizagem_dic['musicas'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Francês'],
        'nivel_idioma': nivel_idioma_dic['Intermediario'],
        'objetivo_aprendizagem': 6,
        'tempo_disponivel': 4,
        'recursos_aprendizagem': recursos_aprendizagem_dic['series'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Espanhol'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 7,
        'tempo_disponivel': 1.3,
        'recursos_aprendizagem': recursos_aprendizagem_dic['musicas'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Francês'],
        'nivel_idioma': nivel_idioma_dic['Intermediario'],
        'objetivo_aprendizagem': 3,
        'tempo_disponivel': 4,
        'recursos_aprendizagem': recursos_aprendizagem_dic['series'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Inglês'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 3,
        'tempo_disponivel': 1.3,
        'recursos_aprendizagem': recursos_aprendizagem_dic['livros'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Japonês'],
        'nivel_idioma': nivel_idioma_dic['Intermediario'],
        'objetivo_aprendizagem': 4,
        'tempo_disponivel': 4,
        'recursos_aprendizagem': recursos_aprendizagem_dic['series'],
        'comunidade': comunidade_dic['professores']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Espanhol'],
        'nivel_idioma': nivel_idioma_dic['Iniciante'],
        'objetivo_aprendizagem': 5.5,
        'tempo_disponivel': 1.3,
        'recursos_aprendizagem': recursos_aprendizagem_dic['musicas'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Japonês'],
        'nivel_idioma': nivel_idioma_dic['Intermediario'],
        'objetivo_aprendizagem': 2,
        'tempo_disponivel': 4,
        'recursos_aprendizagem': recursos_aprendizagem_dic['series'],
        'comunidade': comunidade_dic['acadêmicos']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Inglês'],
        'nivel_idioma': nivel_idioma_dic['Avançado'],
        'objetivo_aprendizagem': 3,
        'tempo_disponivel': 1.3,
        'recursos_aprendizagem': recursos_aprendizagem_dic['musicas'],
        'comunidade': comunidade_dic['funcionários']
    },
    {
        'idioma_alvo': idioma_alvo_dic['Francês'],
        'nivel_idioma': nivel_idioma_dic['Avançado'],
        'objetivo_aprendizagem': 8,
        'tempo_disponivel': 4,
        'recursos_aprendizagem': recursos_aprendizagem_dic['series'],
        'comunidade': comunidade_dic['acadêmicos']
    }

]

# caso de entrada como um dicionário com valores para os mesmos atributos que os casos registrados na base
caso_entrada = {
    'idioma_alvo': idioma_alvo_dic['Inglês'],
    'nivel_idioma': nivel_idioma_dic['Avançado'],
    'objetivo_aprendizagem': 8,
    'tempo_disponivel': 2,
    'recursos_aprendizagem': recursos_aprendizagem_dic['filmes'],
    'comunidade': comunidade_dic['acadêmicos']
}

# Calcula a similaridade entre o caso de entrada e cada caso na base usando a fórmula de distancia euclidiana pros atributos numéricos e a igualdade pros atributos categóricos.
# É ponderada pelos pesos e é armazenada em uma lista de tuplas contendo o caso de base e similaridade calculada
similaridades = []
for case in base_casos:
    similaridade = 0
    for atributo, peso in atributos.items():
        if atributo in ['recursos_aprendizagem', 'tipo_linguagem', 'idioma_alvo', 'comunidade'] :
            # Para atributos categóricos, use o dicionário para mapear os rótulos de texto para valores numéricos
            similaridade += peso * (caso_entrada[atributo] == case[atributo])
        else:
            similaridade += peso * (caso_entrada[atributo] - case[atributo])**2
    similaridades.append((case, similaridade))

# Ordenando os casos por similaridade e calcula a similaridade percentual pra cada caso, em relação ao total de similaridade da lista
similaridades.sort(key=lambda x: x[1], reverse=True)

# Recupera o caso mais similar e vai imprimir como uma recomendação pro caso de entrada ou o caso mais próximo em similaridade
caso_recomendado = similaridades[0][0]

