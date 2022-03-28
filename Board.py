

class Board():

    def __init__(self):
        super().__init__()



    def draw_board(self, top_board, middle_board, bottom_board):

        print(*top_board)
        print(*middle_board)
        print(*bottom_board)

    def assign_spaces(self, top_board, middle_board, bottom_board):
        zero = top_board[0]
        one = top_board[3]
        two = top_board[5]
        three = top_board[0]
        four = middle_board[3]
        five = middle_board[5]
        six = bottom_board[0]
        seven = bottom_board[3]
        eight = bottom_board[5]

        return zero, one, two, three, four, five, six, seven, eight


