import stdio
import sys

error = []

def check_conditions(char, d1, d2, coor3, rows_here, cols_here):
     # COLLECT OBJECTS INTO RELEVANT LISTS
    if char.lower() == 's':
        # ChECK IF SINK FIELD WILL BE FULLY WIThIN ThE OUTER ThREE ROWS OR COLUMNS
        if d2 in range(0, 3) or d2 in range(rows_here - 3, rows_here):
            if coor3 in range(0, 4) or coor3 in range(cols_here - 3, cols_here+1) or coor3 in (3,6,4,5):
                pass
            else:
                stdio.write(f"ERROR: Sink in the wrong position")
    
                exit()
        else:
            stdio.write(f"ERROR: Sink in the wrong position")
        
            exit()
        if ['s', d1, d2, coor3+1] in list_sinks or ['s', d1, d2, coor3-1] in list_sinks:
            stdio.write(f"ERROR: Sink cannot be next to another sink")
            error[0] = True
            error[1] = f"ERROR: Sink cannot be next to another sink"
            pass
        # IF SINK PASSES CONSTRAINTS, APPEND TO LIST
        list_sinks.append([char, int(d1), d2, coor3])
        
        
    elif char.lower() == 'd':
        if ['l',d1, d2, coor3] in light_list:
            stdio.write(f"ERROR: Field {d2} {coor3} not free")
            error[0] = True
            error[1] = "ERROR: Field " + str(d2) + " " + str(coor3) + " not free"
            pass
           
        if d2 in range(0, 3) or d2 in range(rows_here - 3, rows_here):
            stdio.write(f"ERROR: Piece in the wrong position")
            exit()
        else:
            if coor3 in range(0, 3) or coor3 in range(cols_here - 3, cols_here):
                stdio.write(f"ERROR: Piece in the wrong position")
                exit()
            else:
                pass
        dark_list.append([char, d1, d2, coor3])
    elif char.lower() == 'x':
        # ChECK IF FIELD WILL BE FULLY WIThIN ThE OUTER ThREE ROWS OR COLUMNS
        d1 = int(d1)
        blocked_items.append([char, d1, d2])
 
    else:
        if ['d',d1, d2, coor3] in dark_list:
            stdio.write(f"ERROR: Field {d2} {coor3} not free")
            error[0] = True
            error[1] = "ERROR: Field " + str(d2) + " " + str(coor3) + " not free"
            pass
            
        if d2 in range(0, 3) or d2 in range(rows_here - 3, rows_here):
            stdio.write(f"ERROR: Piece in the wrong position")
            exit()
        else:
            if coor3 in range(0, 3) or coor3 in range(cols_here - 3, cols_here):
                stdio.write(f"ERROR: Piece in the wrong position")
                exit()
            else:
                pass
        light_list.append([char, d1, d2, coor3])
    
        
container =[10,10]
def input_given_process(rows_here, cols_here, mode):
    game_board = [[' ' for _ in range(cols_here)] for _ in range(rows_here)]
    # Input Validation
    if not (8 <= rows_here <= 10) or not (8 <= cols_here <= 10):
        stdio.write("ERROR: Illegal Arguments")
    else:
      
            try:
                checking = 0
                container[0] = rows_here
                container[1] = cols_here
                while True:
                    line_input = stdio.readLine()
                    if line_input == "#":
                        if checking==0:
                          display_board_users(rows_here,cols_here,game_board)  
                          stdio.write("Light loses")
                          exit() 
                         
                        check_draw_game_logic(game_board, rows_here, cols_here,True)
                        break
                    
                    checking+=1
                                
                    user_inputs = line_input.split(' ')
                   
                    
                    if len(user_inputs) < 4:
                        piece_passed_check_validate(user_inputs[0], user_inputs[1], user_inputs[2], 0, rows_here, cols_here)
                    else:
                       
                        piece_passed_check_validate(user_inputs[0], user_inputs[1], user_inputs[2], user_inputs[3], rows_here, cols_here)
                    
                    
            except:
                pass
            check_draw_game_logic(game_board, rows_here, cols_here,False)




