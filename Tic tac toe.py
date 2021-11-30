l1 = []
for i in range(0,9,1):
    l1.append('NULL')
print(l1)

Player1 = int(0)#chances played
Player2 = int(0) #chances played

isPlayer1isX = True; #For future Update
isPlayer2isX = False; #for Future Update

Score_of_each = 12345
"""
winning_values = [0,0,0,0,0,0,0,0,0]
blocking_values =[0,0,0,0,0,0,0,0,0]
winning__probablity = [0,0,0,0,0,0,0,0,0]
"""
numberofBlank = l1.count("NULL")

#list l1 store the data
"""
Blank Space ='NULL'
X = 1
O = 0
"""

def showGameBoard():
    print("\n**************************\n")
    for i in range(0,9,1):
        print(l1[i],"\t",end = '');
        if((i+1)%3 == 0):
            print('\n')
    print("\n**************************\n")
showGameBoard()
possible_blocking_indexes = 125
#Player 1
def acceptInputForPlayer1():
    global Player1
    print("Player 1 Chance")
    choice = int(input("Enter Position of X from 1 to 9: "))
    if choice>=1 and choice<=9 and l1[choice-1] == 'NULL':
        l1[choice-1] = "X"
        Player1 = Player1+1
        print("Marked Sucessfully")
        showGameBoard()        
    else:
        print("Plz Give valid Input position ")
        acceptInputForPlayer1()

#Player 2
def acceptInputForPlayer2():
    global Player2
    print("Player 2 Chance")
    choice = int(input("Enter Position of 0 from 1 to 9: "))
    if choice>=1 and choice<=9 and l1[choice-1] == 'NULL':
        l1[choice-1] = "0"
        Player2  = Player2+1
        print("Marked Sucessfully")
        showGameBoard()        
    else:
        print("Plz Give valid Input position ")
        acceptInputForPlayer2()
a= 123
b = 123
def posssibleMoveGenerator(s):
    global possible_blocking_indexes
    possible_blocking_indexes = list()
    numberofBlank = l1.count("NULL")
    print(l1.count("NULL"))
    global a
    a= [list(l1) for x in range(numberofBlank)]
    """
    for i in range(numberofBlank):
        for j in range(9):
            a[i][j] = l1[j]
    """
    i=0
    for j in range(9):
        if (i<numberofBlank):
            if(a[i][j] == "NULL"):
                a[i][j] = s
                possible_blocking_indexes.append(j)
                i = i+1
        else:
            if(not i<numberofBlank):
                break
                
    for i in range(numberofBlank):
        for j in range(9):
            print(a[i][j] ,end =' ')
        print('\n')

    


def give_winning_index(temp):
    maximun = 0
    index = 'NULL'
    global a
    winning_index = [(0,1,2) , (3,4,5) , (6,7,8) , (0,4,8) ,(2,4,6) , (0,3,6) , (1,4,7) , (2,5,8)]
    numberofBlank = l1.count("NULL")
    m = list(a[temp])
    for ind in winning_index:
        score = 0
        for j in ind:
            if(m[j] == 'X'):
                score = score+1
        if(score == 3):
            print("winning at index: ",a[temp])
            return 60
    return 0

def give_blocking_index(temp):
    global possible_blocking_indexes
    print("Possible_Blocking_Indexes: ",possible_blocking_indexes)
    global a
    score = 0
    m = list(a[temp])
    winning_index = [(0,1,2) , (3,4,5) , (6,7,8) , (0,4,8) ,(2,4,6) , (0,3,6) , (1,4,7) , (2,5,8)]
    for j in winning_index:
        score = 0
        score2 = 0
        if(possible_blocking_indexes[temp] in j):
            #print(j)
            for i in j:
                if(m[i]=="0"):
                    score = score+1
                if(m[i]== "X"):
                    score2 = score2+1
        if(score == 2 and score2 == 1):
            return 50
    return 0
                
    
def winning_chances(temp,s):
    global possible_blocking_indexes
    winning_index = [(0,1,2) , (3,4,5) , (6,7,8) , (0,4,8) ,(2,4,6) , (0,3,6) , (1,4,7) , (2,5,8)]
    m = list(a[temp])
    master_chances = 0
    for j in winning_index:
        score = 0
        score2 = 0
        if(possible_blocking_indexes[temp] in j):
            for i in j:
                if(m[i] =="NULL"):
                    score = score+1
                if(m[i] == "0" or m[i] == "X"):
                    score2 = score2+1
        if(score == 3 or (score == 2 and score2 == 1)):
            master_chances +=1

    print("Master Chances : ",master_chances,"Temp = ",temp)
    return master_chances

def get_weightes_play():
    global l1
    global a
    numberofBlank = l1.count("NULL")
    max_values = [0,0,0,0,0,0,0,0,0]
    for i in range(numberofBlank):
        max_values[i] = give_winning_index(i)+winning_chances(i,"X")+give_blocking_index(i)
        print(give_blocking_index(i))    
    print( a[  max_values.index(max(max_values))  ] )
    l1 = a[max_values.index(max(max_values))]
    showGameBoard()
def check_winner():
    winning_index = [(0,1,2) , (3,4,5) , (6,7,8) , (0,4,8) ,(2,4,6) , (0,3,6) , (1,4,7) , (2,5,8)]
    global l1
    score = 0
    for i in winning_index:
        score = 0 
        for j in i:
            if(l1[j] == "X"):
                score = score+1
        if(score == 3):
            print("\n\n\nX is winner...")
            exit(0)
    for i in winning_index:
        score = 0 
        for j in i:
            if(l1[j] == "0"):
                score = score+1
        if(score == 3):
            print("\n\n\n0 is winner...")
            exit(0)


def main():
    #acceptInputForPlayer1()    #1  Add this if u want to let computer play first s
    #posssibleMoveGenerator('X')
    #get_weightes_play()
        
    #check_winner()

    acceptInputForPlayer2()    #2
    check_winner()

    posssibleMoveGenerator('X')#3
    get_weightes_play() 
    check_winner()

    acceptInputForPlayer2()    #4
    check_winner()

    posssibleMoveGenerator('X')#5
    get_weightes_play()
    check_winner()

    acceptInputForPlayer2()    #6
    check_winner()

    posssibleMoveGenerator('X')#7
    get_weightes_play()
    check_winner()

    acceptInputForPlayer2()    #8
    check_winner()

    posssibleMoveGenerator('X')#9
    get_weightes_play()
    check_winner()

    acceptInputForPlayer2()    #Remove if u want computer to play first
    check_winner()             #remove if u want computer to play first 

    
    print("\n\n********* Draw ********** \n\n")

main()

