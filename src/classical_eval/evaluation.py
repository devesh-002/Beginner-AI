

def return_score(l ,player):
    # Iterate through entire board and return score
    opp=-1
    if(player==-1):
        opp=1
    eval=0
    if l.count(player)==4:
        eval+=100
    elif l.count(player)==3 and l.count(0)==1:
        eval+=5
    elif l.count(player)==2 and l.count(0)==2:
        eval+=2
    if l.count(opp)==3 and l.count(0)==1:
        eval-=4
    return eval

def eval(board,player):
    eval_score=0
    columns = list(zip(*board))

    eval_score+=(columns[3].count(player))*6

    for r in range(6):
        arr=list(board[r])
        for c in range(3):
            eval_score+=return_score(arr[c:c+4],player)


    for c in range(6):
        arr=columns[c]
        for r in range(3):
            eval_score+=return_score(arr[r:r+4],player)

    for r in range(3,6):
        for c in range(3,6):
            eval_score+=return_score(list(board[r-i][c-i] for i in range(4)),player)
    
    for r in range(3,6):
        for c in range(3):
            eval_score+=return_score(list(board[r-i][c+i] for i in range(4)),player)
    
    return eval_score