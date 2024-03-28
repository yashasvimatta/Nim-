# Nim-
Nim game 

In this game, players interact with two distinct piles of marbles, one red and the other blue. During each player's turn, they must choose one of the piles and remove either one or two marbles, provided that the pile contains enough marbles to do so. The game has a standard version and a misère version, which differ based on the conditions for losing or winning. In the standard version, a player loses if they are forced to play a turn when one of the marble piles is empty. Conversely, in the misère version, a player wins under these circumstances. The score—either lost or won—is calculated based on the remaining marbles: two points for each red marble and three points for each blue marble. For instance, if it's the computer player's turn and there are no red marbles and three blue marbles left, the computer would lose 9 points in the standard version, or win 9 points in the misère version.Implemented the standard version


**How to Run :**

1. Install Python3 or check version of your python 


2. Navigate to the right directory

3. Run the command -    python red_blue_nim.py <num-red> <num-blue> <first-player>

4. Once the below prompts comes up to choose human move 
        Choose an action:
        Red
        Blue
        Type red or blue in any case. String is not case-sensitive.

5. When its the computer's turn ,the move and the current state will be displayed on the terminal.
        For example             Computer's turn...
                                Computer picked red
                                Current state: 2 red marbles, 1 blue marbles
6. Alternate between computer and human
7. Once the game ends the winner and score will be displayed.
