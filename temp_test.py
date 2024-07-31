import stdio
import sys


# Elements to hold data 
dak_elements = []
light = []
sinks = []
blocked_elements = []


def print_board(rows_board, columns_board, board_data):

    # Display first row to user
    space = "  "
    stdio.write(space)
    
    for iteration, _ in enumerate(range(columns_board)):
        stdio.write(f" {iteration} ")
    newLine= "\n"
    
    stdio.write(newLine)
    # Display top border
    stdio.write(space + "+--" * columns_board + "+ " + newLine)

    # Print each row
    for iteration in range(rows_board - 1, -1, -1):
        # Display left border
        stdio.write(f"{iteration} |")

        # Print each cell
        for inner in range(columns_board):
            if board_data[iteration][inner] == ' ':
                stdio.write("  |")
            else:
                if isinstance(board_data[iteration][inner], str):
                    stdio.write(f" {board_data[iteration][inner]}|")
                elif isinstance(board_data[iteration][inner], int):
                    if len(str(board_data[iteration][inner])) < 2:
                        stdio.write(f" {board_data[iteration][inner]}|")
                    else:
                        stdio.write(f"{board_data[iteration][inner]}|")

        # Display the right border
        stdio.write("\n")
        stdio.write("  " + "+--" * columns_board + "+ \n")   


def game_board_print(rows_board, columns_board, board_data):

    # Check For Any Moves In File
    try:
        while True:
            line_input = stdio.readLine()
            moves_of_user = line_input.split(' ')
            validate_moves_users(moves_of_user[0], moves_of_user[1], moves_of_user[2], board_data)
    except:
        pass
    print_board(rows_board,columns_board,board_data)
        

  


def user_input_process(rows, cols, mode):
    game_board = [[' ' for _ in range(cols)] for _ in range(rows)]
    # Input Validation
    if not (8 <= rows <= 10) or not (8 <= cols <= 10):
        stdio.write("ERROR : Illegal Arguments")
    else:
      
            try:
                while True:
                    line_input = stdio.readLine()
                    user_inputs = line_input.split(' ')
                    if len(user_inputs) != 4:
                        piece_passed_check_validate(user_inputs[0], user_inputs[1], user_inputs[2], 0, rows, cols)
                    else:
                        piece_passed_check_validate(user_inputs[0], user_inputs[1], user_inputs[2], user_inputs[3], rows, cols)
                        
                    
            except:
                pass
            check_draw_game_logic(game_board, rows, cols)


def check_object_type(c):
    if c not in ('s', 'l', 'd', 'x'):
        stdio.write(f"ERROR: Invalid object type {c} \n")
        exit()
    

def piece_passed_check_validate(character, coor1, coor2, coor3, rows, cols):
    # CHECK IF OBJECT TYPE IS LEGAL
    check_object_type(character)
    
    # CHECK IF COORDINATES OF MOVE ARE INTEGERS AND ALSO WITHIN RANGE OF THE BOARD
    try:
        coor2 = int(coor2)
        coor3 = int(coor3)
        # CHECK IF COORDINATES ARE WITHIN RANGE
        if (coor2 in range(rows)) and (coor3 in range(cols)):
            pass
        else:
            stdio.write(f"ERROR: Field {coor2} {coor3} not on board_data. \rows")
            exit()
    except ValueError:
        stdio.write(f"ERROR: Field {coor2} {coor3} not on board_data. \rows")
        exit()
    # CONVERT THE DIMENSIONS OF THE PIECE INTO AN INTEGER AND CHECK IF PIECE TYPES ARE LEGAL
    try:
        # ONLY APPLY TO FIELDS THAT ARE NOT BLOCKED FIELDS
        if character != 'x':
            if character != 'd' and character != 'l':
                coor1 = int(coor1)
                if coor1 not in (1, 2):
                    stdio.write(f"ERROR: Invalid piece type {coor1} \rows")
                    exit()
            else:
                if coor1 not in ("a", "b", "character", "d"):
                    stdio.write(f"ERROR: Invalid piece type {coor1} \rows")
                    exit()
    except ValueError:
        stdio.write(f"ERROR: Invalid piece type {coor1} \rows")
        exit()
    # COLLECT OBJECTS INTO RELEVANT LISTS
    if character.lower() == 's':
        # CHECK IF SINK FIELD WILL BE FULLY WITHIN THE OUTER THREE ROWS OR COLUMNS
        if coor2 in range(0, 3) or coor2 in range(rows - 3, rows):
            if coor3 in range(0, 3) or coor3 in range(cols - 3, cols):
                pass
            else:
                stdio.write(f"ERROR: Sink in the wrong position.\rows")
                exit()
        else:
            stdio.write(f"ERROR: Sink in the wrong position.\rows")
            exit()
        # IF SINK PASSES CONSTRAINTS, APPEND TO LIST
        sinks.append([character, coor1, coor2, coor3])
    elif character.lower() == 'x':
        # CHECK IF FIELD WILL BE FULLY WITHIN THE OUTER THREE ROWS OR COLUMNS
        coor1 = int(coor1)
        blocked_elements.append([character, coor1, coor2])
    elif character.lower() == 'd':
        if coor2 in range(0, 3) or coor2 in range(rows - 3, rows):
            stdio.write(f"ERROR: Piece in the wrong position.\rows")
            exit()
        else:
            if coor3 in range(0, 3) or coor3 in range(cols - 3, cols):
                stdio.write(f"ERROR: Piece in the wrong position.\rows")
                exit()
            else:
                pass
        dak_elements.append([character, coor1, coor2, coor3])
    else:
        if coor2 in range(0, 3) or coor2 in range(rows - 3, rows):
            stdio.write(f"ERROR: Piece in the wrong row position.{coor2}\rows")
            exit()
        else:
            if coor3 in range(0, 3) or coor3 in range(cols - 3, cols):
                stdio.write(f"ERROR: Piece in the wrong column position. {coor3} \rows")
                exit()
            else:
                pass
        light.append([character, coor1, coor2, coor3])


