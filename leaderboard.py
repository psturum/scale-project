#Check if board should be updated
def load_score(leader_board, score):
    for i in range(3):
        if score[0] > leader_board[i][0]:
            leader_board.insert(i, score)
            leader_board.pop()
            return

#Check if board should be updated
def load_score_1(leader_board, score):
    for i in range(3):
        if score[0] < leader_board[i][0]:
            leader_board.insert(i, score)
            leader_board.pop()
            return

 