def display_board_users(board_rows, board_columns, board_values):

    stdio.write("  ")
    
    for index in range(board_columns):
        stdio.write(f" {index} ")

    stdio.write("\n")
    # Display top border
    stdio.write("  " + "+--" * board_columns + "+ \n")

    # Print each row
    for index in range(board_rows - 1, -1, -1):
        # Display left border
        stdio.write(f"{index} |")

        # Print each cell
        for inner in range(board_columns):
            if board_values[index][inner] == ' ':
                stdio.write("  |")
            else:
                if isinstance(board_values[index][inner], str):
                    stdio.write(f" {board_values[index][inner]}|")
                elif isinstance(board_values[index][inner], int):
                    if len(str(board_values[index][inner])) < 2:
                        stdio.write(f" {board_values[index][inner]}|")
                    else:
                        stdio.write(f"{board_values[index][inner]}|")

        # Display the right border
        stdio.write("\n")
        stdio.write("  " + "+--" * board_columns + "+ \n") 
        


def dark_light_player_board_input(rows_here,cols_here,board_values):
  
    # Check For Any Moves In File
    try:
        while True:
            line_input = stdio.readLine()
                          
            moves_of_user = line_input.split(' ')
            
            if int(moves_of_user[0])>10 and int(moves_of_user[1])>10:
                stdio.write(f"ERROR: Field {moves_of_user[0]} {moves_of_user[1]} not on board")
                exit()
                
            validate_moves_users(moves_of_user[0], moves_of_user[1], moves_of_user[2], board_values)
         
    except:
        pass
    # display_board_users(rows_here, cols_here, board_values)
    
    

def validate_dimensions(char,d1):
     # CONVERT ThE DIMENSIONS OF ThE PIECE INTO AN INTEGER AND ChECK IF PIECE TYPES ARE LEGAL
    try:
        # ONLY APPLY TO FIELDS ThAT ARE NOT BLOCKED FIELDS
        if char != 'x':
            if char != 'd' and char != 'l':
                d1 = int(d1)
                if d1 not in (1, 2):
                    stdio.write(f"ERROR: Invalid piece type {d1}")
                    exit()
            else:
                if d1 not in ("a", "b", "c", "d"):
                    stdio.write(f"ERROR: Invalid piece type {d1}")
                    exit()
    except ValueError:
        stdio.write(f"ERROR: Invalid piece type {d1}")
        exit()
        
        


def piece_passed_check_validate(char, d1, d2, coor3, rows_here, cols_here):
    # ChECK IF OBJECT TYPE IS LEGAL
    if char not in ('l' , 'x' , 'd', 's'):
        stdio.write(f"ERROR: Invalid object type {char} \n")
        exit()
    
    # ChECK IF COORDINATES OF MOVE ARE INTEGERS AND ALSO WIThIN RANGE OF ThE BOARD
    try:
        d2 = int(d2)
        coor3 = int(coor3)
        # ChECK IF COORDINATES ARE WIThIN RANGE
        if not (d2 in range(rows_here)) and not (coor3 in range(cols_here)):
            stdio.write(f"ERROR: Field {d2} {coor3} not on board")
            exit()
        else:
            pass
    except ValueError:
        stdio.write(f"ERROR: Field {d2} {coor3} not on board")
        exit()
        
    # Check Dimenstions
    validate_dimensions(char,d1)
    # Catch objects
    check_conditions(char, d1, d2, coor3, rows_here, cols_here)


