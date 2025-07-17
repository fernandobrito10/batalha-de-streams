from musicas import get_info_musicas
from views import get_views
import json

# Função para criar o json de cada artista (hard)

def criar_json(lista_musicas, nome_artista):
    musicas_json = []
    for musica in lista_musicas:
        info_musica = get_info_musicas(musica)
        musicas_json.append(info_musica)
    with open (f"{nome_artista}.json", "w", encoding="utf-8") as outfile:
        json.dump(musicas_json, outfile, ensure_ascii=False, indent=4)
    print(f"{nome_artista}.json criado com sucesso!")

with open("top15queen.txt", "r", encoding="utf-8") as arquivo:
    lista_beatles = [linha.strip() for linha in arquivo]

criar_json(lista_beatles, "Queen")