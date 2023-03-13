import time
import copy


def space(): # space function to clean code output
    print("\n")
    print("____"*15)
    print("\n")
    time.sleep(0.1)


def matrix(): # create 6 by 6 matrix
    list1 = []
    list2 = []
    for i in range(6):
        list1.append("0")
    for j in range(6):
        list2.append(copy.deepcopy(list1))
    return list2


def print_matrix(table): # print the matrix cleanly
    print(("----"*15).center(40,"-"))
    for i in range(len(table)):
        print("|", end=" ")
        for j in range(len(table)):
            print(table[i][j].center(5," "), end="  |  ")
            # time.sleep(0.2)
        print("")
        time.sleep(0.1)
        print(("----"*15).center(40,"-"))


def add_elements(table): # add Pits, Wu, Gold, Breeze, Stench, which will build our environment (not known to agent yet)
    print("Filling elements in matrix:-")
    mat[5][0] = "Start"
    table[0][0], table[3][1], table[3][5], table[5][3] = "Pit","Pit","Pit","Pit"
    table[2][4] = "Wu"
    table[1][3] = "Gold"

    print_matrix(table)
    space()

    # fill the Breeze elements around the pit
    print("Filling breeze around pits in matrix:-")
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == "Pit":

                if i==0 and j==0:
                    table[i][j+1] = "Br"
                    table[i+1][j] = "Br"
                elif i==5 and j==5:
                    table[i][j-1] = "Br"
                    table[i+1][j] = "Br"

                elif i==5 and j==0:
                    table[i-1][j] = "Br"
                    table[i][j+1] = "Br"

                elif i==5 and j==5:
                    table[i-1][j] = "Br"
                    table[i][j-1] = "Br"

                elif j==0:
                    table[i][j+1] = "Br"
                    table[i-1][j] = "Br"
                    table[i+1][j] = "Br"
                elif j==5:
                    table[i][j-1] = "Br"
                    table[i-1][j] = "Br"
                    table[i+1][j] = "Br"

                elif i==0:
                    table[i][j+1] = "Br"
                    table[i][j-1] = "Br"
                    table[i+1][j] = "Br"
                elif i==5:
                    table[i][j-1] = "Br"
                    table[i-1][j] = "Br"
                    table[i][j+1] = "Br"
                else:
                    table[i][j-1] = "Br"
                    table[i][j+1] = "Br"
                    table[i-1][j] = "Br"
                    table[i+1][j] = "Br"
    print_matrix(table)
    space()

    # fill stench around Wumpus
    print("Filling stench (+breeze) in matrix:-")
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == "Wu":
                if i>0:
                    if table[i-1][j] == "0":
                        table[i-1][j] = "S"
                    else:
                        table[i-1][j] = table[i-1][j] + "S"
                if i<5:
                    if table[i+1][j] == "0":
                        table[i+1][j] = "S"
                    else:
                        table[i+1][j] = table[i+1][j] + "S"
                if j>0:
                    if table[i][j-1] == "0":
                        table[i][j-1] = "S"
                    else:
                        table[i][j-1] = table[i][j-1] + "S"
                if j<5:
                    if table[i][j+1] == "0":
                        table[i][j+1] = "S"
                    else:
                        table[i][j+1] = table[i][j+1] + "S"
    print_matrix(table)


def classifier(st): # classify string as Pit Near, Wumpus Near, Gold or safe
    if st=="Br":
        return "PN"
    elif st=="BrS":
        return "WN"
    elif st=="S":
        return "WN"
    elif st=="Gold":
        return "G"
    elif st=="0":
        return "S"
    else:
        return "S"


def check_in(row, column): # check if element exists in not known list and if it does add to known and temp
    exists = False
    for i in not_known:
        if i[0] == row and i[1] == column:
            # print("\n\nThe ",row, column,"is in unknown")
            exists = True
            known.append(i)
            temp.append(i)
            not_known.remove(i)
            # print_known_and_unknown()
            break


def dont_check_in(row, column): # same as above but if it exists dont add to temp so we wont check it and get its neighbours
    exists = False
    for i in not_known:
        if i[0] == row and i[1] == column:
            # print("\n\nThe ",row, column,"is in unknown")
            exists = True
            known.append(i)
            not_known.remove(i)
            # print_known_and_unknown()
            break


