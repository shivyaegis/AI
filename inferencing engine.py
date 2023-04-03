import time

def space():
    print("\n\n")
    print("-".center(50,"-"))
    print('\n\n')
    time.sleep(1)


def no_of_variables():
    move = True
    while move:
        n = int(input("\nEnter no of variables (between 3 and 27) : "))
        if 3 < n < 27:
            move = False 
    space()
    return n


def variable_names(loop):
    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
         "J", "K", "L", "M", "N", "O", "P", "Q", "R",
         "S", "T", "U", "V", "W", "X", "Y", "Z"]
    chosen = []
    for i in range(loop):
        chosen.append(alpha[i])
    print("\n\nYour chosen alphabets are: ", chosen)
    space()
    return chosen

space()
print("Welcome".center(50,"_"))

n = no_of_variables()

alphabets = variable_names(n)

# input rules given by syntax
# IF <condition> THEN <variable name>

# condition is written as <var1> AND <var2> OR NOT <var3>

rules = []
for i in range(3):
    print("\n\nEnter rule number ",i, "in the form :\n<condition>\n:",end="")
    sentence = input("")
    rules.append(sentence)

space()
print(rules)
space()

for i in range(len(alphabets)):
    globals()[alphabets[i]] = None

for i in range(2):
    var = input("Enter variable: ")
    var = var.upper()
    if var in alphabets:
        val = input("Enter value of variable: ")
        if val == "True":
            val = True
        else:
            val = False
        globals()[var] = val
        
    else:
        print("wrong variable name, program may misbehave")

space()
print("Your variable names, values given, and the conditions are: \n")
print(alphabets)
print("\n")
for i in range(len(alphabets)):
    print(alphabets[i], "has value:  ", end="")
    print(globals()[alphabets[i]])
print("\n")
print(rules)

space()


rules_set = ""
actions = []


if eval(rules[0]):
    print("Rule 1 works expression evaluation of ", rules[0], "returns True")

    rules_set += rules[0]
    rules_set = rules_set.split("  ")
    print(rules_set)

    for i in range(0,len(rules_set),2):
        print("running rule set 1:",i)
        if len(rules_set) - i > 1:
            st = rules_set[i] + " " + rules_set[i+1] + " " + rules_set[i+2]
            if eval("st") == True:
                print("Rule ", st, "is getting triggered")
                break
        else:
            continue


if eval(rules[1]):
    print("Rule 2 works expression evaluation of ", rules[1], "returns True")


if eval(rules[2]):
    print("Rule 3 works expression evaluation of ", rules[2], "returns True")

# print(rules[0].index("IF"))