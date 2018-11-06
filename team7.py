team_name = 'Jack' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
import random
a = 0
global a
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.'''
    global a
    for g in range(100):
        a=a+1
        if a == 99:
            return 'b'
        if a == 199:
            return 'b'
        else:
            return 'c'