def in_path(ele):
    for i in path.split(sep=" > "):
        if ele==i:
            return True
    return False


def print_known_and_unknown(): # if u want to print not known and known list
    print("\n\nKnown: ", known)
    print("\n\nUnnown: ", not_known)
    space()


def check_neighbours(table, x, y): # check the neighbours classify them and check their neighbours

    global counter
    global path
    counter += 1

    # can be safe(S), wumpus neighbour(WN), pit in neighbour(PN), goal(G)

    print("On loop: ", counter, " your environment is: ")
    print_matrix(environment)
    space()

    if y > 0:

        environment[x][y-1] = classifier(table[x][y-1])
        if environment[x][y-1] == "PN" or environment[x][y-1] == "WN":
            dont_check_in(x,y-1)
        else:
            check_in(x,y-1)
            if not in_path("S"+str(x)+str(y-1)):
                path = path + (" > S"+str(x)+str(y-1))

    if y < 5:

        environment[x][y+1] = classifier(table[x][y+1])
        if environment[x][y+1] == "PN" or environment[x][y+1] == "WN":
            dont_check_in(x,y+1)
        else:
            check_in(x,y+1)
            if not in_path("S"+str(x)+str(y+1)):
                path = path + (" > S"+str(x)+str(y+1))

    if x > 0:

        environment[x-1][y] = classifier(table[x-1][y])
        if environment[x-1][y] == "PN" or environment[x-1][y] == "WN":
            dont_check_in(x-1,y)
        else:
            check_in(x-1,y)
            if not in_path("S"+str(x-1)+str(y)):
                path = path + (" > S"+str(x-1)+str(y))

    if x < 5:

        environment[x+1][y] = classifier(table[x+1][y])
        if environment[x+1][y] == "PN" or environment[x+1][y] == "WN":
            dont_check_in(x+1,y)
        else:
            check_in(x+1,y)
            if not in_path("S"+str(x+1)+str(y)):
                path = path + (" > S"+str(x+1)+str(y))

    temp.pop(0)
    # print(temp)
    if temp != [] and not_known != []:
        check_neighbours(mat,temp[0][0],temp[0][1])
        

def start():
    global path

    print_matrix(mat)
    space()
    add_elements(mat)
    space()

    print("Your environment is: ")
    environment[5][0] = "Start"
    print_matrix(environment)
    space()

    # now what are the states not known?
    # and what are the states known?
    # we also need to check if it will reach the gold

    
    for i in range(len(environment)):
        for j in range(len(environment)):
            not_known.append([i,j])

    not_known.remove([5,0])
    known.append([5,0])

    check_neighbours(table=mat,x=5,y=0)
    print("\n\n\nYour final environment is: ")
    print_matrix(environment)

    result = False
    for i in range(len(environment)):
        for j in range(len(environment)):
            if environment[i][j] == "G":
                result = True
                break
    
    if not result:
        print("No path to gold and no result possible")
    else:
        print("Safe path to goal exists")
        index = path.index(gold_at)
        path = path[0:index+3]

# initialise variables


mat = matrix() # matrix we will give 
environment = matrix() # environment matrix (keeps updating as agent discovers)
not_known = [] # unknown nodes
known = [] # known or visited nodes
temp = [[5,0]] # temp stack that stores next node to visit
counter = 0
gold_at = "S13"
path = "S50" # path we need to take to find gold
start()

print(path)
'''
The problem is defined as follows:-

Recall the Wumpus World discussed. The knowledge base was represented using a matrix that
stores information about what the agent knows about individual rooms (i.e. the state of each room).
Actually, you will need two matrices. The first one (call it the environment) stores information about the
actual facts about the room (i.e. whether it contains a Wumpus, or a pit, or breeze, or stench, or breeze
and stench, or gold, or nothing). The agent does not have access to this information. The agent has to
start with no knowledge of the rooms and then, when it reaches a particular room, It can consult the
environment matrix to find the necessary information and update its own knowledge base. Develop the
module that will perform the (a) reasoning (b) taking the decision about the next room to be visited.
Assume that the agent is completely averse to risk taking. So, if it finds that all rooms in NEWS directions
are unsafe then it will backtrack.
'''