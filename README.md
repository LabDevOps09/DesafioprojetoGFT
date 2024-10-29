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


### Etapas do Código

#### Entrada de Dados:
- Utilizamos `input()` para capturar o **nome** e a **quantidade de XP** do herói.
- A quantidade de experiência (`xp_heroi`) é convertida para inteiro usando `int()`, pois vamos compará-la em condições numéricas.

#### Estrutura de Decisão (`if-elif-else`):
- A estrutura `if-elif-else` define o **nível do herói** de acordo com a faixa de experiência (XP).
- Cada faixa de valores de XP tem uma condição específica:
  - `if xp_heroi < 1000:` atribui o nível "Ferro".
  - `elif 1001 <= xp_heroi <= 2000:` atribui o nível "Bronze".
  - E assim por diante, até o nível mais alto, "Radiante", para o caso em que `xp_heroi` seja **10.001 ou mais**.
- A variável `nivel` é atualizada conforme a condição que for verdadeira.

#### Saída de Dados:
- Ao final, a função `print()` exibe a mensagem formatada com o nome e o nível do herói, usando uma **f-string** para substituir `{nome_heroi}` e `{nivel}` diretamente no texto.

#### Resultado:
- O programa é flexível e funciona para qualquer valor de XP informado pelo usuário, exibindo sempre a categoria correta de nível.
