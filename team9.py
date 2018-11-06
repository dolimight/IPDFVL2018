####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'B' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    import random
    if len(my_history) == 0:
        return random.choice ('cb')
    elif (their_score) < my_score:
        if (their_score) + (my_score) > 0:
            return 'c'
        else:
            return 'b'
    else:
        return 'b'