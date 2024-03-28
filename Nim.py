#References
#https://classes.engr.oregonstate.edu/eecs/spring2019/cs331/slides/AdversarialSearch1.2pp.pdf
#https://crystal.uta.edu/~gopikrishnav/classes/common/4308_5360/slides/Game_Search.pdf
#https://crystal.uta.edu/~gopikrishnav/classes/common/4308_5360/slides/alpha_beta.pdf

import copy
import sys 

def alphaBetaPruning(state):             
    v_red = maxValue(successor(state, 'pick_red'), alpha, beta)
    v_blue = maxValue(successor(state, 'pick_blue'), alpha, beta)
    if v_red > v_blue:                                                 # compares utility value of each move and determine which action to take
        return 'pick_red'
    else:
        return 'pick_blue'

def maxValue(state, alpha, beta):
    if terminalTest(state):
        return utility(state)
    v = float('-inf')
    for a, s in [('pick_red', successor(state, 'pick_red')), ('pick_blue', successor(state, 'pick_blue'))]:
        v = max(v, minValue(s, alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def minValue(state, alpha, beta):
    if terminalTest(state):
        return utility(state)
    v = float('inf')
    for a, s in [('pick_red', successor(state, 'pick_red')), ('pick_blue', successor(state, 'pick_blue'))]:
        v = min(v, maxValue(s, alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v
def terminalTest(state):                                        #to check whether the current state is a terminal state or not. if either pile is empty it is terminal 
    if state['red'] == 0 or state['blue']==0:
        return True
    else:
        return False
    
def utility(state):                                             # This utility function assigns negative value when the human player empties one of the piles. 
    if state['red'] == 0 or state['blue'] == 0:                 # This prevents the computer to make moves that help the human from emptying a pile and ending the game
        utility_value = 3 * state['blue'] + 2 * state['red']
        if state['current_player'] == 'human':
            return -utility_value
        else:
            return utility_value
        
def final_score_utility(state):
    final_score = 3 * state['blue'] + 2 * state['red']
    return final_score

def successor(state, action):                                          # gives the successor state on taking a particular action
    new_state = copy.deepcopy(state)                                    # created copy of the original state 
    if state['red'] > 0 and action == 'pick_red':
        new_state['red'] -= 1
    if state['blue'] > 0 and action == 'pick_blue':
        new_state['blue'] -= 1
    if state['current_player'] == 'human':
        new_state['current_player'] = 'computer'
    else:
        new_state['current_player'] = 'human'
    return new_state

def play_game(state):
    while not terminalTest(state):                                                              # gameplay loop
        print(f"Current state: {state['red']} red marbles, {state['blue']} blue marbles")
        if state['current_player'] == 'human':
            move = input("Choose an action:\n  Red\n  Blue\n")
            if move.casefold() == "red" and state['red'] > 0:
                state['red'] -= 1
                state['current_player'] = 'computer'
            elif move.casefold() == "blue" and state['blue'] > 0:
                state['blue'] -= 1
                state['current_player'] = 'computer'
            else:
                print("Invalid move, try again.")
        else:
            print("Computer's turn...")                                                         # Calls alphabetapruning to determine the best move for it 
            action = alphaBetaPruning(state)
            if action == 'pick_blue':
                print("Computer picked blue")
            else:
                print("Computer picked red")
            state = successor(state, action)            
            state['current_player'] = 'human'
    score = utility(state)                                                      # calculated the final score by which player wins 
    if state['current_player'] == 'human':
        print("Human wins!")
    elif state['current_player'] == 'computer':
        print("Computer wins!")
    else:
        print("It's a tie!")
    print(f"Final score of win: {abs(score)}")                                  # calculates the final score of the win

if __name__ == "__main__":
    first_player = "human"
    num_red = int(sys.argv[1])                                          # take command line inputs
    num_blue = int(sys.argv[2])                                         # take command line inputs
    first_player = sys.argv[3] if len(sys.argv) > 3 else 'computer'     # take command line inputs
    negative_infinity = float('-inf')
    positive_infinity = float('inf')
    alpha = negative_infinity                                    # initialse alpha and beta as infinite and -infinte respectively                            
    beta = positive_infinity
    state = {"red":num_red ,"blue": num_blue, "current_player": first_player}
    play_game(state)
