####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'FindHistory' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    if len(their_history) < 2:
            return 'c'
    elif their_history[0:5].upper() == 'BBBBB':
            return 'b' 
    elif their_history[0:2] == '  ':
        return 'b'
    elif their_history[0:5].upper() == 'CCCCC':
        return 'b'
    else:
       return their_history[-1]