def check_draw_game_logic(board_values, rows, cplums, check):
    one=1
    second=2
    three = 3       
       
    for sink_element in list_sinks:
        if sink_element[one-one+one] == second:
            board_values[sink_element[second] + one][sink_element[three]] = sink_element[p]
            board_values[sink_element[second]][sink_element[three] + one] = sink_element[p]
            board_values[sink_element[second] + one][sink_element[three] + one] = sink_element[p]
        board_values[sink_element[second]][sink_element[three]] = sink_element[p]
        
   
    for element in blocked_items:
        board_values[element [one]][element [second]] = element [p]
        
    for second in dark_list:
        if second[one] == "a" or second[one] == "b" or second[one] == "c":
            pass
        else:
            board_values[second[second] + one][second[three]] = (second[second] * 10 + second[three])
            board_values[second[second]][second[three] + one] = (second[second] * 10 + second[three])
            board_values[second[second] + one][second[three] + one] = (second[second] * 10 + second[three])
        board_values[second[second]][second[three]] = second[one].upper()
        
    for lt in light_list:
        if lt[one] == "a" or lt[one] == "b" or lt[one] == "c":
            pass
        else:
            board_values[lt[second] + one][lt[three]] = (lt[second] * 10 + lt[three])
            board_values[lt[second]][lt[three] + one] = (lt[second] * 10 + lt[three])
            board_values[lt[second] + one][lt[three] + one] = (lt[second] * 10 + lt[three])
            
        board_values[lt[second]][lt[three]] = lt[one]
        
    if check:
        display_board_users(rows, cplums, board_values)
    else:
       dark_light_player_board_input(rows,cplums,board_values)