def check_draw_game_logic(board_data, n, m):
    for s in sinks:
        if s[1] == 2:
            board_data[s[2] + 1][s[3]] = s[0]
            board_data[s[2]][s[3] + 1] = s[0]
            board_data[s[2] + 1][s[3] + 1] = s[0]
        board_data[s[2]][s[3]] = s[0]
    for x in blocked_elements:
        board_data[x[1]][x[2]] = x[0]
    for d in dak_elements:
        if d[1] == "a":
            pass
        elif d[1] == "b":
            pass
        elif d[1] == "c":
            pass
        else:
            board_data[d[2] + 1][d[3]] = (d[2] * 10 + d[3])
            board_data[d[2]][d[3] + 1] = (d[2] * 10 + d[3])
            board_data[d[2] + 1][d[3] + 1] = (d[2] * 10 + d[3])
        board_data[d[2]][d[3]] = d[1].upper()
    for lt in light:
        if lt[1] == "a":
            pass
        elif lt[1] == "b":
            pass
        elif lt[1] == "c":
            pass
        else:
            board_data[lt[2] + 1][lt[3]] = (lt[2] * 10 + lt[3])
            board_data[lt[2]][lt[3] + 1] = (lt[2] * 10 + lt[3])
            board_data[lt[2] + 1][lt[3] + 1] = (lt[2] * 10 + lt[3])
        board_data[lt[2]][lt[3]] = lt[1]
    game_board_print(n, m, board_data)


def validate_moves_users(n, m, move, board_data):
    n = int(n)
    m = int(m)
    # CHECK IF MOVE IS WITHIN THE RANGE OF THE GAME BOARD
    if board_data[n][m] == '':
        stdio.write(f'ERROR: No piece on field {n} {m}')
        exit()
    else:
        # Check Specified Move
        if move.strip() == "l":
            # Check If The Location Is Empty
            if str(board_data[n][m - 1]).strip() == "":
                make_move(n, m, move, board_data)
            else:
                stdio.write(f"ERROR: Field {n} {m-1} not free")
                exit()
        elif move.strip() == "r":
            # Check If The Location Is Empty
            if str(board_data[n][m + 1]).strip() == "":
                make_move(n, m, move, board_data)
            else:
                stdio.write(f"ERROR: Field {n} {m+1} not free")
                exit()
        elif move.strip() == "u":
            # Check If The Location Is Empty
            if str(board_data[n + 1][m]).strip() == "":
                make_move(n, m, move, board_data)
            else:
                stdio.write(f"ERROR: Field {n+1} {m} not free")
                exit()
        elif move.strip() == "d":
            # Check If The Location Is Empty
            if str(board_data[n - 1][m]).strip() == "":
                make_move(n, m, move, board_data)
               
            else:
                stdio.write(f"ERROR: Field {n-1} {m} not free")
                exit()


def make_move(n, m, move, board_data):
    # CHECK IF DIRECTION OF MOVE IS LEGAL
    if move in ("u", "r", "d", "l"):
        if move.strip() == "l":
            board_data[n][m - 1] = board_data[n][m]
            board_data[n][m] = ' '
        elif move.strip() == "u":
            board_data[n + 1][m] = board_data[n][m]
            board_data[n][m] = ' '    
        elif move.strip() == "r":
            board_data[n][m + 1] = board_data[n][m]
            board_data[n][m] = ' '
        elif move.strip() == "d":
            board_data[n - 1][m] = board_data[n][m]
            board_data[n][m] = ' '
    else:
        stdio.write(f"ERROR: Invalid direction {move}")
        exit()
    game_board_print(10, 10, board_data)


def main():
    args = len(sys.argv)
    # CHECK VALIDITY OF ARGUMENTS
    if args > 4:
        stdio.write("ERROR: Too many arguments \n")
        exit()
    elif args < 4:
        stdio.write("ERROR: Too few arguments \n")
        exit()
    elif args == 4:
        try:
            rows_board = int(sys.argv[1])
            columns_board = int(sys.argv[2])
            game_mode = int(sys.argv[3])
        except:
            stdio.write("ERROR: Illegal argument \n")
            exit()
        if isinstance(rows_board, str) or isinstance(columns_board, str) or isinstance(game_mode, str):
            stdio.write("ERROR: Illegal argument \n")
            exit()
        else:
            if rows_board not in range(8, 11) or columns_board not in range(8, 11) or game_mode not in range(0, 2):
                stdio.write("ERROR: Illegal argument \n")
                exit()
            else:
                pass
        user_input_process(rows_board, columns_board, game_mode)


if __name__ == '__main__':
    main()

# Deal With Errors
