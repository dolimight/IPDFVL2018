####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'EvanTest' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    list = 'ccccccccccccccccccccbccccccccccccccccccbbcccccccccccccccccbbbccccccccccccccccbbbbcccccccccccccccbbbbbccccccccccccccccccccbccccccccccccccccccbbcccccccccccccccccbbbccccccccccccccccbbbbcccccccccccccccbbbbb'
    global count
    if len(their_history) == 0:
        count = 0
        return list[count]
    else:
        count += 1
        return list[count]
 