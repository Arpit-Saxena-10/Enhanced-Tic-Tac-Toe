
class board:
    def __init__(self,n):
        self.position = [[ 0 for _ in range(n)] for _ in range(n)]          # nxn matrix of move_size, 0 denotes empty cell
                                                                            # +ve number denotes player 1 moves, -ve for 2nd player
        self.turn = 1                                                       # turn = 1 implies its 1st player's turn,-1 for 2nd player
        self.length = n                                                     # length = 3 implies 3x3 tic toe board
    def make_move(self,x,y,move):               # move = -2 implies move of size 2 by 2nd player
                                                # make_move returns 1 if move is valid, else 0
        old_move_size,turn = self.position[x][y]
        if  abs(old_move_size) < abs(move):
            self.position[x][y] = (move)
            self.turn = -self.turn              # switching turn
            return 1
        else:
            return 0

    def check_win(self):    # returns 1 for 1st player win, -1 for 2nd player win, 0 for neither
        # checking horizontally
        for i in range(self.length):
            win_for_player_1,win_for_player_2 = True,True
            for j in range(self.length):
                if self.position[i][j]<= 0:
                    win_for_player_1 = False
                if self.position[i][j]>= 0:
                    win_for_player_2 = False
            if win_for_player_1:
                return 1
            if win_for_player_2:
                return-1
        # checking vertically
        for i in range(self.length):
            win_for_player_1,win_for_player_2 = True,True
            for j in range(self.length):
                if self.position[j][i]<= 0:
                    win_for_player_1 = False
                if self.position[j][i]>= 0:
                    win_for_player_2 = False
            if win_for_player_1:
                return 1
            if win_for_player_2:
                return-1
        # checking first diagonal
        win_for_player_1, win_for_player_2 = True, True
        for i in range(self.length):
            if self.position[i][i]<= 0:
                win_for_player_1 = False
            if self.position[i][i]>= 0:
                win_for_player_2 = False
        if win_for_player_1:
            return 1
        if win_for_player_2:
            return-1

        # checking 2nd diagonal
        win_for_player_1, win_for_player_2 = True, True
        for i in range(self.length):
            if self.position[i][self.length-1-i] <= 0:
                win_for_player_1 = False
            if self.position[i][self.length-1-i] >= 0:
                win_for_player_2 = False
        if win_for_player_1:
            return 1
        if win_for_player_2:
            return -1






