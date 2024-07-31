import sys
import stdio

def create_board(rows, cols):
    # Initialize the game board with empty cells
    return [[" " for _ in range(cols)] for _ in range(rows)]

def is_valid_position(board, row, col):
    # Check if the given position is within the bounds of the board
    return 0 <= row < len(board) and 0 <= col < len(board[0])

def print_board(board):
    # Print the current state of the game board with borders resembling a board game
    num_cols = len(board[0])
    num_rows = len(board)
    col_labels = "".join(f"{i:<3}" for i in range(num_cols))
    border_line = "+--" * num_cols + "+"

    stdio.write("    " + col_labels + "\n")
    stdio.write("  "+ border_line + "\n")

    max_lengths = [max(len(str(board[row][col])) for row in range(num_rows)) for col in range(num_cols)]

    for i in range(num_rows - 1, -1, -1):  
        row_data = board[i]
        row_string = "| " + "| ".join(cell.center(max_lengths[col]) if cell != " " else " " * max_lengths[col] for col, cell in enumerate(row_data)) + "|"
        stdio.write(f"{i} {row_string}\n")  
        stdio.write("  "+border_line + "\n")



def process_setup_input(board, input_str):
    # Process the setup input provided by the user and update the game board accordingly
    parts = input_str.split()
    if len(parts) < 4:
        stdio.write("ERROR: Invalid input format")
        return False

    object_type = parts[0]
    if object_type not in ['s', 'x', 'd', 'l']:
        stdio.write(f"ERROR: Invalid object type {object_type}")
        return False

    # Process different types of objects (pieces, sinks, blocked fields)
    if object_type == 'x':
        # Process blocked fields
        if len(parts) != 4:
            stdio.write("ERROR: Invalid input format for blocked field")
            return False
        row, col = int(parts[1]), int(parts[2])
        if not is_valid_position(board, row, col):
            stdio.write(f"ERROR: Field {row} {col} not on board")
            return False
        board[row][col] = 'x'
    elif object_type == 's':
        # Process sink fields
        if len(parts) != 4:
            stdio.write("ERROR: Invalid input format for sink")
            return False
        size, row, col = int(parts[1]), int(parts[2]), int(parts[3])
        if size not in [1, 2]:
            stdio.write(f"ERROR: Invalid piece type {size}")
            return False
        if not is_valid_position(board, row, col):
            stdio.write(f"ERROR: Field {row} {col} not on board")
            return False
        place_sink(board, row, col, size)
    else:
        # Process playing pieces
        if len(parts) != 4:
            stdio.write("ERROR: Invalid input format for piece")
            return False
        piece_type, row, col = parts[1], int(parts[2]), int(parts[3])
        if not is_valid_position(board, row, col):
            stdio.write(f"ERROR: Field {row} {col} not on board")
            return False
        if not is_empty(board, row, col):
            stdio.write(f"ERROR: Field {row} {col} not free")
            return False
        board[row][col] = piece_type.upper() if object_type == 'd' else piece_type.lower()

    return True

def is_empty(board, row, col):
    # Check if the specified position on the board is empty
    return board[row][col] == " "

def place_sink(board, row, col, size):
    # Place a sink on the board at the specified position with the given size
    for i in range(row, row + size):
        for j in range(col, col + size):
            board[i][j] = 's'

def check_win_condition(board):
    dark_sinks = 0
    light_sinks = 0
    for row in board:
        for cell in row:
            if cell == 'S':
                dark_sinks += 1
            elif cell == 's':
                light_sinks += 1
    return dark_sinks >= 4 or light_sinks >= 4

def perform_move(board, row, col, piece_type):
    if is_valid_position(board, row, col):
        if is_empty(board, row, col):
            board[row][col] = piece_type
            return True
        else:
            stdio.write(f"ERROR: Invalid move. Position ({row}, {col}) is not empty.\n")
            return False
    else:
        stdio.write(f"ERROR: Invalid move. Position ({row}, {col}) is not on the board.\n")
        return False

def main():
    # Check if the command line arguments are provided correctly
    if len(sys.argv) > 4:
        stdio.write("ERROR: Too many arguments")
        return

    if len(sys.argv) != 4:
        stdio.write("ERROR: Too few arguments")
        return

    try:
        rows = int(sys.argv[1])
        cols = int(sys.argv[2])
        gui_mode = int(sys.argv[3])
    except ValueError:
        stdio.write("ERROR: Illegal argument")
        return

    if not (8 <= rows <= 10 and 8 <= cols <= 18 and gui_mode in [0, 1]):
        stdio.write("ERROR: Illegal argument")
        return

    board = create_board(rows, cols)

    stdio.write("Initial Board:\n")
    print_board(board)

    
    while True:
        # Process board setup input
        stdio.write("Enter setup input (type '#' to finish setup):")
        setup_input = stdio.readLine()
        if setup_input == "#":
            break
        try:
            process_setup_input(board, setup_input)
        except ValueError as e:
            stdio.write(f"ERROR: {str(e)}")
            return

        print_board(board)

    # Perform moves
    current_player = "light"  # Start with Light player
    while True:
        move_count = 0  # Track the number of moves made in each turn
        while move_count < 2:  # Each player must make two moves per turn
            stdio.write("Enter moves (type '#' to finish moves):")
            move_input = stdio.readLine()
          
            if move_input == "#":
                break

            move_parts = move_input.split()
            # print(len(move_parts))
            if len(move_parts) != 3:
                stdio.write("ERROR: Invalid move format. Please enter in the format 'row column piece_type'.\n")
                continue

            try:
                row = int(move_parts[0])
                col = int(move_parts[1])
                piece_type = move_parts[2]
            except ValueError:
                stdio.write("ERROR: Invalid move format. Row and column must be integers.\n")
                continue

            # Check if the selected position for the move is empty
            if not is_valid_position(board, 9 - row, col):
                stdio.write(f"ERROR: Invalid move. Position ({row}, {col}) is out of bounds.\n")
                continue
            elif not is_empty(board, 9 - row, col):
                stdio.write(f"ERROR: Invalid move. Position ({row}, {col}) is not empty.\n")
                continue

            # Perform the move
            if not perform_move(board, row, col, piece_type):
                continue

            stdio.write(f"Move by {current_player} player at ({row}, {col})\n")
        

            move_count += 1  # Increment move count

            # Check win condition after each turn
            if check_win_condition(board):
                stdio.write(f"{current_player.capitalize()} player wins!\n")
                return

            # Switch to the other player for the next turn
            current_player = "dark" if current_player == "light" else "light"

if __name__ == "__main__":
    main()
