from casos import *

# Calcula a similaridade entre o caso de entrada e cada caso na base usando a fórmula de distância euclidiana
# para os atributos numéricos e a igualdade pros atributos categóricos.
# É ponderada pelos pesos, sendo armazenada em uma lista de tuplas contendo o caso de base e similaridade calculada

# Calculando as similaridades calculamos a diferença entre o valor do caso da base e o valor do caso de entrada,
# elevamos ao quadrado e multiplicamos pelo peso do atributo. Somamos essas contribuições de todos os atributos
# para obter a similaridade total entre os casos.

def calc_similaridades(caso_entrada, atributos):
    similaridades = []
    for caso in base_casos:
        similaridade = 0.0
        for atributo, peso in atributos.items():
            valor_caso = caso[atributo]
            valor_entrada = caso_entrada[atributo]
            similaridade += peso * (valor_caso - valor_entrada) ** 2
        similaridades.append(similaridade)  # Armazenamos as similaridades em uma lista.

    # Obtendo os casos recomendados com percentual de similaridade em uma escala de 0 a 100. Para isso,
    # subtraímos cada similaridade do valor máximo de similaridade encontrado na lista de similaridades,
    # multiplicamos por 100 e subtraímos o resultado de 100. Dessa forma, obtemos o percentual de similaridade,
    # onde 100 indica uma correspondência perfeita e 0 indica nenhuma similaridade.
    casos_recomendados = []
    for i, similaridade in enumerate(similaridades):
        caso = base_casos[i]
        percentual_similaridade = (1 - (similaridade / max(similaridades))) * 100
        casos_recomendados.append((caso,
                                   percentual_similaridade))  # Criamos uma lista de casos recomendados, que combina
        # Cada caso da base com seu respectivo percentual de similaridade.

    # Ordenando os casos recomendados pelo maior percentual de similaridade
    casos_recomendados = sorted(casos_recomendados, key=lambda x: x[1],
                                reverse=True)  # utilizada para que os casos mais similares estejam no início da lista
    caso_recomendado = casos_recomendados[0][0]

    return (similaridades, caso_recomendado, casos_recomendados)
