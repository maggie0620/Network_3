import re
file1 = open('D:/Network/Network 1.txt', 'r')
net1 = file1.read()

## 3-1
# Find one cut-point and one cut-edge (Net1)
split1 = re.split('\n', net1)
split1.remove('')
edge1 = []
for i in range(0,len(split1)):
    num1 = re.sub('\t','',split1[i])
    edge1.append(num1)

ind1 = []
outd1 = []
for j in range(0,len(edge1)):
    ind1.append(edge1[j][1])
    outd1.append(edge1[j][0])
    
mylist1 = []
for k in ind1:
    if k not in mylist1:
        mylist1.append(k)
for k in outd1:
    if k not in mylist1:
        mylist1.append(k)
#print(mylist1)                 

from collections import defaultdict

# Find one cut-point
node1 = mylist1
for r in range(0,len(node1)):
    # Create a copy of the original list
    current_node = node1.copy()
    
    # Remove one node
    removed_node = current_node.pop(r)
    #print("Removed node:", removed_node)
    #print("Current node:", current_node)  # 剩下的node
    
    # Remove all the edge includes removed node 
    result_lists = []
    for k in range(0,len(edge1)):
        copy_edge = edge1.copy()
        if removed_node in edge1[k]:
            removed_edge = copy_edge.pop(k)
            result_lists.append(removed_edge)
    
    # Get current edge
    current_edge = edge1.copy()
    for i in result_lists:
        current_edge.remove(i)
    #print("Current edge:", current_edge)    #剩下的edge

    # Check connectivity
    class Cut_node_graph:
        def __init__(self, nodes):
            self.graph = defaultdict(list)
            self.nodes = nodes
            
        def add_undict_edge(self, u, v):
            self.graph[u].append(v)
            self.graph[v].append(u)

        def DFS(self, v, visited):
            key = self.nodes.index(v)
            visited[key] = True
            for i in self.graph[v]:
                k = self.nodes.index(i)
                if not visited[k]:
                    self.DFS(self.nodes[k], visited)
    
        def connect(self):            
            visited = [False] * len(self.nodes)

            # Find a starting node to start DFS
            v = None
            for v in self.graph:
                if self.graph[v]:
                    start_node = v
                    break
        
            # Check if the graph is connected
            self.DFS(start_node, visited)
        
            # Check if all nodes are reachable
            if any(not visited[i] for i in range(0,len(visited))):
                return True

            return False

    cut_node = Cut_node_graph(current_node)
    for e in range(0,len(current_edge)):
        cut_node.add_undict_edge(current_edge[e][0],current_edge[e][1])
    
    if cut_node.connect():
        print(removed_node, "is a cut-point.")
        break


# Find one cut-edge
for r in range(0,len(edge1)):
    # Create a copy of the original list
    current_edge = edge1.copy()
    
    # Remove one edge
    removed_edge = current_edge.pop(r)
    #print("Removed edge:", removed_edge)
    #print("Current edge:", current_edge)  # 剩下的edge (node不變)

    # Check connectivity
    class Cut_edge_graph:
        def __init__(self, nodes):
            self.graph = defaultdict(list)
            self.nodes = nodes
            
        def add_undict_edge(self, u, v):
            self.graph[u].append(v)
            self.graph[v].append(u)

        def DFS(self, v, visited):
            key = self.nodes.index(v)
            visited[key] = True
            for i in self.graph[v]:
                k = self.nodes.index(i)
                if not visited[k]:
                    self.DFS(self.nodes[k], visited)
    
        def connect(self):            
            visited = [False] * len(self.nodes)

            # Find a starting node to start DFS
            v = None
            for v in self.graph:
                if self.graph[v]:
                    start_node = v
                    break
        
            # Check if the graph is connected
            self.DFS(start_node, visited)
        
            # Check if all nodes are reachable
            if any(not visited[i] for i in range(0,len(visited))):
                return True

            return False

    cut_edge = Cut_edge_graph(mylist1)
    for e in range(0,len(current_edge)):
        cut_edge.add_undict_edge(current_edge[e][0],current_edge[e][1])
    
    if cut_edge.connect():
        print(removed_edge, "is a cut-edge.")
        break

