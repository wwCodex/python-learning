import random 

SIZE = 5
MINES = 5


def create_board():
    board = []

    for i in range(SIZE):
        row = []

        for j in range(SIZE):
            row.append(".")

        board.append(row)

    return board


def place_mines(board):

    mines = 0

    while mines < MINES:

        row = random.randint(0, SIZE - 1)
        col = random.randint(0, SIZE - 1)

        if board[row][col] != "M":
            board[row][col] = "M"
            mines += 1


def print_board(board, revealed):

    print()

    print("   1 2 3 4 5")

    for i in range(SIZE):

        print(i + 1, end="  ")

        for j in range(SIZE):

            if revealed[i][j]:
                print(board[i][j], end=" ")

            else:
                print(".", end=" ")

        print()


def count_mines(board, row, col):

    count = 0

    for i in range(row - 1, row + 2):

        for j in range(col - 1, col + 2):

            if 0 <= i < SIZE and 0 <= j < SIZE:

                if board[i][j] == "M":
                    count += 1

    return count

board = create_board()

place_mines(board)

revealed = create_board()

for i in range(SIZE):
    for j in range(SIZE):
        revealed[i][j] = False

safe_cells = SIZE * SIZE - MINES
revealed_safe = 0

print("""
===========================
      MINESWEEPER
===========================
""")

while True:

    print_board(board, revealed)

    row = int(input("\nEnter Row (1-5): ")) - 1
    col = int(input("Enter Column (1-5): ")) - 1

    if revealed[row][col]:
        print("Already revealed!")
        continue

    revealed[row][col] = True

    if board[row][col] == "M":

        print("\nBOOM!")

        for i in range(SIZE):
            for j in range(SIZE):
                revealed[i][j] = True

        print_board(board, revealed)

        print("\nGAME OVER!")

        break

    mines = count_mines(board, row, col)

    board[row][col] = str(mines)

    revealed_safe += 1

    if revealed_safe == safe_cells:

        print_board(board, revealed)

        print("\nYOU WIN!")

        break