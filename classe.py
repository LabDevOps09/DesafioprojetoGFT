class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        # Dicionário para mapear cada tipo de herói a uma descrição de ataque
        ataques = {
            "mago": "magia",
            "guerreiro": "espada",
            "monge": "artes marciais",
            "ninja": "shuriken"
        }
        
        # Obtém o ataque específico com base no tipo do herói
        ataque = ataques.get(self.tipo, "ataque desconhecido")
        
        # Exibe a mensagem de ataque
        print(f"O {self.tipo} atacou usando {ataque}")

# Exemplo de criação de heróis e uso do método atacar
heroi1 = Heroi("Gandalf", 150, "mago")
heroi2 = Heroi("Conan", 30, "guerreiro")
heroi3 = Heroi("Bruce", 35, "monge")
heroi4 = Heroi("Ryu", 28, "ninja")

# Chamando o método atacar para cada herói
heroi1.atacar()  # Saída: O mago atacou usando magia
heroi2.atacar()  # Saída: O guerreiro atacou usando espada
heroi3.atacar()  # Saída: O monge atacou usando artes marciais
heroi4.atacar()  # Saída: O ninja atacou usando shuriken
