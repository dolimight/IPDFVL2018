####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Evan' # Only 10 chars displayed.
strategy_name = 'Random than counter most'
strategy_description = ''
    
def move(my_history, their_history, my_score, their_score):
    import random
    if len(my_history) == 0:
        return random.choice('cb')
    if their_history.count('c') > their_history.count('b'):
        return 'c'
    else:
        return 'b'