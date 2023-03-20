import time
import copy
import networkx as nx
import matplotlib.pyplot as plt

# constraint graph with unary and binary constraints

def space():
    print(" ".ljust(40, "_"))
    print("\n")


def sleep():
    time.sleep(1)


def print_list(inn):
    for k in inn:
        print(k)


print("Welcome".center(50, "-"))

# 1     define no of variables N_V
n = int(input("\n\nNo of variables: "))

sleep()

# 2     variable names
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
         "J", "K", "L", "M", "N", "O", "P", "Q", "R",
         "S", "T", "U", "V", "W", "X", "Y", "Z"]

var_names = []
for i in range(n):
    if alpha[i] not in var_names:
        var_names.append(alpha[i])

print("\n\nVariables are: ")
print_list(var_names)
space()
sleep()


# 3     domain for each variable
domain = []

for i in range(len(var_names)):
    temp = "Domain for " + var_names[i] + ": "
    domain_temp = list(input(temp))
    domain.append(domain_temp)

print("\nDomain for respective variables are: ")
print_list(domain)
space()
sleep()

# 4     unary constraints number
n_unary = int(input("Number of unary constraints: "))

# 5     unary constraints addition
print("Write unary constraints like\n<var> <op> <constant>")
unary = []
for i in range(n_unary):
    print(i+1, end="->  ")
    temp = str(input(""))
    unary.append(temp.upper())
sleep()

print("\nYour unary constraint list is: ")
print_list(unary)

space()
sleep()

# we have stored unary constraints
# now we need to adjust domain according to that

domain_temp = copy.deepcopy(domain)
no_of_nodes_unary = 0
for i in unary:

    x = i[0]  # var name
    y = i[2]  # operator
    z = i[4]  # constant

    ele_index = var_names.index(x)  # index of variable in variable list

    domain_ele = domain[ele_index]  # domain of variable

    for k in domain_ele:
        # define <, >, == and !=

        if y == "<":
            if int(k) >= int(z):
                print("Modified domain of", x, "removed", k)
                domain_temp[ele_index].remove(k)
                no_of_nodes_unary += 1
            else:
                no_of_nodes_unary += 1
        elif y == ">":
            if int(k) <= int(z):
                print("Modified domain of", x, "removed", k)
                domain_temp[ele_index].remove(k)
                no_of_nodes_unary += 1
            else:
                no_of_nodes_unary += 1
        elif y == "=":
            if int(k) != int(z):
                print("Modified domain of", x, "removed", k)
                domain_temp[ele_index].remove(k)
                no_of_nodes_unary += 1
            else:
                no_of_nodes_unary += 1
        elif y == "!":
            if int(k) == int(z):
                print("Modified domain of", x, "removed", k)
                domain_temp[ele_index].remove(k)
                no_of_nodes_unary += 1
            else:
                no_of_nodes_unary += 1
        else:
            print("no change to domain of", x)
    domain = copy.deepcopy(domain_temp)
    print("\nTotal Number of nodes visited: (unary) ", no_of_nodes_unary)
    print("")
    sleep()
    sleep()

space()
sleep()

print("Variable names and their respective domains:")

print("\nVariables")
print_list(var_names)

sleep()

print("\nDomains")
print_list(domain_temp)

space()
sleep()

# 6     binary constraints

n_binary = int(input("Number of binary constraints: "))

# 7     binary constraints addition

print("Write binary constraints like\n<var1> <rel op> <var2> <op> <constant>")
binary = []
for i in range(n_binary):
    print(i+1, end="->  ")
    temp = str(input(""))
    binary.append(temp.upper())
sleep()

print("\nYour binary constraint list is: ")
print_list(binary)

space()
sleep()

# we have stored unary constraints
# now we need to adjust domain according to that

domain_temp = copy.deepcopy(domain)
no_of_nodes_binary = 0

