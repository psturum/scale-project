# Initializing scoreboards
# top_3 = [(560, "Lars"), (420, "Brian"), (300, "Anna")]
# worst_3 = [(120, "Lars"), (130, "Brian"), (140, "Anna")]

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


# load_score(top_3, (540, "Patrick"))
# load_score_1(worst_3, 141)
# print(worst_3)
# print(top_3)

 