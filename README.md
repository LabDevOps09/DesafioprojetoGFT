# 1️⃣ Desafio Classificador de nível de Herói

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões

## Objetivo

Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

Se XP for menor do que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 5.001 e 7.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000= Imortal
Se XP for maior ou igual a 10.001 = Radiante

## Saída

Ao final deve se exibir uma mensagem:
"O Herói de nome **{nome}** está no nível de **{nivel}**"

 
 
 
Bons estudos 😉


### 📝 Etapas do Código

#### Entrada de Dados:
- Utilizamos `input()` para capturar o **nome** e a **quantidade de XP** do herói.
- A quantidade de experiência (`xp_heroi`) é convertida para inteiro usando `int()`, pois vamos compará-la em condições numéricas.

#### 🔍 Estrutura de Decisão (`if-elif-else`):
- A estrutura `if-elif-else` define o **nível do herói** de acordo com a faixa de experiência (XP).
- Cada faixa de valores de XP tem uma condição específica:
  - `if xp_heroi < 1000:` atribui o nível "Ferro".
  - `elif 1001 <= xp_heroi <= 2000:` atribui o nível "Bronze".
  - E assim por diante, até o nível mais alto, "Radiante", para o caso em que `xp_heroi` seja **10.001 ou mais**. 🥇
- A variável `nivel` é atualizada conforme a condição que for verdadeira.

# 2️⃣  Desafio Calculadora de partidas Rankeadas
**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
- Funções

## Objetivo:

Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 20 = Bronze
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 80 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100= Lendário
Se vitórias for maior ou igual a 101 = Imortal

## Saída

Ao final deve se exibir uma mensagem:
"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"


 # 📝 Explicação do Código

## 📊 Função `calcular_saldo(vitorias, derrotas)`

Esta função recebe a quantidade de vitórias 🏆 e derrotas 💔, calcula o saldo (vitórias - derrotas) e determina o nível com base na quantidade de vitórias. O saldo e o nível são retornados.

## 🔄 Função `main()`

É a função principal que executa o programa. Ela utiliza um laço de repetição `while` para garantir que o usuário insira valores válidos para vitórias e derrotas. Em caso de erro ❌ (como a inserção de um valor não inteiro), uma mensagem de erro é exibida e o usuário é solicitado a tentar novamente.

## 🔍 Estruturas de Decisão

Dentro da função `calcular_saldo`, utilizamos uma série de `if` e `elif` para determinar o nível com base na quantidade de vitórias. 🥇

## ⌨️ Entrada e Saída

A função `input()` coleta as informações do usuário, e `print()` exibe a mensagem final, mostrando o saldo e o nível do jogador. 🎮

## 🎉 Funcionamento do Programa

O programa pedirá para que o usuário insira a quantidade de vitórias e derrotas, e então exibirá o saldo e o nível correspondente. 🚀


#### Saída de Dados:
- Ao final, a função `print()` exibe a mensagem formatada com o nome e o nível do herói, usando uma **f-string** para substituir `{nome_heroi}` e `{nivel}` diretamente no texto.

#### Resultado:
- O programa é flexível e funciona para qualquer valor de XP informado pelo usuário, exibindo sempre a categoria correta de nível.

# 3️⃣ Desafio Escrevendo as classes de um Jogo

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
- Funções
- Classes e Objetos

## Objetivo:

Crie uma classe generica que represente um herói de uma aventura e que possua as seguintes propriedades:

- nome
- idade
- tipo (ex: guerreiro, mago, monge, ninja )

além disso, deve ter um método chamado atacar que deve atender os seguientes requisitos:

- exibir a mensagem: "o {tipo} atacou usando {ataque}")
- aonde o {tipo} deve ser concatenando o tipo que está na propriedade da classe
- e no {ataque} deve seguir uma descrição diferente conforme o tipo, seguindo a tabela abaixo:

se mago -> no ataque exibir (usou magia)
se guerreiro -> no ataque exibir (usou espada)
se monge -> no ataque exibir (usou artes marciais)
se ninja -> no ataque exibir (usou shuriken)

## Saída

Ao final deve se exibir uma mensagem:

- "o {tipo} atacou usando {ataque}"
  ex: mago atacou usando magia
  guerreiro atacou usando espada

  ## 📝 Explicação do Código

### 🔧 Construtor (`__init__`):
- Recebe `nome`, `idade` e `tipo` e define essas propriedades para cada instância do herói.

### ⚔️ Método `atacar`:
- Define um dicionário `ataques` que mapeia cada tipo de herói para uma descrição de ataque específica. Em seguida:
  - 🧩 **Busca a descrição do ataque** com base no `tipo` do herói usando o método `get`.
  - 📢 **Exibe a mensagem** formatada com o tipo e o ataque, conforme especificado.

### 💡 Exemplos de uso:
- Criamos instâncias para quatro heróis com tipos diferentes e chamamos o método `atacar` para cada um.

---

### 🖥️ Saída Esperada
Ao rodar este código, você verá:

```python
O mago atacou usando magia
O guerreiro atacou usando espada
O monge atacou usando artes marciais
O ninja atacou usando shuriken

 
