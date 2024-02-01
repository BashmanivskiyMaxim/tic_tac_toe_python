import random


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(
            board[j][i] == player for j in range(3)
        ):
            return True
    if all(board[i][i] == player for i in range(3)) or all(
        board[i][2 - i] == player for i in range(3)
    ):
        return True
    return False


def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)


def get_player_move():
    row = int(input("Введіть номер рядка (0-2): "))
    col = int(input("Введіть номер стовпця (0-2): "))
    return row, col


def get_computer_move(board, difficulty):
    if difficulty == "easy":
        return random.choice(
            [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
        )
    elif difficulty == "hard":
        # Простий алгоритм для визначення кращого ходу
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    if check_winner(board, "O"):
                        board[i][j] = " "
                        return i, j
                    board[i][j] = " "

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    if check_winner(board, "X"):
                        board[i][j] = " "
                        return i, j
                    board[i][j] = " "

        return random.choice(
            [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
        )


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    difficulty = input("Виберіть рівень складності (easy/hard): ")

    while True:
        print_board(board)

        if current_player == "X":
            row, col = get_player_move()
        else:
            row, col = get_computer_move(board, difficulty)

        if board[row][col] != " ":
            print("Ця клітинка вже зайнята. Спробуйте іншу.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} переміг!")
            break

        if is_board_full(board):
            print_board(board)
            print("Гра завершилась у нічию!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
