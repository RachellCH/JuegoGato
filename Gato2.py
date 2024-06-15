import random

def print_welcome_message():
    print("¡Bienvenido al juego del GATO!")

def print_menu():
    print("\nMenú:")
    print("1. Nueva partida (Player 1 VS COM)")
    print("2. Versus (P1 VS P2)")
    print("3. Salir")

def create_board():
    return [' '] * 9

def print_board(board):
    print("\n")
    for i in range(3):
        print(' | '.join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("--+---+--")
    print("\n")

def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def check_draw(board):
    return ' ' not in board

def get_player_move(board, player):
    move = -1
    while move not in range(1, 10) or board[move - 1] != ' ':
        try:
            move = int(input(f"Jugador {player}, elige una posición (1-9): "))
        except ValueError:
            print("Entrada inválida. Por favor elige un número entre 1 y 9.")
    return move - 1

def get_computer_move(board):
    return random.choice([i for i, spot in enumerate(board) if spot == ' '])

def play_game(player1, player2, vs_com=False):
    board = create_board()
    current_player = player1

    while True:
        print_board(board)
        if vs_com and current_player == player2:
            move = get_computer_move(board)
            print(f"Computadora elige posición {move + 1}")
        else:
            move = get_player_move(board, current_player)
        
        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"¡Jugador {current_player} ha ganado!")
            break

        if check_draw(board):
            print_board(board)
            print("¡Es un empate!")
            break

        current_player = player2 if current_player == player1 else player1

def main():
    print_welcome_message()

    while True:
        print_menu()
        choice = input("Elige una opción (1-3): ")

        if choice == '1':
            play_game('X', 'O', vs_com=True)
        elif choice == '2':
            play_game('X', 'O')
        elif choice == '3':
            print("¡Gracias por jugar! ¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, eliga de nuevo.")

if __name__ == "__main__":
    main()
