from tabulate import tabulate

class Board:
    def __init__(self,N):
        board = [[0 for i in range(N)] for i in range(N)]
        self.board = board
    
    def print_board(self):
        i = 0
        visual_board = [row.copy() for row in self.board]

        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if visual_board[row][col] == 0:
                    visual_board[row][col] = "-"

        for row in visual_board:
            row.insert(0,i)
            i += 1
        visual_board.insert(0,[" "]+[i for i in range(len(self.board))])

        print(tabulate(visual_board,tablefmt="grid"))

    def place_queen(self,row,col):
        self.board[row][col] = "Q"


    def is_valid(self,row,col):
        for i in range(len(self.board)):
            if self.board[i][col] == "Q":
                print(f'({i},{col}) is conflicting')
                return False
        
        for i in range(len(self.board)):
            if self.board[row][i] == "Q":
                print(f'({row},{i}) is conflicting')
                return False
        
        rows , column = row , col

        # Left diagonal (up)
        while rows >= 0 and column >= 0:
            if self.board[rows][column] == "Q":
                print(f'({rows},{column}) is conflicting')
                return False
            rows    -= 1
            column  -= 1

        # Right diagonal(up)
        
        rows , column = row , col
        while rows >= 0 and column < len(self.board):
            if self.board[rows][column] == "Q":
                print(f'({rows},{column}) is conflicting')
                return False
            rows   -= 1
            column += 1

        # Left diagonal (down)

        rows ,column = row,col
        while rows < len(self.board) and column >= 0:
            if self.board[rows][column] == "Q":
                print(f'({rows},{column}) is conflicting ')
                return False

            rows   += 1
            column -= 1

        # Right diagonal (down)

        rows , column = row,col
        while rows < len(self.board) and column < len(self.board):
            if self.board[rows][column] == "Q":
                print(f'({rows},{column}) is conflicting')
                return False
        
            rows   += 1
            column += 1

        return True

    def user_inp(self):
        flag = True
        while flag and self.queen_counter() != len(self.board):
            inp = input("Enter the cords (x,y) : ")
            if inp != "":
                x , y = int(inp[0]),int(inp[2])
                if self.is_valid(x,y) == True:
                    self.place_queen(x,y)
                    self.print_board()
                    print()
                else:
                    print("Not a valid spot ... ")
                    print()
            else:
                flag = False
        if self.queen_counter() == len(self.board):
            print("You have placed N Queens ")

            
    def instructions(self):
        print(f'An N Queen tester')
        self.print_board()
        print(f'Enter the coordinates where u want to place the queen as (x,y)')
        print()

    def queen_counter(self):
        count = 0
        for row in self.board:
            for item in row:
                if item == "Q":
                    count += 1
        return count
N = int(input("Enter size of NxN chess board: "))
chess = Board(N)
chess.instructions()
chess.user_inp()
