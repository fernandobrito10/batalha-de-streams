import json
import random
from views import get_views

# Carrega o JSON com as músicas
with open("The_Beatles.json", "r", encoding="utf-8") as file:
    musicas_info = json.load(file)

# Cria um dicionário com {video_id: nome_da_musica}
musicas = {}
for musica in musicas_info:
    video_id = musica.get("idMusica")  # ou a chave correta que você usou no JSON
    nome = musica.get("nomeMusica")  # ou "titulo", dependendo do seu JSON
    if video_id and nome:
        musicas[video_id] = nome

# Seleciona duas músicas aleatórias
ids = list(musicas.keys())
musica1_id = random.choice(ids)
ids.remove(musica1_id)
musica2_id = random.choice(ids)

# Obtém as views
views1 = int(get_views(musica1_id))
views2 = int(get_views(musica2_id))

# Mostra o jogo
print("Qual música tem mais visualizações?")
print(f"1: {musicas[musica1_id]}")
print(f"2: {musicas[musica2_id]}")

escolha = int(input("Digite 1 ou 2: "))

if (views1 > views2 and escolha == 1) or (views2 > views1 and escolha == 2):
    print("Você acertou!")
else:
    print("Você errou...")

print(f"{musicas[musica1_id]}: {views1} views")
print(f"{musicas[musica2_id]}: {views2} views")
