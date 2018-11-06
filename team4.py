####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'InClassTest' # Only 10 chars displayed.
strategy_name = ''
strategy_description = ''
    
def move(my_history, their_history, my_score, their_score):
    global turn
    turn = 1
    if turn == 1:
        turn = 2
        return 'c'
    elif turn == 2:
        turn = 3
        return 'c'
    elif turn == 3:
        turn = 1
        return 'b'
        
        
        
    
