# Solicita o nome e a quantidade de experiência do herói
nome_heroi = input("Digite o nome do herói: ")
xp_heroi = int(input("Digite a quantidade de experiência (XP) do herói: "))

# Estrutura de decisão para classificar o herói de acordo com o nível de XP
if xp_heroi < 1000:
    nivel = "Ferro"
elif 1001 <= xp_heroi <= 2000:
    nivel = "Bronze"
elif 2001 <= xp_heroi <= 5000:
    nivel = "Prata"
elif 5001 <= xp_heroi <= 7000:
    nivel = "Ouro"
elif 7001 <= xp_heroi <= 8000:
    nivel = "Platina"
elif 8001 <= xp_heroi <= 9000:
    nivel = "Ascendente"
elif 9001 <= xp_heroi <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

# Exibe a mensagem com o nome e o nível do herói
print(f"O Herói de nome {nome_heroi} está no nível de {nivel}")