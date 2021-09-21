#Check if board should be updated
from visualization import load_leaderboard_pic


def load_score(leader_board, score):
    for i in range(3):
        if score[0] > leader_board[i][0]:
            leader_board.insert(i, score)
            leader_board.pop()
            load_leaderboard_pic("visualization_pics/top_3_højest.png", leader_board, "temporary_pics/top_3.png")
            return

#Check if board should be updated
def load_score_1(leader_board, score):
    for i in range(3):
        if score[0] < leader_board[i][0]:
            leader_board.insert(i, score)
            leader_board.pop()
            load_leaderboard_pic("visualization_pics/top_3_lavest.png", leader_board, "temporary_pics/worst_3.png")
            return

 