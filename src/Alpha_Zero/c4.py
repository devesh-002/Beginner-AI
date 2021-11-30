import numpy as np
# This is the implementation of rules of Connect$4
def check_if_win(board_u,row,col,player_val):
    check=True
    for i in range(3):
        check=True
        for j in range(4):
            if board_u[row][i+j] != player_val:
                check=False
                break
        if check==True:
            return True
    if(check==True):
        return True
    check=True

    for i in range(3):
        check=True
        for j in range(4):
            if board_u[i+j][col] != player_val:
                check=False
                break
        if check==True:
            return True
    if(check==True):
        return True

    b_r=row-min(row,col)
    b_c=col-min(row,col)
    
    for i in range(3):
        if max(b_c+i,b_r+i)+4>6:
            break
        if board_u[b_r+i][b_c+i]==player_val and board_u[b_r+i+1][b_c+i+1]==player_val and board_u[b_r+i+2][b_c+i+2]==player_val and board_u[b_r+i+3][b_c+i+3]==player_val:
            return True
    b_r=row
    b_c=col
    while(True):
        if b_r == 0 or b_c == 5:
            break
        
        b_c=b_c+1
        b_r=b_r-1
        
    for i in range(3):
        if b_r+3+i>5 or b_c-3-i<0:
            break
        if board_u[b_r+i][b_c-i] == player_val and board_u[b_r+i+1][b_c-i-1] == player_val and board_u[b_r+i+2][b_c-i-2] == player_val and board_u[b_r+i+3][b_c-i-3] == player_val :
            return True
    return False

board_test=[
        ["--","--","--","--","--","--"],
        ["--","--","--","--","--","--"],
        ["--","--","--","--","--","--"],
        ["--","--","--","--","--","--"],
        ["--","--","--","--","--","--"],
        ["--","--","--","--","--","--"],
    ]
# Main class of playing, uses 2 players namely Alpha and Human
class Connect():
    
    def __init__(self) :
        super().__init__()
        self.board=[
        
        ["--","--","--","--","--","--"],
        ["--","--","--","--","--","--"],
        ["--","--","--","--","--","--"],
        ["--","--","--","--","--","--"],
        ["--","--","--","--","--","--"],
        ["--","--","--","--","--","--"]
        ]
        self.players=['A','H']
        self.current_player='A'

    def get_previous_player(self):
        if(self.current_player=='A'):
            return 'H'
        return 'A'
    def makeMove(self,move):
        valid_moves=self.get_valid_moves()
        if(len(valid_moves)==0):
            return True,None
        if move in valid_moves:
            row_c=move[0]
            col_c=move[1]
            self.board[row_c-1][col_c-1]=self.current_player

            check=  check_if_win(self.board,row_c-1,col_c-1,self.current_player)
            valid_moves=self.get_valid_moves()

            if(len(valid_moves)==0):
                return True,None
            elif(check==True):
                winner=self.current_player
            else:
                winner=None
            if self.current_player=='A':
                self.current_player='H'
            else :
                self.current_player='A'
            
            return check,winner
    def check_legal_move(self,x_cord,y_cord):
        x_cord=x_cord-1
        y_cord=y_cord-1
        if 0<=x_cord<=5 and 0<=y_cord<=5:
            if(self.board[x_cord][y_cord]=="--"):
                return True
        return False
    def get_valid_moves(self):
        l=[]
        for i in range(6):
            for j in range(6):
                if self.board[i][j]=="--":
                    l.append(tuple((i+1,j+1)))
        return l
    def get_current(self):
        return self.current_player
    def get_opponent(self):
        if self.current_player=='A':
            return 'H'
        return 'A'
    def set_game(self):
        self.board=board_test
        self.current_player='A'
        # print(board_test)
        
    def __repr__(self) :
            return (' '.join(map(str, self.board)))


