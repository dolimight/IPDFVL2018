####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Hacked' # Only 10 chars displayed.
strategy_name = 'Attack'
strategy_description = 'It always Wins'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    '''
    myhistmostused = ''
    myc = 0
    myb = 0
    theirhistmostused = ''
    theirc = 0
    theirb = 0
    if len(my_history) == 0:
        return 'b'
    else:
        if my_score < their_score:
            for i in range(len(my_history)):
                if my_history[i] == 'c':
                    myc += 1
                else:
                    myb += 1
            if myc > myb:
                myhistmostused = 'c'
            else:
                myhistmostused = 'b'
            for i in range(len(their_history)):
                if their_history[i] == 'c':
                    theirc += 1
                else:
                    theirb += 1
            if theirc > theirb:
                theirhistmostused = 'c'
            else:
                theirhistmostused = 'b'
            if theirhistmostused == their_history[-1]:
                if theirhistmostused == 'c':
                    return 'b'
                else:
                    return 'c'
        else:
            return 'b'
        