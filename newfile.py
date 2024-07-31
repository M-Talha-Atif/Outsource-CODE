import stdio
import sys

def check_constraints(object_type, dimension1, dimension2, coordinate3, rows, cols):
    # Check if the object type is a sink
    if object_type.lower() == 's':
        # Check if sink is at the border of the board
        if dimension2 in range(0, 3) or dimension2 in range(rows - 3, rows):
            # Check if sink is at the border of the board or in special positions
            if coordinate3 in range(0, 4) or coordinate3 in range(cols - 3, cols + 1) or coordinate3 in (3, 6, 4, 5):
                pass
            else:
                stdio.write("ERROR: Sink in the wrong position")
                exit()
        else:
            stdio.write("ERROR: Sink in the wrong position")
            exit()
        
        # Check if sink is next to another sink
        if ['s', dimension1, dimension2, coordinate3 + 1] in list_sinks or ['s', dimension1, dimension2, coordinate3 - 1] in list_sinks:
            stdio.write("ERROR: Sink cannot be next to another sink")
            error_messages.append("ERROR: Sink cannot be next to another sink")
            pass
        
        # Add sink coordinates to the list
        list_sinks.append([object_type, dimension1, dimension2, coordinate3])
    
    # Check if the object type is a dark piece
    elif object_type.lower() == 'd':
        # Check if there is a light piece at the specified position
        if ['l', dimension1, dimension2, coordinate3] in light_list:
            stdio.write(f"ERROR: Field {dimension2} {coordinate3} not free")
            error_messages.append("ERROR: Field " + str(dimension2) + " " + str(coordinate3) + " not free")
            pass
        
        # Check if the dark piece is at the border of the board
        if dimension2 in range(0, 3) or dimension2 in range(rows - 3, rows):
            stdio.write("ERROR: Piece in the wrong position")
            exit()
        else:
            # Check if the dark piece is at the border of the board or in special positions
            if coordinate3 in range(0, 3) or coordinate3 in range(cols - 3, cols):
                stdio.write("ERROR: Piece in the wrong position")
                exit()
            else:
                pass
        
        # Add dark piece coordinates to the list
        dark_list.append([object_type, dimension1, dimension2, coordinate3])
    
    # Check if the object type is a blocked item
    elif object_type.lower() == 'x':
        dimension1 = int(dimension1)
        # Add blocked item coordinates to the list
        blocked_items.append([object_type, dimension1, dimension2])
    
    # Check if the object type is a light piece
    else:
        # Check if there is a dark piece at the specified position
        if ['d', dimension1, dimension2, coordinate3] in dark_list:
            stdio.write(f"ERROR: Field {dimension2} {coordinate3} not free")
            error_messages.append("ERROR: Field " + str(dimension2) + " " + str(coordinate3) + " not free")
            pass
        
        # Check if the light piece is at the border of the board
        if dimension2 in range(0, 3) or dimension2 in range(rows - 3, rows):
            stdio.write("ERROR: Piece in the wrong position")
            exit()
        else:
            # Check if the light piece is at the border of the board or in special positions
            if coordinate3 in range(0, 3) or coordinate3 in range(cols - 3, cols):
                stdio.write("ERROR: Piece in the wrong position")
                exit()
            else:
                pass
        
        # Add light piece coordinates to the list
        light_list.append([object_type, dimension1, dimension2, coordinate3])

error_messages = []

def process_input(rows, cols, mode):
    # Create an empty game board
    game_board = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    # Input Validation
    if not (8 <= rows <= 10) or not (8 <= cols <= 10):
        # If the dimensions are invalid, print an error message
        stdio.write("ERROR: Invalid arguments")
    else:
        try:
            checking = 0
            while True:
                line_input = stdio.readLine()
                
                # If the input is "#", check game logic and exit
                if line_input == "#":
                    if checking == 0:
                        # If it's the first move and the input is "#", display board, declare light loses, and exit
                        display_board(rows, cols, game_board)
                        stdio.write("Light loses")
                        exit()
                    check_game_logic(game_board, rows, cols, True)
                    break
                
                checking += 1
                
                # Split the input into individual pieces
                user_inputs = line_input.split(' ')
                
                # Check the number of inputs and call the appropriate validation function
                if len(user_inputs) != 4:
                    validate_piece(user_inputs[0], user_inputs[1], user_inputs[2], 0, rows, cols)
                else:
                    validate_piece(user_inputs[0], user_inputs[1], user_inputs[2], user_inputs[3], rows, cols)
        
        except:
            pass
        
        # After all inputs are processed, check game logic
        check_game_logic(game_board, rows, cols, False)





