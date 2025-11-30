import random
start= int(input("Enter 1 to start Tic Tac Toe: "))
if start== 1:
    computer = ["❌", "⭕"]                                                                                    #| [x o]
    computer_choice = random.choice(computer)                                                                   #| randomly chioce 
    grid = []                                                                                                   #| [ ]
    for i in range(3):                                                                                          #| i= 0 1 2
        row = []                                                                                                #| row =[]
        for j in range(3):                                                                                      #| j = 0 1 2
            row.append('')                                                                                      #| row = ['']['']['']
        grid.append(row)                                                                                        #| grid =[['']['']['']]
    score = 0                                                                                                   #| score = 0
    def display():                                                                                  
        for row in grid:
            print(row)
    def check_matches():
        global score
        new_score=0
        for col in range(3):
            if grid[0][col] != '' and grid[0][col] == grid[1][col] == grid[2][col]:  # check vertically
                
                new_score += 1
        if grid[0][0] != '' and grid[0][0] == grid[1][1] == grid[2][2]:              # check Diagonal
                new_score += 1
        if grid[0][0]!='' and grid[0][0]== grid[0][1]== grid[0][2]:            
                new_score+=1
        if grid[1][0]!='' and grid[1][0]== grid[1][1]== grid[1][2]: 
                new_score+=1
        score=new_score
    def user_move():
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if grid[row][col] == '':
            letter = input("Enter a letter (X or O): ").upper()
            grid[row][col] = letter
            check_matches() 
        else:
            print("Try again.")
            user_move() 
    def computer_move():
        while True:
            row=random.randint(0,2)
            col=random.randint(0,2)
            if grid[row][col] == '':  
                print(f"Computer plays at row {row}, column {col}")
                grid[row][col] = computer_choice 
                check_matches() 
                return
    for move in range(9):                                                                       # | move= 0 1 2 3 4 5 6 7 8
        display()
        if move % 2 == 0:                                                                       #| move= 0 %2=0     player turn
            print("Player's turn:")
            user_move()
        else:                                                                                   #| move =1     computer turn
            print("Computer's turn:")
            computer_move()
    print("Final score:", score)

else:
     print("Invalid")
     





