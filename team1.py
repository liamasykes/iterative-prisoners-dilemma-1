####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'NiceGuys' # Only 10 chars displayed.
strategy_name = 'Be the nice guys'
strategy_description = 'Collude 50 times, if betrayed >25 times, then betray the rest of the rounds'
    
def move(my_history, their_history, my_score, their_score):
    '''
    Collude = c or Betray = b
    Returns 'c' or 'b'. 
    '''
    #Always collude until they have betrayed us more than 25 times we will betray for the rest of the game.
    if 'b' in their_history or len(their_history)>25:
        return 'b'
    else:
        return 'c'      