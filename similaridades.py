from casos import *

# Calcula a similaridade entre o caso de entrada e cada caso na base usando a fórmula de distância euclidiana
# para os atributos numéricos e a igualdade pros atributos categóricos.
# É ponderada pelos pesos, sendo armazenada em uma lista de tuplas contendo o caso de base e similaridade calculada


def calc_similaridades(caso_entrada):
    similaridades = []
    for case in base_casos:
        similaridade = 0 # para acumular o valor da similaridade entre os casos.
        for atributo, peso in atributos.items(): #O loop percorre cada atributo definido na variável atributos, juntamente com o seu peso correspondente.
            if atributo in ['idioma_alvo', 'nivel_idioma', 'recursos_aprendizagem', 'comunidade']:
                # Para atributos categóricos, usa o dicionário para mapear os rótulos de texto para valores numéricos
                similaridade += peso * (caso_entrada[atributo] == case[atributo]) #calculada como 0 se os valores dos atributos forem diferentes e 1 se forem iguais
            else:
                # Atributos numéricos
                similaridade += peso * (caso_entrada[atributo] - case[atributo])**2 #A diferença entre os valores dos atributos é elevada ao quadrado e multiplicada pelo peso correspondente.
        similaridades.append((case, similaridade))#O resultado da similaridade de cada atributo é acumulado na variável similaridade.
        # Após percorrer todos os atributos, a similaridade total entre os casos é obtida

    # Ordenando os casos por similaridade por ordem decrescente
    similaridades.sort(key=lambda x: x[1], reverse=True)

    # Recupera o caso mais similar e vai imprimir como uma recomendação pro caso de entrada
    # ou o caso mais próximo em similaridade
    caso_recomendado = similaridades[0][0]

    return (similaridades, caso_recomendado)
