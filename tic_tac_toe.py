class TicTacToe(object):
    def __init__(self):
        self.tic_tac_toe_matrix =[[str(row)+str(col) for col in range(3)] \
        for row in range(3)]
        self.print_tic_tac_toe_matrix()
        self.cells_filled = 0
    
    def print_tic_tac_toe_matrix(self):
        print '\n\n'
        for row in range(0,3):
            print '|'.join([ele if ele in ['X', 'O'] else '-' for ele in row])

    def evaluate_input(self, input, player):
        if len(input.split()) != 2:
            return False, False, True #player_won, Match tied, invalid_ip
        
        row_of_input = int(input.split()[0])
        col_of_input = int(input.split()[1])

        if self.tic_tac_toe_matrix[row_of_input][col_of_input] in ['X', 'O']:
            return False, False, True #player_won, Match tied, invalid_ip

        self.tic_tac_toe_matrix[row_of_input][col_of_input] = player
        
        if self.check_row(input, player) or self.check_col(input, player) or \
         self.check_diagonal(input, player):
            self.print_tic_tac_toe_matrix()
            return True, False, False #player_won, Match tied, invalid_ip
        else:
            self.print_tic_tac_toe_matrix()
            self.cells_filled += 1
            if self.cells_filled == 9:
                print 'Match tied!'
                return False, True, False #player_won, Match tied, invalid_ip
            return False, False, False #player_won, Match tied, invalid_ip


    def check_col(self, input, player):
        row_of_input = int(input.split()[0])
        no_of_consecutives = 0
        for col in range(3):
            if self.tic_tac_toe_matrix[row_of_input][col] == player:
                no_of_consecutives += 1
                continue
            else:
                break
        if no_of_consecutives == 3:
            print 'ret t from check_row'
            return True
        else:
            return False


    def check_row(self, input, player):
        col_of_input = int(input.split()[1])
        no_of_consecutives = 0
        for row in range(3):
            if self.tic_tac_toe_matrix[row][col_of_input] == player:
                no_of_consecutives += 1
                continue
            else:
                break
        if no_of_consecutives == 3:
            print 'ret t from check_col'
            return True

    def check_diagonal(self, input, player):
        row_of_input = int(input.split()[0])
        col_of_input = int(input.split()[1])
        if row_of_input == col_of_input or abs(row_of_input - col_of_input) == 2:
            if self.tic_tac_toe_matrix[0][0] == self.tic_tac_toe_matrix[1][1] == \
            self.tic_tac_toe_matrix[2][2]:
                print 'ret t from check_dia 1'
                return True
            elif self.tic_tac_toe_matrix[0][2] == self.tic_tac_toe_matrix[1][1] == \
            self.tic_tac_toe_matrix[2][0]:
                print 'ret t from check_dia 2'
                return True
        return False


    def insert_x_or_o(self, row, col, x_or_o):
        row_col_string = str(row) + str(col)
        self.available_positions_board_dict.pop(row_col_string)
        print 'avail pos = ', self.available_positions_board_dict.keys()
        self.tic_tac_toe_board[row][col] = x_or_o
        self.print_tic_tac_toe()


    def check_board_is_full(self):
        if not self.available_positions_board_dict.keys():
            print 'Board is full'
            return False
        else:
            return True


    def insert_O_in_board(self): #use this function if single player is playing
        first_avail_pos = self.available_positions_board_dict.keys()[0]
        self.insert_x_or_o(int(first_avail_pos[0]), int(first_avail_pos[0]), 'O')


if __name__ == '__main__':
    t = TicTacToe()
    player_x = 1 #player_x will always start the game
    
    while(True):
        if player_x:
            player_x_input = raw_input('Player X enter your choice as rowNumber<space>colNumber: ')
            player_x = 0
            player_won, match_tied, invalid_ip = t.evaluate_input(player_x_input, 'X')
            
            if player_won:
                print 'Congratulations Player X! You Won'
                break
            elif match_tied:
                print 'That is a tie'
                break
            elif invalid_ip:
                player_x = 1
                print 'Invalid Input'
        else:
            player_o_input = raw_input('Player O enter your choice as rowNumber<space>colNumber: ')
            player_x = 1
            player_won, match_tied, invalid_ip = t.evaluate_input(player_o_input, 'O')
            
            if player_won:
                print 'Congratulations Player O! You Won'
                break
            elif match_tied:
                print 'That is a tie'
                break
            elif invalid_ip:
                player_x = 0
                print 'Invalid Input'
