from tabulate import tabulate

class Board:
    def __init__(self,N,super_queen):
        board = [[0 for i in range(N)] for i in range(N)]
        self.board = board
        self.super_queen = super_queen
    
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

    def remove_queen(self,row,col):
        self.board[row][col] = 0

    def is_valid(self,row,col):
        for i in range(len(self.board)):
            if self.board[i][col] == "Q":
                print(f'({i},{col}) is column conflicting')
                return False
        
        for i in range(len(self.board)):
            if self.board[row][i] == "Q":
                print(f'({row},{i}) is row conflicting')
                return False
        
        rows , column = row , col

        # Left diagonal (up)
        while rows >= 0 and column >= 0:
            if self.board[rows][column] == "Q":
                print(f'({rows},{column}) in left diagonal is conflicting')
                return False
            rows    -= 1
            column  -= 1

        # Right diagonal(up)
        
        rows , column = row , col
        while rows >= 0 and column < len(self.board):
            if self.board[rows][column] == "Q":
                print(f'({rows},{column}) in right diagonal is conflicting')
                return False
            rows   -= 1
            column += 1

        # Left diagonal (down)

        rows ,column = row,col
        while rows < len(self.board) and column >= 0:
            if self.board[rows][column] == "Q":
                print(f'({rows},{column}) in left diagonal is conflicting ')
                return False

            rows   += 1
            column -= 1

        # Right diagonal (down)

        rows , column = row,col
        while rows < len(self.board) and column < len(self.board):
            if self.board[rows][column] == "Q":
                print(f'({rows},{column}) in right diagonal is conflicting')
                return False
        
            rows   += 1
            column += 1

        if self.super_queen == "y":
                # Knight condition 
            possible_moves = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
            for (x,y) in possible_moves:
                x = x + row
                y = y + col

                if x>= 0 and y>= 0 and x < len(self.board) and y < len(self.board):
                    if self.board[x][y] == "Q":
                        print(f'({x},{y}) is knight conflicting')
                        return False

        return True

    def user_inp(self):
        flag = True
        r = "R"
        while flag and self.queen_counter() != len(self.board):
            inp = eval(input("Enter the cords (x,y) : "))
            #if inp != "":
            if inp:
                #inp = inp+"00"
                if (inp[0]) != "R":
                    x , y = int(inp[0]),int(inp[1])
                    if self.is_valid(x,y) == True:
                        self.place_queen(x,y)
                        self.print_board()
                        print()
                    else:
                        print("Not a valid spot ... ")
                        print()
                else:
                    x , y = int(inp[1]) , int(inp[2])
                    self.remove_queen(x,y)
                    self.print_board()
                    print()
            else:
                flag = False
        if self.queen_counter() == len(self.board):
            print("You have placed N Queens ")


    def instructions(self):
        print(f'An N Queen tester')
        self.print_board()
        print(f'Enter the coordinates where u want to place the queen as (x,y)')
        print('To remove a Queen type in cords with an extra argument r (x,y,r)')
        print()


    def queen_counter(self):
        count = 0
        for row in self.board:
            for item in row:
                if item == "Q":
                    count += 1
        return count
N = int(input("Enter size of NxN chess board: "))
super_queen = input("Do you want Super Queen rules (y/n): ").lower()
chess = Board(N,super_queen)
chess.instructions()
chess.user_inp()