def check_draw_game_logic(board_values, n, m, check):
    c=1 
    d=2
    p=0         
       
    for s in list_sinks:
        if s[c] == d:
            board_values[s[d] + 1][s[3]] = s[p]
            board_values[s[d]][s[3] + 1] = s[p]
            board_values[s[2] + 1][s[3] + 1] = s[p]
        board_values[s[2]][s[3]] = s[p]
        
   
    for element in blocked_items:
        board_values[element [c]][element [d]] = element [p]
        
    for d in dark_list:
        if d[c] == "a" or d[c] == "b" or d[c] == "c":
            pass
        else:
            board_values[d[2] + 1][d[3]] = (d[2] * container[1]+ d[3])
            board_values[d[2]][d[3] + 1] = (d[2] * container[1] + d[3])
            board_values[d[2] + 1][d[3] + 1] = (d[2] * container[1]+ d[3])
        board_values[d[2]][d[3]] = d[1].upper()
        
    for lt in light_list:
        if lt[1] == "a" or lt[1] == "b" or lt[1] == "c":
            pass
        else:
            board_values[lt[2] + 1][lt[3]] = (lt[2] * container[1] + lt[3])
            board_values[lt[2]][lt[3] + 1] = (lt[2] * container[1] + lt[3])
            board_values[lt[2] + 1][lt[3] + 1] = (lt[2] * container[1] + lt[3])
            
        board_values[lt[2]][lt[3]] = lt[1]
        
    if check:
        display_board_users(n, m, board_values)
    else:
       dark_light_player_board_input(n,m,board_values)
  
 
check_win_light = [0,0]
def moves_made_checking(n,m,move,board_values):
        
     # Check Specified Move
        if move.strip() == "l":
            # Check If The Location Is Empty
            if str(board_values[n][m - 1]).strip() == "" or  str(board_values[n][m - 1]).strip() == "s":
              if str(board_values[n][m - 1]).strip() == "s":
                  if str(board_values[n][m]).lower():
                    check_win_light[0]+=1
                  else:
                    check_win_light[1]+=1
                
                      
                  board_values[n][m] =' '
                
                  if( check_win_light[0] == len(light_list)) and check_win_light[0]>=4:
                    display_board_users(10,10,board_values)
                    stdio.write(f"Light wins!")
                    exit()
                  if( check_win_light[1] == len(dark_list)) and check_win_light[1]>=4:
                    display_board_users(10,10,board_values)
                    stdio.write(f"Dark wins!")
                    exit()
                      
                  callPrint(10,10,board_values)
              else:
                 apply_move_user(n, m, move, board_values)
            else:
                stdio.write(f"ERROR: Field {n} {m-1} not free")
                exit()
        elif move.strip() == "r" :
            # Check If The Location Is Empty
            if str(board_values[n][m + 1]).strip() == "" or  str(board_values[n][m + 1]).strip() == "s":
                if str(board_values[n][m + 1]).strip() == "s":
                  if str(board_values[n][m]).lower():
                    check_win_light[0]+=1
                  else:
                    check_win_light[1]+=1
                
                      
                  board_values[n][m] =' '
                
                  if( check_win_light[0] == len(light_list)) and check_win_light[0]>=4:
                    display_board_users(10,10,board_values)
                    stdio.write(f"Light wins!")
                    exit()
                  if( check_win_light[1] == len(dark_list)) and check_win_light[1]>=4:
                    display_board_users(10,10,board_values)
                    stdio.write(f"Dark wins!")
                    exit()
                      
                  callPrint(10,10,board_values)
                else:
                 apply_move_user(n, m, move, board_values)
            else:
                stdio.write(f"ERROR: Field {n} {m+1} not free")
                exit()
        elif move.strip() == "u":
            # Check If The Location Is Empty
            if str(board_values[n + 1][m]).strip() == "" or  str(board_values[n+1][m ]).strip() == "s":
                if str(board_values[n+1][m]).strip() == "s":
                  if str(board_values[n][m]).lower():
                    check_win_light[0]+=1
                  else:
                    check_win_light[1]+=1
                
                      
                  board_values[n][m] =' '
              
                  if( check_win_light[0] == len(light_list)) and check_win_light[0]>=4:
                    display_board_users(10,10,board_values)
                    stdio.write(f"Light wins!")
                    exit()
                  if( check_win_light[1] == len(dark_list)) and check_win_light[1]>=4:
                    display_board_users(10,10,board_values)
                    stdio.write(f"Dark wins!")
                    exit()
                    
                  callPrint(10,10,board_values)
                else:
                 apply_move_user(n, m, move, board_values)
            else:
                stdio.write(f"ERROR: Field {n+1} {m} not free")
                exit()
        elif move.strip() == "d":
            # Check If The Location Is Empty
            if str(board_values[n - 1][m]).strip() == "" or  str(board_values[n-1][m]).strip() == "s":
                if str(board_values[n-1][m]).strip() == "s":
                  if str(board_values[n][m]).lower():
                    check_win_light[0]+=1
                  else:
                    check_win_light[1]+=1
                
                      
                  board_values[n][m] =' '
                 
                  if( check_win_light[0] == len(light_list)) and check_win_light[0]>=4:
                    display_board_users(container[0] ,container[1] ,board_values)
                    stdio.write(f"Light wins!")
                    exit()
                  if( check_win_light[1] == len(dark_list)) and check_win_light[1]>=4:
                    display_board_users(container[0] ,container[1] ,board_values)
                    stdio.write(f"Dark wins!")
                    
                    exit()
                  callPrint(container[0],container[1],board_values)
                else:
                 apply_move_user(n, m, move, board_values)
            else:
                stdio.write(f"ERROR: Field {n-1} {m} not free")
                exit()
        else:
            stdio.write(f"ERROR: Invalid direction {move}")
            exit()
            
