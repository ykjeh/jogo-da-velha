import time


def tabuleiro(elemento: list) -> None:
    print()
    print(f"{elemento[0]} | {elemento[1]} | {elemento[2]}")
    print(f"{elemento[3]} | {elemento[4]} | {elemento[5]}")
    print(f"{elemento[6]} | {elemento[7]} | {elemento[8]}")


print("Pressiona ENTER para começar.")

input()

print("Carregando...")

time.sleep(1)

def nomear_jogador(simbolo: str, numero: int) -> str:
    while True:
        print(f"\nJogador {numero}({simbolo}), digite seu nome: ")
        nome_jogador = input().title()
        if nome_jogador != "":
            return nome_jogador
        
        print("Nome inválido, digite novamente.")

jogador1 = nomear_jogador("Circulo", 1)
jogador2 = nomear_jogador("X", 2)

print("\nComo Jogar: ")
print("Cada casa do jogo da velha tem um número associado. Veja a ilustração")

tabuleiro([numbers for numbers in range(1, 10)])
print("\nPara ganhar, é preciso 3 símbolos consecutivos.\n")

time.sleep(3)

print(f"{jogador1}(O) vs {jogador2}(x)!")

def checar_vitoria(elemento: list) -> bool:
    combinacoes_vencedoras = [
        # Horizontais
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        # Verticais
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        # Diagonais
        [0, 4, 8],
        [2, 4, 6]
    ]

    for a, b, c in combinacoes_vencedoras:
        if elemento[a] == elemento[b] == elemento[c] and elemento[a] != " ":
            return True
    return False
        
    for i in range(len(elemento) - 6):
        if (elemento[i] == elemento[i + 3] == elemento[i + 6] or elemento[i - 3] == elemento[i] == elemento[i + 3] or
                elemento[i - 6] == elemento[i - 3] == elemento[i]) and elemento[i] != " ":
            return True
        
    if elemento[0] == elemento[4] == elemento[8] != " ":
        return True
    
    if elemento[2] == elemento[4] == elemento[6] != " ":
        return True
    
    return False

def checar_empate(elemento: list) -> bool:
    return " " not in elemento


def rodada(elemento: list, num_jogador: int, num_rodada, jogador: str) -> None:
    simbolo = "O" if num_jogador == 1 else "X"

    tabuleiro(elemento)
    print(f"Rodada {num_rodada}! {jogador}, digite o número da casa que deseja jogar: ")

    jogada = int(input())

    if jogada in range(1, 10):
        if elemento[jogada - 1] == " ":
            elemento[jogada - 1] = simbolo
        else:
            print("Casa ocupada, tente novamente")


            rodada(elemento, num_jogador, num_rodada, jogador)

    else:
        print("Jogada inválida, tente novamente.")

        rodada(elemento, num_jogador, num_rodada, jogador)

elemento_do_jogo = [" "] * 9

for num_rodada_atual in range(1, 10):
    contador_jogador = num_rodada_atual - 1
    num_jogador_atual = not (contador_jogador % 2)
    jogador_atual = jogador1 if num_jogador_atual == 1 else jogador2

    rodada(elemento_do_jogo, num_jogador_atual, num_rodada_atual, jogador_atual)
    if checar_vitoria(elemento_do_jogo):
        tabuleiro(elemento_do_jogo)
        print(f"{jogador_atual} venceu! Parabéns você venceu na {num_rodada_atual} rodada!")
        time.sleep(2)
        break

    if checar_empate(elemento_do_jogo):
        print("Empate!")
        break

    time.sleep(0.5)


print("O jogo acabou.")