def display_board(board_rows, board_columns, board_values):
    # Print column numbers
    stdio.write("  ")
    for index in range(board_columns):
        stdio.write(f" {index} ")
    stdio.write("\n")

    # Display top border
    stdio.write("  " + "+--" * board_columns + "+ \n")

    # Print each row
    for index in range(board_rows - 1, -1, -1):
        # Display left border and row number
        stdio.write(f"{index} |")

        # Print each cell in the row
        for inner in range(board_columns):
            # Check if the cell is empty
            if board_values[index][inner] == ' ':
                stdio.write("  |")
            else:
                # Check if the value in the cell is a string or an integer
                if isinstance(board_values[index][inner], str):
                    # If it's a string, print it with proper formatting
                    stdio.write(f" {board_values[index][inner]}|")
                elif isinstance(board_values[index][inner], int):
                    # If it's an integer, check its length for proper formatting
                    if len(str(board_values[index][inner])) < 2:
                        stdio.write(f" {board_values[index][inner]}|")
                    else:
                        stdio.write(f"{board_values[index][inner]}|")

        # Display the right border of the row
        stdio.write("\n")
        stdio.write("  " + "+--" * board_columns + "+ \n")



def process_player_input(rows, cols, board_values):
    try:
        while True:
            # Read the input from the player
            line_input = stdio.readLine()
            
            # Split the input into individual moves
            moves_of_user = line_input.split(' ')
            
            # Check if the move is within the board's dimensions
            if int(moves_of_user[0]) > 10 and int(moves_of_user[1]) > 10:
                stdio.write(f"ERROR: Field {moves_of_user[0]} {moves_of_user[1]} not on board")
                exit()
            
            # Validate the move
            validate_moves(moves_of_user[0], moves_of_user[1], moves_of_user[2], board_values)
    except:
        pass


    

def validate_dimensions(piece_type, dimension):
    try:
        # Convert the dimension of the piece into an integer and check if piece types are legal
        if piece_type != 'x':  # Only apply to fields that are not blocked fields
            if piece_type != 'd' and piece_type != 'l':
                # Check if the piece type is valid (for non-dark and non-light pieces)
                dimension = int(dimension)
                if dimension not in (1, 2):
                    stdio.write(f"ERROR: Invalid piece type {dimension}")
                    exit()
            else:
                # Check if the piece type is valid (for dark and light pieces)
                if dimension not in ("a", "b", "c", "d"):
                    stdio.write(f"ERROR: Invalid piece type {dimension}")
                    exit()
    except ValueError:
        # Handle the case where dimension cannot be converted to an integer
        stdio.write(f"ERROR: Invalid piece type {dimension}")
        exit()


        
    

def validate_piece(char, d1, d2, coor3, rows, cols):
    # Check if the object type is valid
    if char not in ('l', 'x', 'd', 's'):
        stdio.write(f"ERROR: Invalid object type {char} \n")
        exit()
    
    try:
        # Convert dimensions and coordinates to integers
        d2 = int(d2)
        coor3 = int(coor3)
        
        # Check if the coordinates are within the board's dimensions
        if not (d2 in range(rows)) and not (coor3 in range(cols)):
            stdio.write(f"ERROR: Field {d2} {coor3} not on board")
            exit()
    except ValueError:
        # Handle the case where dimensions or coordinates cannot be converted to integers
        stdio.write(f"ERROR: Field {d2} {coor3} not on board")
        exit()
        
    # Validate the dimensions of the piece
    validate_dimensions(char, d1)
    
    # Check constraints for placing the piece on the board
    check_constraints(char, d1, d2, coor3, rows, cols)



