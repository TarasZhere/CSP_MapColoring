'''
Taras Zherebetskyy.
Constraint Satisfacion Problems

The program, composed by a class Node that creates objects stored in an array alled graph.
the nodes are connected by pointers 

X set of variables: nodes rapresented ny numbers {x0, x1, x2, x3, x4, x5, x6}
D set of domains: Colors in this case {"Red", "Green", "Blue"}
C set of constraints {"will be defined at the end, when problem is solved"}
'''

class Node:
    def __init__(self, num):
        self.node = num #hold the number of the node
        self.color = "" #hold the color 
        self.vertex = [] # hold all the verteces
    
    def set_connection(self, vertex): # the function set a pointer to the Node it is connected to and viceversa
        for i in vertex:
            self.vertex.append(i)
            i.vertex.append(self)

    def print(self): #just a print function
        print(f'''
        Node: {self.node}
        Color: \t{self.color}
        Verteces:\t ''', end='')
        for i in self.vertex: print(i.node,":", i.color, ",", end=" ")

def print_graph(graph): #print function
    for i in graph:
        i.print()

def print_constraint(graph):
    print("\n", "C = {", end=" ")
    for i in graph:
        print(f"<{i.node},{i.color}>", end=" ")
    print("}")

def collision(node):
    for ver in node.vertex: #loop through all verteces and return true if there are collision
        if node.color == ver.color: return True
    return False

def compile_colors(graph, colors):
    for node in graph: # Looping throught each node
        i = 0 #setting the node with color 0
        node.color = colors[i] 
        while collision(node):
            i += 1
            if i > 2: 
                print("This graph can't be solved")
                node.color = "No color"
                return
            node.color = colors[i]

'''
      MAIN STARTS HERE
'''
colors = ["Red", "Green", "Blue"] #colors that are used
graph = [] #this list will contain each node in the graph
j = 0 # j will number each node

#this loop will append all the nodes inside the array
for i in range(6):
    graph.append(Node(j))
    j += 1

# setting the connections. the function "set_connection" will connect a pointer to the node it is conected and viceversa
graph[0].set_connection([graph[1], graph[2]])
graph[2].set_connection([graph[1], graph[3], graph[5], graph[4]])
graph[1].set_connection([graph[3]])
graph[3].set_connection([graph[5]])
graph[4].set_connection([graph[5]])

'''
# this node is used to check if the function can recognize if a graph is not solvable 
# uncomment for test.
graph.append(Node(6))
graph[6].set_connection([graph[4], graph[5], graph[2]])
'''

'''
# uncomment the next for the change the structure of the graph adding another node.
# in this case it works becasue the node 6 doesn't collide with other colors
graph.append(Node(6))
graph[6].set_connection([graph[4], graph[2], graph[0]])
'''

compile_colors(graph, colors)
print_graph(graph)
print_constraint(graph)
