def make_move(board,move,player):
    valid_moves=get_valid_moves(board)
    if valid_moves==[]:
        return True,None
    if move in valid_moves:
        board[move[0]][move[1]]=player
        if check_if_win(board,move[0],move[1],player)==True:
            return True,player
        return False,None
            
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

def get_valid_moves(board):
    l=[]
    for r in range(6):
        for c in range(6):
            if board[r][c]==0:
                l.append((r,c))
    return l