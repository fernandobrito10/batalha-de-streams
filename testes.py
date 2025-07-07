import random
from views import get_views

musicas = {
    "wXTJBr9tt8Q": "The Beatles - Yesterday",
    "5tc0gLSSU1M": "The Beatles - And I Love Her",
    "2Q_ZzBGPdqE": "The Beatles - Help!",
    "UelDrZ1aFeY": "The Beatles - Something",
    "6ZwNO_zAqOo": "The Beatles - Drive My Car"
}

ids = list(musicas.keys())

musica1_id = random.choice(ids)
ids.remove(musica1_id)
musica2_id = random.choice(ids)

views1 = int(get_views(musica1_id))
views2 = int(get_views(musica2_id))

print(f"Qual música tem mais visualizações?")
print(f"1: {musicas[musica1_id]}")
print(f"2: {musicas[musica2_id]}")

escolha = int(input("Digite 1 ou 2: "))

if (views1 > views2 and escolha == 1) or (views2 > views1 and escolha == 2):
    print("Você acertou!")
else:
    print("Você errou...")

print(f"{musicas[musica1_id]}: {views1} views")
print(f"{musicas[musica2_id]}: {views2} views")