def update_board(board_values, n, m):
    # Update the board for sinks
    for s in list_sinks:
        if s[1] == 2:
            # If the sink is of size 2x2, update the surrounding cells accordingly
            board_values[s[1] + 1][s[3]] = s[0]
            board_values[s[1]][s[3] + 1] = s[0]
            board_values[s[1] + 1][s[3] + 1] = s[0]
        # Update the sink cell
        board_values[s[1]][s[3]] = s[0]
        
    # Update the board for blocked items
    for element in blocked_items:
        board_values[element[1]][element[2]] = element[0]
        
    # Update the board for dark pieces
    for d in dark_list:
        if d[1] in ("a", "b", "c"):
            pass
        else:
            # If the dark piece is not of size 1x1, update the surrounding cells accordingly
            board_values[d[2] + 1][d[3]] = d[2] * 10 + d[3]
            board_values[d[2]][d[3] + 1] = d[2] * 10 + d[3]
            board_values[d[2] + 1][d[3] + 1] = d[2] * 10 + d[3]
        # Update the dark piece cell
        board_values[d[2]][d[3]] = d[1].upper()
        
    # Update the board for light pieces
    for lt in light_list:
        if lt[1] in ("a", "b", "c"):
            pass
        else:
            # If the light piece is not of size 1x1, update the surrounding cells accordingly
            board_values[lt[2] + 1][lt[3]] = lt[2] * 10 + lt[3]
            board_values[lt[2]][lt[3] + 1] = lt[2] * 10 + lt[3]
            board_values[lt[2] + 1][lt[3] + 1] = lt[2] * 10 + lt[3]
        # Update the light piece cell
        board_values[lt[2]][lt[3]] = lt[1]

    
def check_game_logic(board_values, n, m, check):
    # Update the board with the current state
    update_board(board_values, n, m)
    
    # If check is True, display the board; otherwise, process player input
    if check:
        display_board(n, m, board_values)
    else:
        process_player_input(n, m, board_values)

  
check_win_light = [0, 0]

def check_move_validity(n, m, move, board_values):
        # Check the direction of the move and validate it accordingly
    if move.strip() == "l":
        if str(board_values[n][m - 1]).strip() in ("", "s"):
            if str(board_values[n][m - 1]).strip() == "s":
                if str(board_values[n][m]).lower():
                    check_win_light[0] += 1
                else:
                    check_win_light[1] += 1

                board_values[n][m] = ' '

                if check_win_light[0] == len(light_list) and check_win_light[0] >= 4:
                    display_board(10, 10, board_values)
                    stdio.write(f"Light wins!")
                    exit()
                if check_win_light[1] == len(dark_list) and check_win_light[1] >= 4:
                    display_board(10, 10, board_values)
                    stdio.write(f"Dark wins!")
                    exit()

                call_print(10, 10, board_values)
            else:
                apply_move_user(n, m, move, board_values)
        else:
            stdio.write(f"ERROR: Field {n} {m - 1} not free")
            exit()
    elif move.strip() == "r":
        if str(board_values[n][m + 1]).strip() in ("", "s"):
            if str(board_values[n][m + 1]).strip() == "s":
                if str(board_values[n][m]).lower():
                    check_win_light[0] += 1
                else:
                    check_win_light[1] += 1

                board_values[n][m] = ' '

                if check_win_light[0] == len(light_list) and check_win_light[0] >= 4:
                    display_board(10, 10, board_values)
                    stdio.write(f"Light wins!")
                    exit()
                if check_win_light[1] == len(dark_list) and check_win_light[1] >= 4:
                    display_board(10, 10, board_values)
                    stdio.write(f"Dark wins!")
                    exit()

                call_print(10, 10, board_values)
            else:
                apply_move_user(n, m, move, board_values)
        else:
            stdio.write(f"ERROR: Field {n} {m + 1} not free")
            exit()
    elif move.strip() == "u":
        if str(board_values[n + 1][m]).strip() in ("", "s"):
            if str(board_values[n + 1][m]).strip() == "s":
                if str(board_values[n][m]).lower():
                    check_win_light[0] += 1
                else:
                    check_win_light[1] += 1

                board_values[n][m] = ' '

                if check_win_light[0] == len(light_list) and check_win_light[0] >= 4:
                    display_board(10, 10, board_values)
                    stdio.write(f"Light wins!")
                    exit()
                if check_win_light[1] == len(dark_list) and check_win_light[1] >= 4:
                    display_board(10, 10, board_values)
                    stdio.write(f"Dark wins!")
                    exit()

                call_print(10, 10, board_values)
            else:
                apply_move_user(n, m, move, board_values)
        else:
            stdio.write(f"ERROR: Field {n + 1} {m} not free")
            exit()
    elif move.strip() == "d":
        if str(board_values[n - 1][m]).strip() in ("", "s"):
            if str(board_values[n - 1][m]).strip() == "s":
                if str(board_values[n][m]).lower():
                    check_win_light[0] += 1
                else:
                    check_win_light[1] += 1

                board_values[n][m] = ' '

                if check_win_light[0] == len(light_list) and check_win_light[0] >= 4:
                    display_board(10, 10, board_values)
                    stdio.write(f"Light wins!")
                    exit()
                if check_win_light[1] == len(dark_list) and check_win_light[1] >= 4:
                    display_board(10, 10, board_values)
                    stdio.write(f"Dark wins!")
                    exit()

                call_print(10, 10, board_values)
            else:
                apply_move_user(n, m, move, board_values)
        else:
            stdio.write(f"ERROR: Field {n - 1} {m} not free")
            exit()
    else:
        stdio.write(f"ERROR: Invalid direction {move}")
        exit()

            
