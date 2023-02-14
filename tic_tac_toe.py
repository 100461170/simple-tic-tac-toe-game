
game = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def print_table(game:dict):
    """This function prints table"""

    valores = list(game.values())
    print("",valores[0], "|",valores[1], "|", valores[2], sep="    ")
    print("-------------------------------")
    print("",valores[3], "|",valores[4], "|",valores[5], sep="    ")
    print("-------------------------------")
    print("",valores[6], "|",valores[7], "|",valores[8], sep="    ")
    print("\n\n")
    return None

def run(game:dict)-> None:
    """This function runs the game"""
    contador = 0
    a = check_win(game)
    valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while a == 0 and contador < 9:
        print_table(game)
        player1 = -1
        player2 = -1
        while player1 not in valores:
            player1 = int(input("Choose a valid square Player 1: "))

        player1 = str(player1)
        game[player1] = "X"
        contador += 1
        print_table(game)
        a = check_win(game)

        if a != 0:
            print("El jugador 1 gano!!!")
            return 1
        if contador == 9:
            print("nadie gano empate")

        while player2 not in valores:
            player2 = int(input("Choose a valid square Player 2: "))

        player2 = str(player2)
        game[player2] = "O"
        print_table(game)
        a = check_win(game)
        if a != 0:
            print("El jugador 2 gano!!!")
        contador += 1


def check_win(game:dict)-> int:
    valores = list(game.values())
    retorno = 0
    # comprobaciones jugador 1
    if valores[0] == "X" and valores[1] == "X" and valores[2] == "X":
        retorno = 1
    if valores[3] == "X" and valores[4] == "X" and valores[5] == "X":
        retorno = 1
    if valores[6] == "X" and valores[7] == "X" and valores[8] == "X":
        retorno = 1
    if valores[0] == "X" and valores[3] == "X" and valores[6] == "X":
        retorno = 1
    if valores[1] == "X" and valores[4] == "X" and valores[7] == "X":
        retorno = 1
    if valores[2] == "X" and valores[5] == "X" and valores[8] == "X":
        retorno = 1
    if valores[0] == "X" and valores[4] == "X" and valores[8] == "X":
        retorno = 1
    if valores[2] == "X" and valores[4] == "X" and valores[6] == "X":
        retorno = 1
    # condiciones ganar jugador 2
    if valores[0] == "O" and valores[1] == "O" and valores[2] == "O":
        retorno = 2
    if valores[3] == "O" and valores[4] == "O" and valores[5] == "O":
        retorno = 2
    if valores[6] == "O" and valores[7] == "O" and valores[8] == "O":
        retorno = 2
    if valores[0] == "O" and valores[3] == "O" and valores[6] == "O":
        retorno = 2
    if valores[1] == "O" and valores[4] == "O" and valores[7] == "O":
        retorno = 2
    if valores[2] == "O" and valores[5] == "O" and valores[8] == "O":
        retorno = 2
    if valores[0] == "O" and valores[4] == "O" and valores[8] == "O":
        retorno = 2
    if valores[2] == "O" and valores[4] == "O" and valores[6] == "O":
        retorno = 2
    return retorno




