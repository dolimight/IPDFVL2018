team_name = 'JessupTest'
strategy_name = 'Gradual'
strategy_description = 'Do not betray unless betrayed. If betrayed, use betray for the number of times Ive betrayed'
    
def move(my_history, their_history, my_score, their_score):
    count = 'B' in their_history.upper()
    retaliate = False
    if len(their_history) == 0:
        return 'b'
    else:
        if their_history[-1].upper() == 'B':
            retaliate = True
            countr = 0
        if retaliate == True:
            countr +=1
            if countr <= count:
                return 'b'
            else:
                retaliate = False
                return 'c'
        else: 
            return 'c'