from atributos import *
from entrada import *
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
        'comunidade': comunidade_dic['professores']
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
        'comunidade': comunidade_dic['funcionários']
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
        'comunidade': comunidade_dic['professores']
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



