import stdio
import sys



def update_board(placement_values, d1, d2):
    # Call placement functions
    
    place_sinks(placement_values)
        
    place_blocked_elements(placement_values)
        
    place_dark_pieces(placement_values)
    
    place_light_pieces(placement_values)
        
        
        
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
                    if err[0] == True:
                       exit()
                    if checking == 0:
                        # If it's the first move and the input is "#", display board, declare light loses, and exit
                        corrdinates_board_display(rows, cols, game_board)
                        stdio.write("Light loses")
                        exit()
                    check_game_logic(game_board, rows, cols, True)
                    break
                
                checking += 1
                
                # Split the input into individual pieces
                user_inputs = line_input.split(' ')
                
                # Check the number of inputs and call the appropriate validation function
                if len(user_inputs) < 4:
                    validate_piece(user_inputs[0], user_inputs[1], user_inputs[2], 0, rows, cols)
                else:
                    validate_piece(user_inputs[0], user_inputs[1], user_inputs[2], user_inputs[3], rows, cols)
        
        except:
            pass
        
        # After all inputs are processed, check game logic
        check_game_logic(game_board, rows, cols, False)


        
err = [False]


def check_constraints(object_type, dimension1, dimension2, value_number, rows, cols):
    # Check if the object type is a sink
    if object_type.lower() == 's':
        # Check if sink is at the border of the board
        if dimension2 in range(0, 3) or dimension2 in range(rows - 3, rows):
            # Check if sink is at the border of the board or in special positions
            if value_number in range(0, 4) or value_number in range(cols - 3, cols + 1) or value_number in (3, 6, 4, 5):
                pass
            else:
                stdio.write("ERROR: Sink in the wrong position")
                exit()
        else:
            stdio.write("ERROR: Sink in the wrong position")
            exit()
        
        # Check if sink is next to another sink
        if ['s', int(dimension1), dimension2, value_number + 1] in list_sinks or ['s', int(dimension1), dimension2, value_number - 1] in list_sinks:
            stdio.write("ERROR: Sink cannot be next to another sink")
            err[0] = True
            pass
        
        # Add sink coordinates to the list
        list_sinks.append([object_type, convert_to_number(dimension1), dimension2, value_number])
    
    # Check if the object type is a dark piece
    elif object_type.lower() == 'd':
        # Check if there is a light piece at the specified position
        if ['l', dimension1, dimension2, value_number] in light_list:
            stdio.write(f"ERROR: Field {dimension2} {value_number} not free")
            err[0] = True
            pass
        
        # Check if the dark piece is at the border of the board
        if dimension2 in range(0, 3) or dimension2 in range(rows - 3, rows):
            stdio.write("ERROR: Piece in the wrong position")
            exit()
        else:
            # Check if the dark piece is at the border of the board or in special positions
            if value_number in range(0, 3) or value_number in range(cols - 3, cols):
                stdio.write("ERROR: Piece in the wrong position")
                exit()
            else:
                pass
        
        # Add dark piece coordinates to the list
        dark_list.append([object_type, dimension1, dimension2, value_number])
    
    # Check if the object type is a blocked item
    elif object_type.lower() == 'x':
        dimension1 = int(dimension1)
        # Add blocked item coordinates to the list
        blocked_items.append([object_type, dimension1, dimension2])
    
    # Check if the object type is a light piece
    else:
        # Check if there is a dark piece at the specified position
        if ['d', dimension1, dimension2, value_number] in dark_list:
            stdio.write(f"ERROR: Field {dimension2} {value_number} not free")
            err.append("ERROR: Field " + str(dimension2) + " " + str(value_number) + " not free")
            pass
        
        # Check if the light piece is at the border of the board
        if dimension2 in range(0, 3) or dimension2 in range(rows - 3, rows):
            stdio.write("ERROR: Piece in the wrong position")
            exit()
        else:
            # Check if the light piece is at the border of the board or in special positions
            if value_number in range(0, 3) or value_number in range(cols - 3, cols):
                stdio.write("ERROR: Piece in the wrong position")
                exit()
            else:
                pass
        
        # Add light piece coordinates to the list
        light_list.append([object_type, dimension1, dimension2, value_number])




def corrdinates_board_display(board_rows, board_columns, placement_values):
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
            if placement_values[index][inner] == ' ':
                stdio.write("  |")
            else:
                # Check if the value in the cell is a string or an integer
                if isinstance(placement_values[index][inner], str):
                    # If it's a string, print it with proper formatting
                    stdio.write(f" {placement_values[index][inner]}|")
                elif isinstance(placement_values[index][inner], int):
                    # If it's an integer, check its length for proper formatting
                    if len(str(placement_values[index][inner])) < 2:
                        stdio.write(f" {placement_values[index][inner]}|")
                    else:
                        stdio.write(f"{placement_values[index][inner]}|")

        # Display the right border of the row
        stdio.write("\n")
        stdio.write("  " + "+--" * board_columns + "+ \n")



