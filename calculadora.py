def calcular_saldo(vitorias, derrotas):
    # Calcula o saldo de vitórias
    saldo_vitorias = vitorias - derrotas
    
    # Determina o nível com base nas vitórias
    if vitorias < 10:
        nivel = "Ferro"
    elif 10 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:  # vitorias >= 101
        nivel = "Imortal"

    return saldo_vitorias, nivel

def main():
    while True:
        try:
            vitorias = int(input("Digite a quantidade de vitórias: "))
            derrotas = int(input("Digite a quantidade de derrotas: "))
            break  # Sai do laço se os inputs forem válidos
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    saldo_vitorias, nivel = calcular_saldo(vitorias, derrotas)
    
    print(f"O Herói tem de saldo de {saldo_vitorias} está no nível de {nivel}")

# Executa o programa
if __name__ == "__main__":
    main()