for i in binary:
    x = i[0]  # var name 1
    y_rel = i[2]  # rel operator
    y = i[4]  # var 2
    y_op = i[6]  # op
    z = i[8]  # constant

    ele_index_1 = var_names.index(x)  # index of variable 1 in variable list
    ele_index_2 = var_names.index(y)  # index of variable 2 in variable list

    domain_ele_1 = domain[ele_index_1]  # domain of variable 1
    domain_ele_2 = domain[ele_index_2]  # domain of variable 2

    for k in domain_ele_1:
        # define <, >, == and !=

        if y_rel == "<":
            for l in domain_ele_2:
                if y_op == "+":
                    if int(k) >= int(l)+int(z):
                        print("Modified domain of", x, "removed", k)
                        domain_temp[ele_index_1].remove(k)
                        no_of_nodes_binary += 1
                        break
                    else:
                        no_of_nodes_binary += 1

                elif y_op == "-":
                    if int(k) >= int(l)-int(z):
                        print("Modified domain of", x, "removed", k)
                        domain_temp[ele_index_1].remove(k)
                        no_of_nodes_binary += 1
                        break
                    else:
                        no_of_nodes_binary += 1
                        

        elif y_rel == ">":
            for l in domain_ele_2:
                if y_op == "+":
                    if int(k) <= int(l)+int(z):
                        print("Modified domain of", x, "removed", k)
                        domain_temp[ele_index_1].remove(k)
                        no_of_nodes_binary += 1
                        break
                    else:
                        no_of_nodes_binary += 1
                        
                elif y_op == "-":
                    if int(k) <= int(l)-int(z):
                        print("Modified domain of", x, "removed", k)
                        domain_temp[ele_index_1].remove(k)
                        no_of_nodes_binary += 1
                        break
                    else:
                        no_of_nodes_binary += 1
                        
        elif y_rel == "=":
            for l in domain_ele_2:
                if y_op == "+":
                    if int(k) != int(l)+int(z):
                        print("Modified domain of", x, "removed", k)
                        domain_temp[ele_index_1].remove(k)
                        no_of_nodes_binary += 1
                        break
                    else:
                        no_of_nodes_binary += 1
                        
                elif y_op == "-":
                    if int(k) != int(l)-int(z):
                        print("Modified domain of", x, "removed", k)
                        domain_temp[ele_index_1].remove(k)
                        break
                    else:
                        no_of_nodes_binary += 1
                        
        elif y_rel == "!":
            for l in domain_ele_2:
                if y_op == "+":
                    if int(k) == int(l)+int(z):
                        print("Modified domain of", x, "removed", k)
                        domain_temp[ele_index_1].remove(k)
                        no_of_nodes_binary += 1
                        break
                    else:
                        no_of_nodes_binary += 1
                        
                elif y_op == "-":
                    if int(k) == int(l)-int(z):
                        print("Modified domain of", x, "removed", k)
                        domain_temp[ele_index_1].remove(k)
                        no_of_nodes_binary += 1
                        break
                    else:
                        no_of_nodes_binary += 1
                        
        else:
            print("no change to domain of", x)
            no_of_nodes_binary += 1
                        
    domain = copy.deepcopy(domain_temp)
    print("\nTotal Number of nodes visited: (binary) ", no_of_nodes_binary)
    print("")
    sleep()
    sleep()

space()
sleep()

print("Variable names and their respective domains:", end="")

print("\nVariables")
print_list(var_names)

sleep()

print("\nDomains\n")
print_list(domain_temp)

G1 = nx.Graph()

for variable in var_names:
    G1.add_node(variable)

for constraint in binary:
    G1.add_edge(constraint[0], constraint[4])

pos = nx.random_layout(G1)

nx.draw(G1, pos, with_labels=True)
edge_labels = {(constraint[0], constraint[4]): str(constraint[4:]) for constraint in binary}
nx.draw_networkx_edge_labels(G1, pos, edge_labels=edge_labels, font_color='green')
plt.show()

nx.dfs_tree(G=G1,source="A",depth_limit=10)

successors = nx.dfs_successors(G=G1, source="A", depth_limit=10)
print("\n\nThe tree and its successors from node A would be: ", successors)

dfs = nx.dfs_edges(G=G1, source="A", depth_limit=10)

goal_node = "C"
iterations = 0
end = False

for i in dfs:
    print("Edge:", i)
    for j in i:
        if j == goal_node:
            print("\n\nFound goal")
            end = True
            break
        else:
            iterations += 1
    if end:
        break        
    
print("\nFinished with no of nodes searched: ", iterations)