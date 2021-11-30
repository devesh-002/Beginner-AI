# from MCT.classical_eval.minimax import makeMove
from evaluation import *
import math
from copy import deepcopy
import numpy as np
from util import *
def board_to_numpy(board):
    l=[]
    for r in range(6):
        l_util=[]
        for c in range(6):
            if (board[r][c]=="--"):
                l_util.append(0)
            elif (board[r][c]=="A"):
                l_util.append(1)
            else:
                l_util.append(-1)
        l.append(l_util)
    return np.asarray(l)
def minimax(board :list,alpha,beta,player,depth,maximiser,check,winner):

    if check==True:
        if winner==-1:
            return math.inf
        elif winner==1:
            return -math.inf
        else : return 0
    valid_moves=get_valid_moves(board)
    
    if valid_moves==[]:
        return 0
    
    if depth==0:
        return eval(board,-1)
    if maximiser:
        best_eval=-math.inf

        for move in valid_moves:
            temp=board.copy()
            check_temp,winner_temp=make_move(temp,move,-1)
            max_val=minimax(temp,alpha,beta,player,depth-1,not maximiser,check_temp,winner_temp)
            best_eval=max(best_eval,max_val)
            alpha=max(alpha,best_eval)
            # board[move[0]-1][move[1]-1]="--"
            if alpha>=beta:
                break
        return best_eval
    
    else:
        best_eval=math.inf
        for move in valid_moves:
            temp=board.copy()
            check_temp,winner_temp=make_move(temp,move,1)
            min_val=minimax(temp,alpha,beta,-1,depth-1,not maximiser,check_temp,winner_temp)
            best_eval=min(best_eval,min_val)
            beta=min(beta,min_val)
            # board[move[0]-1][move[1]-1]="--"
            if alpha>=beta:
                break
        return best_eval
def minimax_util(board,player,depth):
    valid_moves=get_valid_moves(board)

    best_val=-math.inf
    best_move=()

    for move in valid_moves:
        temp=board.copy()
        
        # print(board)
        # print(make_move(temp,move,player))
        check,winner=make_move(temp,move,player)
        move_val=minimax(temp,-math.inf,math.inf,player,depth-1,True,check,winner)
        if move_val>best_val:
            best_val=move_val
            best_move=move
    return best_move
    

# def main():
#     while True:
#         if game.get_current()==-1:
#             move=minimax_util(game.board,-1,3)
#             x_cord,y_cord=move     
#             x_cord+=1;y_cord+=1               

#         else:
#             while(True):
#                 x_cord=int(input("Enter x coordinate"))
#                 y_cord=int(input("Enter y coordinate"))
#                 check=game.check_legal_move(x_cord,y_cord)
#                 if check==True:
#                     break
#         check,winner=game.makeMove((x_cord+1,y_cord+1))
#         print(game.board)
#         if check==True:
#                 print(game)
#                 if winner==None:
#                     print("It was a draw, will try harder next time")
#                 else:
#                     print("Winnter is ",winner)
#                 exit()

# def makeMove_util(move,valid_moves,board,player):
        
#         if(len(valid_moves)==0):
#             return True,None
#         if move in valid_moves:
#             row_c=move[0]
#             col_c=move[1]
#             board[row_c-1][col_c-1]=player
#         # else:
#         #     print("Move is not Valid")
#             # print(player)
#             check=  check_if_win(board,row_c-1,col_c-1,player)

#             if(len(valid_moves)==0):
#                 return True,None
#             elif(check==True):
#                 winner=player
#             else:
#                 winner=None
#             if player==-1:
#                 player=1
#             else :
#                 player=-1
            
#             return check,winner
# if __name__ == '__main__':
#     main()
