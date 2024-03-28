# Nim-
Nim game 
Code Structure 

~ The alphaBetaPruning function is the top-level function that calls the maxValue function to determine the best move for the computer player. 
It takes the current state of the game as input and returns the action that the computer player should take.

~ The maxValue function returns the maximum utility value for the computer player. 
It calls the minValue function to determine the utility value for the human player.

~The minValue function returns the minimum utility value for the human player. 
It calls the maxValue function to determine the utility value for the computer player.

~The terminalTest function checks whether the current state is a terminal state, i.e., whether one of the piles is empty.

~The utility function calculates the utility value of a terminal state.

~The final_score_utility function calculates the final score of the game based on the number of marbles left in each pile.

~The successor function generates the successor state of the game given a particular action.

~The play_game function implements the main game loop. It alternates between the human player and the computer player.

~The main function takes command line inputs for the initial state of the game (i.e., the number of red and blue marbles) 
and calls the play_game function with the initial state. 


**How to Run :**
-Install Python3 or check version of your python 
-Navigate to the right directory>
-Run the command -    python red_blue_nim.py <num-red> <num-blue> <first-player>
-Once the below prompts comes up to choose human move 
        Choose an action:
        Red
        Blue
        Type red or blue in any case. String is not case-sensitive.
-When its the computer's turn ,the move and the current state will be displayed on the terminal.
        For example             Computer's turn...
                                Computer picked red
                                Current state: 2 red marbles, 1 blue marbles
-Alternate between computer and human
-Once the game ends the winner and score will be displayed.
