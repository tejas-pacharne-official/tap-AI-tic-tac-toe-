#TAP
current_board = [2,0,0,0,1,0,0,0,0]
print("""Plz Put\nX as 1 \nO as 2  \n0 as bank""")
temp = 0
def accept_input():
    global current_board
    temp =0
    for i in range(0,3,1):
        for j in range(0,3,1):
            print("Enter Curren Board ",i,j)
            current_board[temp] = int(input(":"))
            temp = temp+1
def check_valid_board():
    global current_board
    if(abs(current_board.count(1) - current_board.count(2)) in [0,1]):
        return True
    else:
        return False
def index_finder():
    global current_board
    index = current_board[0]*3 ** 8 + current_board[1]*3 ** 7 + current_board[2]*3 ** 6 + current_board[3]*3 ** 5 +current_board[4]*3 ** 4 +current_board[5]*3 ** 3 + current_board[6]*3 ** 2 + current_board[7]*3 ** 1 + current_board[8]*3 ** 0
    print(index)

def main():
    #accept_input()
    if(check_valid_board()):
        index_finder()
    
main()