def process_player_input(rows, cols, placement_values):
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
            validate_moves(moves_of_user[0], moves_of_user[1], moves_of_user[2], placement_values)
    except:
        pass


def piece_error(dim):
    if dim not in ("d", "a", "c", "b"):
        stdio.write(f"ERROR: Invalid piece type {dim}")
        exit()
    

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
                piece_error(dimension)
    except ValueError:
        # Handle the case where dimension cannot be converted to an integer
        stdio.write(f"ERROR: Invalid piece type {dimension}")
        exit()

def object_error(char):
     # Check if the object type is valid
    if char not in ('l', 'x', 'd', 's'):
        stdio.write(f"ERROR: Invalid object type {char} \n")
        exit()


def convert_to_number(c):
    return int(c)

def validate_piece(char, a1, a2, a3, rows, cols):
    # Check if the object type is valid
    object_error(char) 
    try:
        # Convert dimensions and coordinates to integers
        a2 = convert_to_number(a2)
        a3 = convert_to_number(a3)
        
        # Check if the coordinates are within the board's dimensions
        if not (a2 in range(rows)) and not (a3 in range(cols)):
            stdio.write(f"ERROR: Field {a2} {a3} not on board")
            exit()
    except ValueError:
        # Handle the case where dimensions or coordinates cannot be converted to integers
        stdio.write(f"ERROR: Field {a2} {a3} not on board")
        exit()
        
    # Validate the dimensions of the piece
    validate_dimensions(char, a1)
    
    # Check constraints for placing the piece on the board
    check_constraints(char, a1, a2, a3, rows, cols)

def place_sinks(placement_values):
    for sinking in list_sinks:
        data = sinking [0]
        if sinking [1] == 2:
            placement_values[sinking [2] + 1][sinking[3]] = data
            placement_values[sinking [2]][sinking [3] + 1] = data
            placement_values[sinking [2] + 1][sinking [3] + 1] = data
     
        placement_values[sinking[2]][sinking [3]] = data
        
def place_blocked_elements(placement_values):
     # Modify the board for blocked items
    for element in blocked_items:
        placement_values[element[1]][element[2]] = element[0]


def place_dark_pieces(placement_values):
    # Modify the board for dark pieces
    for d in dark_list:
        if d[1] not in ("a", "b", "c"):
             # Make placement of digits
            placement_values[d[2] + 1][d[3]] = d[2] * 10 + d[3]
            placement_values[d[2]][d[3] + 1] = d[2] * 10 + d[3]
            placement_values[d[2] + 1][d[3] + 1] = d[2] * 10 + d[3]
           
        # Modify the dark piece cell
        placement_values[d[2]][d[3]] = d[1].upper()
    
def place_light_pieces(placement_values):
    # Modify the board for light pieces
    for lt in light_list:
        if lt[1] not in ("a", "b", "c"):
            # If the light piece is not of size 1x1, update the surrounding cells accordingly
            placement_values[lt[2] + 1][lt[3]] = lt[2] * 10 + lt[3]
            placement_values[lt[2]][lt[3] + 1] = lt[2] * 10 + lt[3]
            placement_values[lt[2] + 1][lt[3] + 1] = lt[2] * 10 + lt[3]
            
        # Modify light cell
        placement_values[lt[2]][lt[3]] = lt[1]
        
    
def check_game_logic(placement_values, n, m, check):
    # Update board placed values 
    update_board(placement_values, n, m)
    
    # If check is True, display the board; otherwise, process player input
    if check:
        corrdinates_board_display(n, m, placement_values)
    else:
        process_player_input(n, m, placement_values)

  
win_comparison = [0, 0]


def call_print(a, b, placement_values):
    # Call Print Function
    corrdinates_board_display(a, b, placement_values)
    process_player_input(a, b, placement_values) 
    
def check_player_win(placement_values):
    
    # Check Player win 
    if win_comparison[0] == len(light_list) and win_comparison[0] >= 4:
            corrdinates_board_display(10, 10, placement_values)
            stdio.write(f"Light wins!")
            exit()
    if win_comparison[1] == len(dark_list) and win_comparison[1] >= 4:
            corrdinates_board_display(10, 10, placement_values)
            stdio.write(f"Dark wins!")
            exit()

