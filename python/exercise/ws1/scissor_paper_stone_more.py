print("rock, paper, scissors, lizard, spock")
p1 = input("Player1:\n")
p2 = input("Player2:\n")

# Rock=0, paper=1, scissors=2, lizard=3, spock=4
# draw=0, win=1, lose=-1

# the value inside the matrix can be converted to the certain messages
# and it can help reduce the work of logical operation later
check = [[0, -1, 1, 1, -1],
         [1, 0, -1, -1, 1],
         [-1, 1, 0, 1, -1],
         [-1, 1, -1, 0, 1],
         [1, -1, 1, -1, 0]]
l = {"rock": 0,
     "paper": 1,
     "scissors": 2,
     "lizard": 3,
     "spock": 4}
    
a, b = l[p1], l[p2]

if check[a][b]==1:
    print("Player 1 wins")
elif check[a][b]==-1:
    print("Player 2 wins")
else:
    print("Draw")