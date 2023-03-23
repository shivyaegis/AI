import time
import matplotlib.pyplot as plt
import networkx as nx

def space():
    print(" ".ljust(40, "_"))
    print("\n")
    time.sleep(3)

def print_list(inn):
    for k in inn:
        print(k)

def graph():
    edges = [("Midas", "Gold"), ("Midas", "Daughter"), ("Midas", "Angel"), 
         ("Gold", "Excited"), ("Gold", "Devastated"), 
         ("Daughter", "Gold"), 
         ("Angel", "Help"), ("Angel", "Wish"), 
         ("Wish", "Gold"), 
         ("Excited", "Daughter"),
         ("Devastated", "Angel")]
    
    print("\n\nYour edges are: ")
    print(edges)
    space()

    G = nx.DiGraph()
    G.add_edges_from(edges)
    
    plt.figure(figsize =(10, 7))
    pos = nx.circular_layout(G)
    nx.draw_networkx(G, pos, with_labels = True ,node_color ='yellow')

    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels={
                    ("Midas", "Gold") : "had", 
                    ("Midas", "Daughter") : "had and loved", 
                    ("Midas", "Angel") : "helped", 
                    ("Gold", "Excited") : "made midas", 
                    ("Gold", "Devastated") : "made midas", 
                    ("Daughter", "Gold") : "turned into", 
                    ("Angel", "Help") : "needed", 
                    ("Angel", "Wish") : "granted", 
                    ("Wish", "Gold") : "turned everything into", 
                    ("Excited", "Daughter") : "midas hugged",
                    ("Devastated", "Angel") : "Asked to take wish away"
                    },
        font_color='black'
    )
    plt.axis('off')
    plt.show()

print("Welcome".center(50, "-"))


graph()

# add nodes here
#        0         1       2           3       4       5       6          7
nodes = ['midas', 'gold', 'daughter', 'angel','help', 'wish', 'excited', 'devastated']

# add sequence wise messages
messages = ["had","had and loved","needed","helped","granted",
            "turned everything into","made midas","hugged","turned into",
            "made midas","asked to take wish away from"]

# sequence
timing = [[0,1],[0,2],[3,4],[0,3],[3,5],[5,1],[1,6],[6,2],[2,1],[1,7],[7,3]]

for i in range(len(timing)):
    x = nodes[timing[i][0]]
    y = nodes[timing[i][1]]

    text = messages[i]

    print("Time:", i, " ",x, text, y)
    space()

graph()


'''
Consider the following short story:
Once upon a time, there was a Greek King, Midas.
Midas was very rich and had lots of Gold. Midas had a daughter, whom he loved a lot.
One day, Midas found an angel in need of help. Midas helped her and in return she agreed to grant
a wish.
Midas wished that everything he touched would turn into gold. Midas' wish was granted.
On Midas' way home, Midas touched rocks and plants and they turned into gold.
As Midas reached home, in excitement Midas' hugged his daughter, who turned into gold.
Midas was devastated and Midas had learnt his lesson. Upon learning the lesson, Midas asked the
angel to take the wish away.
Create a semantic net, manually, for the above story. Enter the semantic net in your program. Now
write functions to answer the following queries:
a) whom did Midas find one day?
b) why did Midas hug his daughter?
'''