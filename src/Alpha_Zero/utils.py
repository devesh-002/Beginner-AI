import numpy as np
from c4 import *
# This is just a utility file used in most of the code
def return_player_val(player_name):
    if player_name=='A':
        return -1
    elif player_name=='H':
        return 1
    return 0

def make_board_array(board_n ):
    
    total=[]
    for i in range(6):
            temp=[]    
            for j in range(6):
                    if(board_n[i][j]=="--"):
                            temp.append(0.0)
                    elif (board_n[i][j]=="A"):
                            temp.append(-1.0)
                    else :
                            temp.append(1.0)
            total.append(temp)
    total=np.array(total)
    return total
