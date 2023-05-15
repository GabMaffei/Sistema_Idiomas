# Press the green button in the gutter to run the script.
from casos import *

if __name__ == '__main__':
    # Saída
    print('Caso de entrada :')
    print(caso_entrada)
    print('Pesos:')
    print(atributos)
    print('Caso recomendado:')
    print(caso_recomendado)
    print('Casos base ordenados por similaridade:')
    # for case, similaridade in similaridades:
    #    print(case)
    #    print('Similaridade:', similaridade)
    # calculate similarity percentage for each case
    total_similaridade = sum([sim[1] for sim in similaridades])
    for sim in similaridades:
        case = sim[0]
        similaridade = sim[1]
        similaridade_percentual = round((similaridade / total_similaridade) * 100, 2)
        print(f"{case}, similaridade: {similaridade_percentual}%")
    # A saída das similaridades é apresentada em ordem decrescente de similaridade. Em seguida, a
    # similaridade é convertida em um percentual de similaridade em relação ao total da similaridade
    # para cada caso. Finalmente, é exibido cada caso da base de casos, com seu percentual de
    # similaridade em relação ao caso de entrada.