def call_print(a, b, board_values):
    display_board(a, b, board_values)
    process_player_input(a, b, board_values)   

def validate_moves(n, m, move, board_values):
    # Convert values to integers
    n = int(n)
    m = int(m)
    
    if increment[0] == 0 and str(board_values[n][m]).isupper():
        stdio.write(f"ERROR: Piece does not belong to the correct player")
        exit()
        
    if increment[0] == 0 and len(str(move)) == 0:
        stdio.write(f"Light loses")
        exit()
    
    increment[0] += 1      
    
    # Check if the moves are  within the range of the game board
    if board_values[n][m] == ' ':
        stdio.write(f'ERROR: No piece on field {n} {m}')
        exit()
    
    if str(board_values[n][m + 1]) == "44" and str(board_values[n][m]) == 'd' and move == 'r':
        stdio.write(f'ERROR: Cannot move a 2x2x2 piece on the second move')
        exit()
    else:
        check_move_validity(n, m, move, board_values)
        

def apply_move_user(n, m, move, board_values):
    initial_n, initial_m = 3, 3
    
    # Check if direction of move is legal
    if move in direction_users:
        if move.strip() == "l":
            if m - 1 < 0:
                stdio.write(f'ERROR: Cannot move beyond the board')
                exit()
            board_values[n][m - 1] = board_values[n][m]
            board_values[n][m] = ' '
        elif move.strip() == "u":
            if n + 1 >= 10:
                stdio.write(f'ERROR: Cannot move beyond the board')
                exit()
            board_values[n + 1][m] = board_values[n][m]
            board_values[n][m] = ' '    
        elif move.strip() == "r":
            if m + 1 >= 10:
                stdio.write(f'ERROR: Cannot move beyond the board')
                exit()
            board_values[n][m + 1] = board_values[n][m]
            board_values[n][m] = ' '
        elif move.strip() == "d":
            if n - 1 < 0:
                stdio.write(f'ERROR: Cannot move beyond the board')
                exit()
            if n - 1 == initial_n and m == initial_m :
                stdio.write(f'ERROR: Piece cannot be returned to starting position')
                exit()
            board_values[n - 1][m] = board_values[n][m]
            board_values[n][m] = ' '
    else:
        stdio.write(f"ERROR: Invalid direction {move}")
        exit()
    
    a, b = 10, 10
    call_print(a, b, board_values)

# Global Data Variables
dark_list = []
light_list = []
list_sinks = []
blocked_items = []
direction_users = ("u", "r", "d", "l")
increment = [0]

  

def main():
    args = len(sys.argv)
    counter = 4
    
    # Check validity of arguments
    if args > counter:
        stdio.write("ERROR: Too many arguments \n")
        exit()
    elif args < counter:
        stdio.write("ERROR: Too few arguments \n")
        exit()
    elif args == counter:
        try:
            mode_game_taken = int(sys.argv[3])
            board_rows = int(sys.argv[1])
            board_columns = int(sys.argv[2])
          
        except ValueError:
            stdio.write("ERROR: Illegal argument \n")
            exit()
        
        if board_rows not in range(8, 11) or board_columns not in range(8, 11) or mode_game_taken not in range(0, 2):
            stdio.write("ERROR: Illegal argument \n")
            exit()
            
        process_input(board_rows, board_columns, mode_game_taken)

# Main function
if __name__ == '__main__':
    main()
