from casos import *

# Calcula a similaridade entre o caso de entrada e cada caso na base usando a fórmula de distância euclidiana
# para os atributos numéricos e a igualdade pros atributos categóricos.
# É ponderada pelos pesos, sendo armazenada em uma lista de tuplas contendo o caso de base e similaridade calculada
similaridades = []
for case in base_casos:
    similaridade = 0
    for atributo, peso in atributos.items():
        if atributo in ['recursos_aprendizagem', 'tipo_linguagem', 'idioma_alvo', 'comunidade']:
            # Para atributos categóricos, use o dicionário para mapear os rótulos de texto para valores numéricos
            similaridade += peso * (caso_entrada[atributo] == case[atributo])
        else:
            similaridade += peso * (caso_entrada[atributo] - case[atributo])**2
    similaridades.append((case, similaridade))

# Ordenando os casos por similaridade e calcula a similaridade percentual para cada caso,
# em relação ao total de similaridade da lista
similaridades.sort(key=lambda x: x[1], reverse=True)

# Recupera o caso mais similar e vai imprimir como uma recomendação pro caso de entrada
# ou o caso mais próximo em similaridade
caso_recomendado = similaridades[0][0]
