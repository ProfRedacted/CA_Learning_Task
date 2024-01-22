# CA_Learning_Task

This is a simulation of Elementary CA.<br>
Written by:<br>
Uy, Wesley King<br>
Corpuz, David Joshua<br>

Elementary cellular automata are one-dimensional, discrete mathematical models consisting of a line of cells, each with a binary state, and evolve through discrete time steps based on simple local rules. These rules, often represented by a binary number, determine the state transitions of each cell based on its current state and the states of its neighbors, leading to diverse and complex patterns emerging over time.

Steps:
1) Install pygame using "pip install pygame"
2) Run the program (Rules184.py)
3) Select the starting column by clicking any part of the column
4) Press Space to play the program

Features 
- Main Menu
- Custom rules
- pause and play the simulation by pressing the space bar
- reset the board to try out a new starting state by pressing "R" key
- randomly generate a starting state by pressing "G" key

The default configuration for an Elementary Cellular Automaton (CA) is defined as follows: <br>
CA = { L^1, (0, 1) , (pattern of L,C,R), Rules:{
                                               1) 111 -> 1,
                                               2) 110 -> 0,
                                               3) 101 -> 1,
                                               4) 100 -> 1,
                                               5) 011 -> 1,
                                               6) 010 -> 0,
                                               7) 001 -> 0,
                                               8) 000 -> 0 } 
                                               }