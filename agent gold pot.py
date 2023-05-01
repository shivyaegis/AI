import time

#initialise room
def room_create(n):
    list1 = []
    list2 = []
    for i in range(n):
        list1.append(0)
    for j in range(n):
        list2.append(list1.copy())
    return list2


#print room
def print_room(rm):
    
    print("\nYour room is: \n")
    for i in range(len(rm)):
        print("-----"*len(rm))
        print(" | ", end="")
        for j in range(len(rm)):
            print(rm[i][j], end=" | ")
        print("\n")
 
    
def agent(locx, locy):
    global x, y
    room[locx][locy] += 1
    print("\n\nYour agent is at point: ", locx, ",", locy)
    x = locx
    y = locy


def path():
    global n, room
    time.sleep(1)
    run = True
    for i in range(n):
        while run:
            if(i%2==0):
                x = 0
                while(x<n) and run:
                    agent(i,x)
                    print_room(room)
                    time.sleep(1)
                    x += 1
                    if(room[i][x-1]!=100):
                        room[i][x-1] += 1
                    else:
                        run = found_gold(room)
            else:
                y = n-1
                while(y>=0) and run:
                    agent(i,y)
                    print_room(room)
                    time.sleep(1)
                    y -= 1
                    if(room[i][y+1]!=100):
                        room[i][y+1] += 1
                    else:
                        run = found_gold(room)


def found_gold(matrice):
    global x, y
    gold = 100
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] == gold:
                print("Gold found at: ","(", x, ",", y, ")")
                return False
    return True



room = []
print("\n\npreknowledge:- \n\n1 and 3 -> position of agent")
print("0 -> node not visited")
print("2 -> node visited")
print("99 -> gold location\n")
time.sleep(1)
print("----"*10)

n = int(input("Number of rows & columns: "))
bat = n/2
room = room_create(n)
print_room(room)
print("----"*10)

gold_locx = int(input("Enter gold x location:"))
gold_locy = int(input("Enter gold y location:"))
room[gold_locx][gold_locy] = 99

x, y = 0, 0
print_room(room)
path()



