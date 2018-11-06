

team_name = 'MainFrame' # Only 10 chars displayed.
strategy_name = 'Find Pattern'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    if len(their_history) < 3:
        if my_history[-1:-2].upper() == 'c':
            return 'b'
        else:
            return 'c'
    elif their_history[len(their_history)-3:len(their_history)].upper() == 'BBB' and my_history[len(my_history)-3:len(my_history)].upper() == 'CCB':
        return 'b'
    elif their_history[len(their_history)-3:len(their_history)].upper() == 'CCB' and my_history[len(my_history)-3:len(my_history)].upper() == 'CCB':
        return 'b'
    elif their_history[len(their_history)-3:len(their_history)].upper() == 'CCC' and my_history[len(my_history)-3:len(my_history)].upper() == 'CCB':
        if len(my_history)>30:
            return 'b'
        else:
            return 'c'
    elif their_history[len(their_history)-3:len(their_history)].upper() == 'CBB' and my_history[len(my_history)-3:len(my_history)].upper() == 'CCB':
        return 'b'
    elif their_history[len(their_history)-3:len(their_history)].upper() == 'CBC' and my_history[len(my_history)-3:len(my_history)].upper() == 'CCB':
        return 'b'
    elif their_history[len(their_history)-3:len(their_history)].upper() == 'BCB' and my_history[len(my_history)-3:len(my_history)].upper() == 'CCB':
        return 'b'
    else:
        return 'b'