def callPrint(a,b,board_values):
    display_board_users(container[0] ,container[1] ,board_values)
    dark_light_player_board_input(container[0] ,container[1] , board_values)   


def validate_moves_users(n, m, move, board_values):
    # Convert values to integers
    n = int(n)
    m = int(m)
    
    if  increment[0] == 0 and str(board_values[n][m]).isupper():
        stdio.write(f"ERROR: Piece does not belong to the correct player")
        exit()
        
    if  increment[0] == 0 and len(str(move))==0:
        stdio.write(f"Light loses")
        exit()
    increment[0]+=1      
    # ChECK IF MOVE IS WIThIN ThE RANGE OF ThE GAME BOARD
    if board_values[n][m] == ' ':
        stdio.write(f'ERROR: No piece on field {n} {m}')
        exit()
    # added at 3 am
    if str(board_values[n][m+1]) == "44" and str(board_values[n][m]) == 'd' and move =='r':
        stdio.write(f'ERROR: Cannot move a 2x2x2 piece on the second move')
        exit()
    else:
        moves_made_checking(n,m,move,board_values)
        
        

def apply_move_user(n, m, move, board_values):
    initial_n, initial_m = 3,3
    # ChECK IF DIRECTION OF MOVE IS LEGAL
    if move in direction_users:
        if move.strip() == "l":
            if m-1 < 0:
                stdio.write(f'ERROR: Cannot move beyond the board')
                exit()
            if board_values[n][m - 1] == ' ':
             place = board_values[n][m] 
             if board_values[n][m]=="b" or place == "B":
                 board_values[n][m - 1] = n * container[1] + (m-2)
                 board_values[n][m] = ' '
                 board_values[n][m-2] = place
                 
             elif board_values[n][m]=="d" or place == "D": # done
                 board_values[n][m - 1] = n * container[1] + (m-2)
                 board_values[n+1][m - 1] = n * container[1] + (m-2)
                 board_values[n+1][m - 2] = n * container[1] + (m-2)
                 board_values[n][m] = ' '
                 board_values[n][m-2] = place
                 
             elif board_values[n][m]=="c" or place == "C": # done
                 board_values[n][m - 2] = n * container[1] + (m-1)
                 board_values[n][m - 3] = n * container[1] + (m-1)
                 board_values[n][m] = ' '
                 board_values[n][m-1] = place
             else:
               board_values[n][m - 1] = board_values[n][m]
               board_values[n][m] = ' '
        elif move.strip() == "u":
            if n+1 >= 10:
                stdio.write(f'ERROR: Cannot move beyond the board')
                exit()
            if board_values[n+1][m] == ' ':
             place = board_values[n][m]  
             if board_values[n][m]=="b" or place == "B":
                 board_values[n+2][m ] = n+1 * container[1] + m
                 board_values[n][m] = ' '
                 board_values[n+1][m] = place
                 
             elif board_values[n][m]=="d" : # done
                 board_values[n+3][m ] = n+2 * container[1] + (m-2)
                 board_values[n+2][m ] = n+2 * container[1] + (m-2)
                 board_values[n+3][m +1] = n+2 * container[1] + (m-2)
                 board_values[n][m] = ' '
                 board_values[n+2][m] = place
                 
             elif board_values[n][m]=="c" or place == "C": # done
                 board_values[n+2][m ] = n+1 * container[1] + (m)
                 board_values[n+3][m] = n+1 * container[1] + (m)
                 board_values[n][m] = ' '
                 board_values[n+1][m] = place
             else:
               board_values[n][m - 1] = board_values[n][m]
               board_values[n][m] = ' '
            
        elif move.strip() == "r":
            if m+1 >= 10:
                stdio.write(f'ERROR: Cannot move beyond the board')
                exit()
            if board_values[n][m + 1] == ' ':
             place = board_values[n][m]
             if board_values[n][m]=="b" or place == "B":
                 board_values[n][m + 2] = n * container[1] + (m+1)
                 board_values[n][m+1] = place
                 board_values[n][m] = ' '
                 
             elif board_values[n][m]=="d" or place == "D": # done
                 board_values[n][m +3] = n * container[1] + (m+2)
                 board_values[n+1][m +2] = n * container[1] + (m+2)
                 board_values[n+1][m +3] = n * container[1] + (m+2)
                 board_values[n][m+2] = board_values[n][m]
                 board_values[n][m] = ' '
               
                 
             elif board_values[n][m]=="c" or place =="C": # done
                 board_values[n][m + 2] = n * container[1] + (m+1)
                 board_values[n][m + 3] = n * container[1] + (m+1)
                 board_values[n][m+1] = board_values[n][m]
                 board_values[n][m] = ' '
    
             else:
               board_values[n][m - 1] = board_values[n][m]
               board_values[n][m] = ' '
            
        # Downward
        elif move.strip() == "d":
            if n-1 < 0:
                stdio.write(f'ERROR: Cannot move beyond the board')
                exit()
            if n-1 ==initial_n and m==initial_m :
                stdio.write(f'ERROR: Piece cannot be returned to starting position')
                exit()
            if board_values[n-1][m] == ' ':
             place = board_values[n][m] 
             
             if board_values[n][m]=="b" or place == "B":
                 board_values[n-1][m] = n-2 * container[1] + m
                 board_values[n][m] = ' '
                 board_values[n-2][m] =  place
                 
             elif board_values[n][m]=="d" or place == "D": # done
                 board_values[n-1][m ] = n-2 * container[1] + m
                 board_values[n-1][m + 1] = n-2 * container[1] + m
                 board_values[n-2][m +1] = n-2 * container[1] + m
                 board_values[n][m] = ' '
                 board_values[n-2][m] = place
                 
             elif board_values[n][m]=="c" or place == "C": # done
                 board_values[n-2][m] = n-1 * container[1] + m
                 board_values[n-3][m] = n-1 * container[1] + m
                 board_values[n][m] = ' '
                 board_values[n-1][m] = place
             else:
               board_values[n][m - 1] = board_values[n][m]
               board_values[n][m] = ' '

    else:
        stdio.write(f"ERROR: Invalid direction {move}")
        exit()
    a=b=10
    display_board_users(container[0],container[1],board_values)
    dark_light_player_board_input(container[0], container[1], board_values)

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
    # ChECK VALIDITY OF ARGUMENTS
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
          
        except:
            stdio.write("ERROR: Illegal argument \n")
            exit()
        if isinstance(board_rows, str) or isinstance(board_columns, str) or isinstance(mode_game_taken, str):
            stdio.write("ERROR: Illegal argument \n")
            exit()
        else:
            if board_rows not in range(8, 11) or board_columns not in range(8, 11) or mode_game_taken not in range(0, 2):
                stdio.write("ERROR: Illegal argument \n")
                exit()
        input_given_process(board_rows, board_columns, mode_game_taken)

# Call Main function
if __name__ == '__main__':
    main()