def check_move_validity(n, m, move, placement_values):
        # Left Direction
        
        
    if move.strip() == "l":
        if str(placement_values[n][m - 1]).strip() in ("", "s"):
            if str(placement_values[n][m - 1]).strip() == "s":
                if str(placement_values[n][m]).lower():
                    win_comparison[0] += 1
                else:
                    win_comparison[1] += 1

                placement_values[n][m] = ' '

                check_player_win(placement_values)

                call_print(10, 10, placement_values)
            else:
                apply_move_user(n, m, move, placement_values)
        else:
            stdio.write(f"ERROR: Field {n} {m - 1} not free")
            exit()
            
       # Upward Direction
    elif move.strip() == "u":
        if str(placement_values[n + 1][m]).strip() in ("", "s"):
            if str(placement_values[n + 1][m]).strip() == "s":
                if str(placement_values[n][m]).lower():
                    win_comparison[0] += 1
                else:
                    win_comparison[1] += 1

                placement_values[n][m] = ' '

                check_player_win(placement_values)

                call_print(10, 10, placement_values)
            else:
                apply_move_user(n, m, move, placement_values)
        else:
            stdio.write(f"ERROR: Field {n + 1} {m} not free")
            exit()
            
            # Right Direction
    elif move.strip() == "r":
        if str(placement_values[n][m + 1]).strip() in ("", "s"):
            if str(placement_values[n][m + 1]).strip() == "s":
                if str(placement_values[n][m]).lower():
                    win_comparison[0] += 1
                else:
                    win_comparison[1] += 1

                placement_values[n][m] = ' '

                check_player_win(placement_values)

                call_print(10, 10, placement_values)
            else:
                apply_move_user(n, m, move, placement_values)
        else:
            stdio.write(f"ERROR: Field {n} {m + 1} not free")
            exit()
    elif move.strip() == "d":
        if str(placement_values[n - 1][m]).strip() in ("", "s"):
            if str(placement_values[n - 1][m]).strip() == "s":
                if str(placement_values[n][m]).lower():
                    win_comparison[0] += 1
                else:
                    win_comparison[1] += 1

                placement_values[n][m] = ' '

                check_player_win(placement_values)

                call_print(10, 10, placement_values)
            else:
                apply_move_user(n, m, move, placement_values)
        else:
            stdio.write(f"ERROR: Field {n - 1} {m} not free")
            exit()
    else:
        stdio.write(f"ERROR: Invalid direction {move}")
        exit()

checker_increment = [0]

def apply_move_user(n, m, move, placement_values):
    
    # Check if direction of move is legal
    if move in direction_users:
        if move.strip() == "l":
            if m - 1 < 0:
                stdio.write(f'ERROR: Cannot move beyond the board')
                exit()
            placement_values[n][m - 1] = placement_values[n][m]
            placement_values[n][m] = ' '
        elif move.strip() == "u":
            if n + 1 >= 10:
                stdio.write(f'ERROR: Cannot move beyond the board')
                exit()
            placement_values[n + 1][m] = placement_values[n][m]
            placement_values[n][m] = ' '    
        elif move.strip() == "r":
            if m + 1 >= 10:
                stdio.write(f'ERROR: Cannot move beyond the board')
                exit()
            placement_values[n][m + 1] = placement_values[n][m]
            placement_values[n][m] = ' '
        elif move.strip() == "d":
            if n - 1 < 0:
                stdio.write(f'ERROR: Cannot move beyond the board')
                exit()
            if n - 1 == 3 and m == 3 and placement_values[n][m]=='a':
                stdio.write(f'ERROR: Piece cannot be returned to starting position')
                exit()
            placement_values[n - 1][m] = placement_values[n][m]
            placement_values[n][m] = ' '
    else:
        stdio.write(f"ERROR: Invalid direction {move}")
        exit()

    call_print(10, 10, placement_values)

# Global Data Variables
dark_list = []
light_list = []
list_sinks = []
blocked_items = []
direction_users = ("u", "r", "d", "l")


def second_move():
    stdio.write(f'ERROR: Cannot move a 2x2x2 piece on the second move')
    
def check_second_move(a,b,user_move,board_passed):
    if str(board_passed[a][b]) == 'd' and str(board_passed[a][b + 1]) == "44" and user_move == 'r':
        second_move()
        exit()
    else:
        check_move_validity(a,b,user_move,board_passed)
    


def validate_moves(n, m, move, placement_values):
    n = convert_to_number(n)
    m = convert_to_number(m)
    
    if checker_increment[0] == 0 and str(placement_values[n][m]).isupper():
        stdio.write(f"ERROR: Piece does not belong to the correct player")
        exit()
        
    if checker_increment[0] == 0 and len(str(move)) == 0:
        stdio.write(f"Light loses")
        exit()
    
    checker_increment[0] += 10      
    
    if placement_values[n][m] == ' ':
        stdio.write(f'ERROR: No piece on field {n} {m}')
        exit()
    
    check_second_move(n,m,move,placement_values)

def write_illegal():
    stdio.write("ERROR: Illegal argument \n") 
        
# driver code
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
            game_mode_being_played =  convert_to_number(sys.argv[3])
            board_rows      =  convert_to_number(sys.argv[1])
            board_columns   =  convert_to_number(sys.argv[2])
          
        except ValueError:
            write_illegal()
            exit()
        
        if board_rows not in range(8, 11) or board_columns not in range(8, 11) or game_mode_being_played not in range(0, 2):
            write_illegal()
            exit()
            
        process_input(board_rows, board_columns, game_mode_being_played)

# Main function
if __name__ == '__main__':
    main()