## 3-2
# Identify two spanning trees of network 1
class Spanning_tree:
    def __init__(self, nodes):
        self.graph = defaultdict(list)
        self.nodes = nodes
            
    def add_undict_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, v, visited, path):
        key = self.nodes.index(v)
        visited[key] = True
        for i in self.graph[v]:
            k = self.nodes.index(i)
            if not visited[k]:                
                path.append(v+i)  # Store the direct edge in the path
                self.DFS(self.nodes[k], visited, path)
        return path
    
    def span_DFS(self):
        visited = [False] * len(self.nodes)

        # Run DFS
        for node in self.nodes:
            if not visited[self.nodes.index(node)]:
                path = []
                DFS_result = self.DFS(node, visited, path) # Save path in variable (DFS_result)
                #subgraphs.append(path)
                print("DFS spanning tree edge list:", path)                
            # Check if all nodes are reachable
            if all(visited[i] for i in range(0,len(visited))):
                break
        return DFS_result
    
    def BFS(self, start, visited):
        #visited = [False] * len(self.nodes)
        alist = []
        key = self.nodes.index(start)
        visited[key] = True
        alist.append(start)
        
        edge_visit = []
        while alist:
            v = alist.pop()
            for i in self.graph[v]:
                k = self.nodes.index(i)
                if not visited[k]:
                    visited[k] = True
                    alist.append(i)
                    edge_visit.append(v+i)
        print("BFS spanning tree edge list:", edge_visit)
        return edge_visit

    def span_BFS(self):
        visited = [False] * len(self.nodes)
        # Run BFS
        for node in self.nodes:
            if not visited[self.nodes.index(node)]:
                BFS_result = self.BFS(node, visited)   # Save edge_visit in variable (BFS_result)
                # Check if all nodes are reachable
                if all(visited[i] for i in range(0, len(visited))):
                    break
        return BFS_result

tree = Spanning_tree(mylist1)
for e in range(0,len(edge1)):
    tree.add_undict_edge(edge1[e][0],edge1[e][1])

# DFS spanning tree
span_tree1 = tree.span_DFS()
#print(span_tree1)

# BFS spanning tree
span_tree2 = tree.span_BFS()
#print(span_tree2)

## 3-3
# Do following operations on the two identified trees
# (1) Edge complementation
comple = []
for node_in_span1 in mylist1:
    for node_in_span2 in mylist1:
        if node_in_span1 != node_in_span2:
            comple.append(node_in_span1 + node_in_span2)

new_comple1 = []
for element in comple:
    if element not in span_tree1:
        new_comple1.append(element)
#print(new_comple1)

new_comple2 = []
for element in comple:
    if element not in span_tree2:
        new_comple2.append(element)
#print(new_comple2)

print("(1) Edge complementation (span1): \nV =", mylist1, "\nE =", new_comple1)
print("Edge complementation (span2): \nV =", mylist1, "\nE =", new_comple2)

# (2) Join
# Define a dictionary to map characters to their replacements
char_mapping = {}
for x in range(len(mylist1)):
    char_mapping[mylist1[x]] = str(x+1)
#print(char_mapping)

# Create a new list with the substitutions
new_span = []
for string in span_tree1:
    name = char_mapping.get(string[0]),char_mapping.get(string[1])
    changed = "".join(name)
    new_span.append(changed)
#print(new_span)

new_list = []
for node in mylist1:
    name = char_mapping.get(node[0])
    changed = "".join(name)
    new_list.append(changed)
#print(new_list)

join_node = new_list.copy()
for element in mylist1:
    join_node.append(element)
print("(2) Join: \nV =", join_node)

join_edge = []
for node_in_span1 in mylist1:
    for node_in_span2 in new_list:
        edge = node_in_span1 + node_in_span2
        join_edge.append(edge)
#print(join_edge)

for i in new_span:
    join_edge.append(i)
for k in span_tree2:
    join_edge.append(k)
print("E =", join_edge)

# (3) Union
# Remove same elements
merge = span_tree1.copy()
merge.extend(span_tree2)

new_merge = []
for x in range(0,len(merge)):
    if merge[x] in new_merge:
        continue
    else:
        new_merge.append(merge[x])  # span1 U span2
print("(3) Union: \nV =", mylist1)
print("E =", new_merge)

# (4) Intersection
span_inter = []
for same in span_tree1:
    if same in span_tree2:
        span_inter.append(same)

inter_nodes = []
for edge in span_inter:
    for position in edge:
        if position not in inter_nodes:
            inter_nodes.append(position)

print("(4) Intersection: \nV =", inter_nodes)
print("E =", span_inter)

# (5) Difference: (DFS - BFS) and (BFS - DFS)
# DFS - BFS 
span1_diff = []
for edge in span_tree1:
    if edge not in span_inter:
        span1_diff.append(edge)
#print(span1_diff)

print("(5) Difference (DFS - BFS): \nV =", mylist1)
print("E =", span1_diff)

# BFS - DFS
span2_diff = []
for edge in span_tree2:
    if edge not in span_inter:
        span2_diff.append(edge)
#print(span2_diff)

print("Difference (BFS - DFS): \nV =", mylist1)
print("E =", span2_diff)
