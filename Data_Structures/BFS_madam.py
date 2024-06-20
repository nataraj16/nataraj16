graph={
    5 : [3,7],
    3 : [2,4],
    7 : [8],
    2 : [],
    4 : [8],
    8 : []
}
bfs_visited=[]
queue=[]

def BFS(bfs_visited,graph,node):
    bfs_visited.append(node)
    queue.append(node)
    while queue:
        front=queue.pop(0) #since it is queue add at end and delete from front, if it only pop() instead of pop(0),
        #then it will behave as stack and useful for DFS traversal.
        print(front,end=' ')
        for neighbours in graph[front]:
            if neighbours not in bfs_visited:
                bfs_visited.append(neighbours)
                queue.append(neighbours)

dfs_visited=[]
stack=[]

visited=set()#to keep track of visited nodes and acts as stack that does not allow duplicates

def DFS_madam_algo(visited,graph,node):
    if node not in visited:
        print(node,end=' ')
        visited.add(node) #here set is adding intgers as strings so i used int(node) in next line
        for neighbour in graph[int(node)]:
            DFS_madam_algo(visited, graph, neighbour)

print("DFS with Recurrsive Function:",end=' ')
DFS_madam_algo(visited,graph,'5')

def DFS(def_visited,graph,node):
    def_visited.append(node)
    stack.append(node)
    while stack:
        front=stack.pop()
        print(front,end=' ')
        for neighbours in graph[front]:
            if neighbours not in def_visited:
                def_visited.append(neighbours)
                stack.append(neighbours)

print("\nBFS Traversal: ",end=' ')
BFS(bfs_visited,graph,5)
print("\nDFS Traversal: ",end=' ')
DFS(dfs_visited,graph,5)