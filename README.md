# CA_Learning_Task

This is a simulation of Elementary CA of Rule 184.

Steps:
1) Install pygame using "pip install pygame"
2) Run the program
3) Select the starting column by clicking any part of the column
4) Press Space to play the program and Space to pause again
5) Lastly, press "R" to reset the board to try out a new starting state
   
Addionally, you can press "G" to randomly generate a starting state.

This is the definition for the Elementary CA of rule 184

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
