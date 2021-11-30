#Prim's Algorithm

#This is the adjacency matrix representing edges and vertices of the graph
graph = [[0,28,0,0,0,10,0],
    [28,0,16,0,0,0,14],
    [0,16,0,12,0,0,0],
    [0,0,12,0,22,0,18],
    [0,0,0,22,0,25,24],
    [10,0,0,0,25,0,0],
    [0,14,0,18,24,0,0]]
    
 #this is the number of vertices in the graph   
v = 7

 #This is used to check the selected edge vertices   
selected = [0] * v
# Used to initailize the number of edges as 0
no_edge = 0
#used to set the 0th index as true
selected[0] = True

# This is used to print for edge and weight
print("Edge : Weight\n")
#this is a while loop where it keeps looping if the edge_no is less than v - 1
while (no_edge < v - 1):
  
  #initializing my variables  
    minimum = float("inf")
    x = 0
    y = 0
    # looping through every vertex in the graph
    for i in range(v):
        if selected[i]:
        # If the vertices is in selected and there is an edge
            for j in range(v):
                if ((not selected[j]) and graph[i][j]):  
                    # not in selected and there is an edge
                    if minimum > graph[i][j]:
                        minimum = graph[i][j]
                        x = i
                        y = j
    print(str(x+1) + "--" + str(y+1) + ":" + str(graph[x][y]))
    # this is used to set the visited vertex as true
    selected[y] = True
    # this is used to increase the number of edges
    no_edge += 1
