board=['-'for i in range(9)]
def DisplayBoard():
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("|",board[6],"|",board[7],"|",board[8],"|")

player1="X"
player2="O"
def condition(player):
    conditions=[
    [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]
]
    for check in conditions:
        if board[check[0]]==player and board[check[1]]==player and board[check[2]]==player:
            return 1
    else:
        return 0
        
def StartGame():
    DisplayBoard()
    while True:
        while True:
            player1_option=int(input(f"{player1},Enter your position:"))
            if player1_option not in [int(i) for i in range(1,10)]:
                print("Please enter [1-9]")
                continue
            if board[player1_option-1]=="-":
                board[player1_option-1]=player1
                DisplayBoard()
                if condition(player1):
                    return"Winner:{X}"
                break
            else:
                print("This place is not empty.")
            if len([i for i in board if i=='-'])==0:
               return"Match draw" 
        while True:
            player2_option=int(input(f"{player2},Enter your position:"))
            if player2_option not in [int(i) for i in range(1,10)]:
                print("Please enter [1-9]")
                continue
            if board[player2_option-1]=="-":
                board[player2_option-1]=player2
                DisplayBoard()
                if condition(player2):
                    return"Winner:{O}"
                break
            else:
                print("This place is not empty.")
            if len([i for i in board if i=='-'])==0:
               return"Match draw" 

print(StartGame())
while True:
    play_again=input("Do you want to play again[yes/no]:")
    if play_again in "yesYes":
        board=['-'for i in range(9)]
        print(StartGame())
    else:
        exit()
