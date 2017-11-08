from random import *
from copy import deepcopy
from datetime import datetime

"""
NOTE THIS IS FOR AN UNWEIGHTED GRAPH UNDIRECTED
TODO:
write analogous code for weighted directed graph
in this code would be good to have the adjacency matrix as a class variable
also might want to keep the node list sorted by adj number as go as much as possible
maybe not but its an idea
(maybe not because the incidence number could change as edges are added)
so if it is rare for an edge to be added after a vertex has been added then should
keep the node list sorted by adj number as add them
otherwise dont and just sort before calling the distance metric

TODO:
-test remove edge and remove node methods more
-write creat adj_matrix method
    - can first write one that just adds rows and cols at end
    -then later write one that inserts the empty rows and cols at the right place
-then write distance method
1.
Make set of graphs and then for each graph on that list manually come up
with some near-isomorphic graphs  (with some verts or edges removed or different edge types)
2.
then try out my new distance metric!
should give 0 dist if exactly isomorphic
(though if have metric that gives say always a dist <0.15 if isomorphic,)
(could offset our distance metric just to have this hold, or could not have this hold)
if has 2 edges removed should have greater dist than graph with 1 edge removed
^^^NOTE the above conditions could change depending by what graphs are near-isomorphic
in the context of our problem
My guess is that the definition of near-isomorphism for these web pages is not very strict at all


-find what distances the dist metric gives for a graph w n nodes w
     - 1 vert removed
     - 2 verts removed (this set includes the first)
     - 2 verts removed (this set doesn't include the first)
     - 3 verts removed (including the first two)
     - different 3 verts removed
     - an edge removed
     - 2 edges removed
     - 3 edges removed
     - 1 edge of a different type
     - 2 edges of a different type
     NOTE:  might want to sum the edge_weight_dist_metric and edge_type_dist_metric
     to give a total dist metric
     NOTE: could weight the two differently, see which weights work

"""


"""
1. empty graph
2. for num of verts uniformly pick one permutation of the verts
which is written p_0,p_1,p_2,p_3...p_(n-1)
3. for each i in range(n-1):
    add edge between [p_i and p_(i-1)]
4. choose uniformly m-n+1 edges to add from set of ((possible edges among verts) - (edges already included))
5. add them

2. just figured out how
start with list of all verts
list = [vert for vert in graph.nodes]
ordered_list = []
for k in range(n-1,0,-1):
   #n wont actually run will go up to n-1
   #indexing for me will start at 0
   idx_of_vert_to_add = randint(0,k)
   vert_to_add = list[idx_of_vert_to_add]
   ordered_list.append(vert_to_add)
   list.remove(vert_to_add)

4. how?
could make all possible pairs of verts then remove edges already in edge set
but waaaaay too inefficient
so how?
[this may not be uniform but i will improve upon it]
first, pick the start vert out of the sets of verts
may not be uniform so we need to weight the start vert choices
based on how many possible end verts they have (may be different for each start
vert since some edge already included and these could not be possible end verts
)
then once that is done properly, choose an end vert out of the set of possible end verts
for that start vert
will work through a couple examples by hand to get the weighting right but this should
work

ok, worked this out:
1. make list of possible_start_verts and for each start_vert possible end verts
to avoid duplicates make the start vert the smaller one
2. make probability of choosing each start vert = (#possible end_verts for that start vert)/(sum(over possible start verts)(# end verts for each)))
3. choose each start vert with its probability
4. once have done that choose from its end verts with uniform probability (do this with randint)

   
"""

"""
TODO:
test!

way to optimize:
there is repeated work in constructing the hashmap start_vert_to_end_verts
over and over
should modify code so that it is only constructed once and then has stuff
deleted as we go rather than re constructed so many times
"""


class Graph(object):
    def __init__(self,nodes=None):
        if nodes == None:
            nodes = []
        self.nodes = nodes
        self.num_edges = 0

    def removeNode(self,node):
        #go to node.adj
        #for each adj node:
        #remove node from adj node.adj
        if node in self.nodes:
            for itm in node.adj:
                itm.removeAdjNode(node)
            self.nodes.remove(node)
        #####TEST######

    def removeEdge(self,node1,node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.removeAdjNode(node2)
            node2.removeAdjNode(node1)
        #####TEST######

    def getNodes(self):
        return self.nodes

    def addNode(self,data):
        new_node = GraphNode(data)
        if new_node not in self.nodes:
            self.nodes.append(new_node)

    def addNodeByNode(self,node):
        if node not in self.nodes:
            self.nodes.append(node)

    def addEdgeByNode(self,edge):
        #edge is a set of 2 instances of the GraphNode class
        [vert1,vert2] = edge
        #print("vert1 in self.nodes")
        #print(vert1 in self.nodes)
        #print("vert2 in self.nodes")
        #print(vert2 in self.nodes)
        vert1.addAdjNode(vert2)
        vert2.addAdjNode(vert1)
        self.num_edges += 1

    def constructAdjMatrix(self):
        self.sortNodesByIncidenceNumber()
        adj_matrix = [[0 for node1 in self.nodes] for node2 in self.nodes]
        for i in range(len(self.nodes)-1):
            for j in range(i,len(self.nodes)):
                if self.nodes[j] in self.nodes[i].getAdj():
                    adj_matrix[i][j] = 1
                    adj_matrix[j][i] = 1
        return adj_matrix

    #def constructIncidenceNumberToNodes(self):
        #grouping  the nodes by incidence number and creating a hashmap
        
    def printNodesAndIncNumbers(self):
        ret = ""
        for node in self.nodes:
            ret += "Node Data: " + str(node.data) + "\n"
            ret += "Incidence Number: " + str(node.getNumAdj()) + "\n"
        print(ret)
            
    #def addEdgeByNodeData():
    def printNodesDataToAdjSet(self):
        node_data_to_adj_node_data = dict()
        for node in self.nodes:
            key = node.data
            adj_nodes = node.getAdj()
            val = []
            for itm in adj_nodes:
                val.append(itm.data)
            node_data_to_adj_node_data[key] = val
        print(node_data_to_adj_node_data)

    def returnCopy(self):
        ##this should return a copy of self with n verts removed
        #it can also take a specific list of verts to remove as input
        #how?
        #find data in self.nodes
        #make list of nodes and their adj by data
        #then construct new nodes that match this data
        #NOTE:  I am doing this because I want to create a completely
        #different graph that has the same data in an analogous set of nodes
        #could store this data in a hashmap
        #node.data to adj_node.data for adj_node in node.adj
        node_data_to_adj_node_data = dict()
        node_data_to_node_in_g1 = dict()
        node_data_to_node_in_g2 = dict()
        node_to_node_data_in_g1 = dict()
        node_to_node_data_in_g2 = dict()
        for node in self.nodes:
            #self.nodes is g1s nodes
            key = node.data
            print("key type should be int")
            print(type(key))
            val = [adj_node.data for adj_node in node.adj]
            node_data_to_node_in_g1[key] = None
            node_data_to_adj_node_data[key] = val
        #now have data
        #so make new graph with it
        new_graph = Graph()
        for node_data in node_data_to_adj_node_data.keys():
            print("type(node_data)  should be int")
            print(type(node_data))
            new_node = GraphNode(node_data)
            node_data_to_node_in_g2[node_data] = new_node
            node_to_node_data_in_g2[new_node] = node_data
            new_graph.addNodeByNode(new_node)
        #i see the problem
        print(" node_data_to_adj_node_data.keys(): ")
        for node_data in node_data_to_adj_node_data.keys():
            print(node_data)
        print()
        for node in new_graph.nodes:
            #find it's adj node_data
            #then add the appropriate nodes to it's adj list
            print("current nodes data")
            print(node.data)
            print("type of node.data should be int")
            print(type(node.data))
            adj_node_data = node_data_to_adj_node_data[node.data]
            for adj_node_num in adj_node_data:
                adj_node = node_data_to_node_in_g2[adj_node_num]
                node.addAdjNode(adj_node)
        return new_graph
    
    def sortNodesByIncidenceNumber(self,a=None):
        #will use mergesort
        #will sort node list from highest incidence number to lowest
        new_node_list = []
        if a == None:
            a = self.nodes
        if len(a) == 1:
            return a
        else:
            mid = len(a)//2
            a1 = a[:mid]
            a2 = a[mid:]
            ret = MergeNodeLists(self.sortNodesByIncidenceNumber(a1),self.sortNodesByIncidenceNumber(a2))
            self.nodes = ret
            return ret
        
def MergeNodeLists(a1,a2):
    #a1 and a2 are a list of nodes
    i1 = 0
    i2 = 0
    ret = []
    while i1 < len(a1) and i2 < len(a2):
        if a1[i1].getNumAdj() > a2[i2].getNumAdj():
            ret.append(a1[i1])
            i1 += 1
        else:
            ret.append(a2[i2])
            i2 += 1
    while i1 < len(a1):
        ret.append(a1[i1])
        i1 += 1
    while i2 < len(a2):
        ret.append(a2[i2])
        i2 += 1
    return ret


class GraphNode(object):
    def __init__(self,data,adj=None):
        if adj == None:
            adj = []
        self.data = data
        self.adj = adj

    def getNumAdj(self):
        return len(self.adj)

    def getAdj(self):
        return self.adj

    def removeAdjNode(self,adj_node):
        if adj_node in self.adj:
            self.adj.remove(adj_node)

    def addAdjNode(self,node):
        self.adj.append(node)
    

def uniformly_chosen_perm_of_verts(nodes):
    ordered_list = []
    verts = [node for node in nodes]
    while len(verts) > 0:
       idx_of_vert_to_add = randint(0,len(verts)-1)
       vert_to_add = verts[idx_of_vert_to_add]
       ordered_list.append(vert_to_add)
       verts.remove(vert_to_add)
    return ordered_list

def constructPossibleStartVertsAndEndVertsExludingSomeEdgeSet(verts,edge_set):
    # we are constructing a hashmap where each key is a vert in the edge_set
    #and the vals are the possible verts that this vert could be connected to
    #conditions: no loops (the start and end vert can't be the same)
    #             the start and end vert cant form an edge in "edge_set"
    #             we want no duplicate edges represented in this hashmap
    #            ie if [2,4] is a possible edge it could also be [4,2]
    #            but we want the hashmap st the smaller num is seen as the start vert
    #           and the larger is in the val for that key not vice versa
    #           so for the key 2, 4 would be in hashmap[2]
    #            but not vice versa
    #edge set is an ordered list of a 2-set of verts
    #useful to have an ordered list so wait is it? maybe not
    #however having graph.nodes as an ordered list is useful because
    #then can make pairs of nodes with no duplicates easily by type of loop
    #written below ok but edge set can just be a set or bag as cs ppl say lol
    #with no duplicates
    start_vert_to_end_verts = dict()
    #wait this might still be technically doing what I wanted to do.....
    #could take a while....
    #well i'll write and test
   # print("len(verts) within constructPossibleStartVertsAndEndVertsExludingSomeEdgeSet method")
   # print(len(verts))
    for i in range(len(verts)-1):
        val = []
        for j in range(i+1,len(verts)):
            if ([verts[i],verts[j]] not in edge_set) and ([verts[j],verts[i]] not in edge_set):
                val.append(verts[j])
        """
        print("adding key to start_vert_to_end_verts")
        print("key")
        print(verts[i])
        print("val")
        print(val)
        print("or by label rather than class instance....")
        print("key by data")
        print(verts[i].data)
        print("val by data")
        print([node.data for node in val])
        """
        start_vert_to_end_verts[verts[i]] = val
    return start_vert_to_end_verts

def constructStartVertArrayAndProbArray(start_vert_to_end_verts):
    start_vert_arr = []
    prob_arr = []
    total_num_end_verts = 0
    for start_vert in start_vert_to_end_verts.keys():
        end_verts = start_vert_to_end_verts[start_vert]
        if len(end_verts) > 0:
            total_num_end_verts += len(end_verts)
            start_vert_arr.append(start_vert)
            prob_arr.append(len(end_verts))
    for i in range(len(prob_arr)):
        prob_arr[i] = prob_arr[i]/float(total_num_end_verts)
    return [start_vert_arr,prob_arr]

def chooseStartVertWItsProbability(start_vert_arr,prob_arr):
    randfloat = random()
#    print("data of elts in start_vert_arr within chooseStartVertWItsProb method")
#    for itm in start_vert_arr:
#        print(itm.data)
#    print()
#    print("prob_arr")
#    print(prob_arr)
#    print("randfloat")
#    print(randfloat)
    prob_arr_sum = []
    tally = 0
    for i in range(len(prob_arr)):
        tally += prob_arr[i]
        prob_arr_sum.append(tally)
    for i in range(len(prob_arr_sum)):
        if randfloat < prob_arr_sum[i]:
            return start_vert_arr[i]

def chooseEndVertUniformly(start_vert,start_vert_to_end_verts):
#    print(type(start_vert))
    end_verts = start_vert_to_end_verts[start_vert]
    rand_idx = randint(0,len(end_verts)-1)
    return end_verts[rand_idx]

def removeEdgeFromStartVertToEndVerts(start_vert_to_end_verts,edge):
    #just added an edge
    #it is guaranteed to be "in" startvertoendverts
    #need to remove it
    #so how?
    ordered_edge = edge
    start_vert = ordered_edge[0]
    if start_vert in start_vert_to_end_verts.keys():
        vals = start_vert_to_end_verts[start_vert]
        vals.remove(ordered_edge[1])
        start_vert_to_end_verts[start_vert] = vals
    else:
        start_vert = ordered_edge[1]
        vals = start_vert_to_end_verts[start_vert]
        vals.remove(ordered_edge[0])
        start_vert_to_end_verts[start_vert] = vals
    return start_vert_to_end_verts
    
"""
def UniformlyChooseFromPossibleEdgesNotInEdgeSet(verts,edge_set):
    start_vert_to_end_verts = constructPossibleStartVertsAndEndVertsExludingSomeEdgeSet(verts,edge_set)
    [start_vert_arr,prob_arr] = constructStartVertArrayAndProbArray(start_vert_to_end_verts)
    start_vert = chooseStartVertWItsProbability(start_vert_arr,prob_arr)
    end_vert = chooseEndVertUniformly(start_vert,start_vert_to_end_verts)
    new_edge = [start_vert,end_vert]
    return new_edge


def UniformlyChooseFromPossibleEdgesNotInEdgeSet(verts,edge_set,graph):
    start_vert_to_end_verts = constructPossibleStartVertsAndEndVertsExludingSomeEdgeSet(verts,edge_set)
    [start_vert_arr,prob_arr] = constructStartVertArrayAndProbArray(start_vert_to_end_verts)
    start_vert = chooseStartVertWItsProbability(start_vert_arr,prob_arr)
    end_vert = chooseEndVertUniformly(start_vert,start_vert_to_end_verts)
    new_edge = [start_vert,end_vert]
    return new_edge
"""
###### wrote this method to overwrite (overload?) cant remember the previous one
##### if something goes terribly wrong and this one doesn't work
#### can go back to using above until get this working
def UniformlyChooseFromPossibleEdgesNotInEdgeSet(verts,edge_set,start_vert_to_end_verts,last_edge_added,graph):
#    print("key data in uniformlychoosefrompossedgesnotinedgeset")
#    print("before modifying dict.....")
#    printKeyData(start_vert_to_end_verts)
    if last_edge_added != None:
        start_vert_to_end_verts = removeEdgeFromStartVertToEndVerts(start_vert_to_end_verts,last_edge_added)
#    print("after modifying.....")
#    printKeyData(start_vert_to_end_verts)
#    print("num keys in start_vert_to_end_verts")

#    print(len(start_vert_to_end_verts.keys()))
    [start_vert_arr,prob_arr] = constructStartVertArrayAndProbArray(start_vert_to_end_verts)
#    print("elt type for elt of start_vert_arr")
#    for itm in start_vert_arr:

#        print(type(itm))
#    print()
#    print("data of elts in start_vert_arr")
#    for itm in start_vert_arr:
#        print(itm.data)
    #print()
    #for v in start_vert_arr:
#        print("v in graph.getNodes()")
#        print("(should be true)")
#        print(v in graph.getNodes())
    start_vert = chooseStartVertWItsProbability(start_vert_arr,prob_arr)
    #print("desired start_verts type")
    #print(type(start_vert))
    #print("desired start_vert's data")
    #print(start_vert.data)
    end_vert = chooseEndVertUniformly(start_vert,start_vert_to_end_verts)
    new_edge = [start_vert,end_vert]
#    print("start_vert in graph.getNodes()")
#    print(start_vert in graph.getNodes())
#    print("end_vert in graph.getNodes()")
#    print(end_vert in graph.getNodes())
    return new_edge

def printKeyData(start_vert_to_end_verts):
    print("data of keys in start_vert_to_end_verts")
    for key in start_vert_to_end_verts.keys():
        print(key.data)
    print()

def printEdgeData(edge):
    print("data in the end verts of this edge")
    for vert in edge:
        print(vert.data)

def GenRandomGraphNNodes(num_nodes,num_edges):
    #MUST HOLD: num_edges > num_nodes-1
    if num_edges <= num_nodes -1:
        print("Error!  We must have num_edges > num_nodes - 1")
        return None
    if num_edges > int((num_nodes)*(num_nodes-1)*0.5):
        print("Error!  The complete graph on %d nodes has %d edges.  You can not ask for more than that!" % (num_nodes,int((num_nodes)*(num_nodes-1)*0.5)))
        return None
    g = Graph()
    for i in range(num_nodes):
        g.addNode(i)
    verts = g.getNodes()
    #print("len(verts)")
    #print(len(verts))
    random_perm = uniformly_chosen_perm_of_verts(verts)
    #print("len(verts) after calling uniform perm method")
    #print(len(verts))
    edge_set = []
    for i in range(len(random_perm)-1):
        start_vert = random_perm[i]
        end_vert = random_perm[i+1]
        edge = [start_vert,end_vert]
        g.addEdgeByNode(edge)
        edge_set.append(edge)
    #print("len edge set")
    #print(len(edge_set))
    #print("len(verts) right before calling constructpossstartvertandendvertsexlcsomeedgeset method")
    #print(len(verts))
    start_vert_to_end_verts = constructPossibleStartVertsAndEndVertsExludingSomeEdgeSet(verts,edge_set)
    #print("num keys in start_vert_to_end_verts right after constructing")
    #print(len(start_vert_to_end_verts.keys()))
#    printKeyData(start_vert_to_end_verts)
    last_edge_added = None
    for i in range(num_edges-num_nodes+1):
        edge = UniformlyChooseFromPossibleEdgesNotInEdgeSet(verts,edge_set,start_vert_to_end_verts,last_edge_added,g)
        #printEdgeData(edge)
        g.addEdgeByNode(edge)
        edge_set.append(edge)
        last_edge_added = edge
    return g

def returnAdjMatrixDistance(g1,g2):
    """
    NOTE:  my idea for sorting by incidence number then trying all reorderings
    within chains of verts w same incidence number works perfectly
    (read: returns a distance of zero for isomorphic graphs) but might return too
    high a distance for near-isomorphic graphs with different number of nodes
    THEREFORE, would want to enlargen the smaller adj matrix in the "right way"
    meaning in this case we want the empty rows in the adj matrix for the smaller graph
    to coincide with where the verts in the larger graph were deleted
    EG do NOT want to just add rows and cols at end

    RELATED IDEA:  could try defining the edge weight distance between a null node and it's
    corresponding node in the other graph to be different constants then test and use
    the one that gives us the right distance for our near isomorphism problem
    #note: might want to scale this ie take the AVERAGE sqaure dist
    """
    a1 = g1.constructAdjMatrix()
    a2 = g2.constructAdjMatrix()
    #need to even out lengths
    #for now just add rows and cols to the smaller one at the end
    if len(a1) < len(a2):
        #by the way these are both square
        row_diff = len(a2) - len(a1)
        for i in range(len(a1)):
            for j in range(row_diff):
                #NOTE COULD CHANGE THIS VALUE DEPENDING ON TESTING
                a1[i].append(0)
        #IF CHANGE CHANGE HERE TOO
        new_row = [0 for i in range(len(a2))]
        for i in range(row_diff):
            a1.append(new_row)
    elif len(a2) < len(a1):
        row_diff = len(a1) - len(a2)
        for i in range(len(a2)):
            for j in range(row_diff):
                #NOTE COULD CHANGE THIS VALUE DEPENDING ON TESTING
                a2[i].append(0)
        #IF CHANGE CHANGE HERE TOO
        new_row = [0 for i in range(len(a1))]
        for i in range(row_diff):
            a2.append(new_row)
    diff_sum = 0
    for i in range(len(a1)-1):
        for j in range(i,len(a1[i])):
            diff_sum += (a2[i][j] - a1[i][j])**2
    diff_av = diff_sum/(0.5*len(a1)**2)
    return diff_av

print("Testing! (Note: some of these should produce errors!)")
print("Generating a random graph with 2 nodes and 0 edges:")
g = GenRandomGraphNNodes(2,0)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 2 nodes and 1 edges:")
g = GenRandomGraphNNodes(2,1)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 2 nodes and 2 edges:")
g = GenRandomGraphNNodes(2,2)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 2 nodes and 3 edges:")
g = GenRandomGraphNNodes(2,3)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 2 nodes and 4 edges:")
g = GenRandomGraphNNodes(2,4)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 2 nodes and 5 edges:")
g = GenRandomGraphNNodes(2,5)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 2 nodes and 6 edges:")
g = GenRandomGraphNNodes(2,6)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 2 nodes and 7 edges:")
g = GenRandomGraphNNodes(2,7)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 2 nodes and 8 edges:")
g = GenRandomGraphNNodes(2,8)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 2 nodes and 9 edges:")
g = GenRandomGraphNNodes(2,9)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 2 nodes and 10 edges:")
g = GenRandomGraphNNodes(2,10)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 3 nodes and 0 edges:")
g = GenRandomGraphNNodes(3,0)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 3 nodes and 1 edges:")
g = GenRandomGraphNNodes(3,1)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 3 nodes and 2 edges:")
g = GenRandomGraphNNodes(3,2)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 3 nodes and 3 edges:")
g = GenRandomGraphNNodes(3,3)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 3 nodes and 4 edges:")
g = GenRandomGraphNNodes(3,4)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 3 nodes and 5 edges:")
g = GenRandomGraphNNodes(3,5)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 3 nodes and 6 edges:")
g = GenRandomGraphNNodes(3,6)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 3 nodes and 7 edges:")
g = GenRandomGraphNNodes(3,7)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 3 nodes and 8 edges:")
g = GenRandomGraphNNodes(3,8)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 3 nodes and 9 edges:")
g = GenRandomGraphNNodes(3,9)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 3 nodes and 10 edges:")
g = GenRandomGraphNNodes(3,10)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 4 nodes and 0 edges:")
g = GenRandomGraphNNodes(4,0)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 4 nodes and 1 edges:")
g = GenRandomGraphNNodes(4,1)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 4 nodes and 2 edges:")
g = GenRandomGraphNNodes(4,2)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 4 nodes and 3 edges:")
g = GenRandomGraphNNodes(4,3)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 4 nodes and 4 edges:")
g = GenRandomGraphNNodes(4,4)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 4 nodes and 5 edges:")
g = GenRandomGraphNNodes(4,5)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 4 nodes and 6 edges:")
g = GenRandomGraphNNodes(4,6)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 4 nodes and 7 edges:")
g = GenRandomGraphNNodes(4,7)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 4 nodes and 8 edges:")
g = GenRandomGraphNNodes(4,8)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 4 nodes and 9 edges:")
g = GenRandomGraphNNodes(4,9)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 4 nodes and 10 edges:")
g = GenRandomGraphNNodes(4,10)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 5 nodes and 0 edges:")
g = GenRandomGraphNNodes(5,0)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 5 nodes and 1 edges:")
g = GenRandomGraphNNodes(5,1)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 5 nodes and 2 edges:")
g = GenRandomGraphNNodes(5,2)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 5 nodes and 3 edges:")
g = GenRandomGraphNNodes(5,3)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 5 nodes and 4 edges:")
g = GenRandomGraphNNodes(5,4)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 5 nodes and 5 edges:")
g = GenRandomGraphNNodes(5,5)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 5 nodes and 6 edges:")
g = GenRandomGraphNNodes(5,6)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("---------------------------")
print("Generating a random graph with 5 nodes and 7 edges:")
g = GenRandomGraphNNodes(5,7)
if g:
    g.printNodesDataToAdjSet()
    g.printNodesAndIncNumbers()
print()
print("SORTING NODES BY INCIDENCE NUMBER")
g.sortNodesByIncidenceNumber()
g.printNodesDataToAdjSet()
g.printNodesAndIncNumbers()
print()
print("Generating a random graph with 5 nodes and 8 edges:")
g = GenRandomGraphNNodes(5,8)
print("-------------------------------------------")
print("these two adj lists should be equal")
if g:
    g.printNodesDataToAdjSet()
g2 = g.returnCopy()
g2.printNodesDataToAdjSet()
print()
print("checking for node equality, these should all be FALSE")
for node1 in g.getNodes():
    for node2 in g2.getNodes():
        print(node1 == node2)
node_to_rem = g2.getNodes()[2]
g2.removeNode(node_to_rem)
g2.printNodesDataToAdjSet()
node1 = g2.getNodes()[0]
node2 = g2.getNodes()[2]
g2.removeEdge(node1,node2)
g2.removeEdge(node1,node1)
g2.printNodesDataToAdjSet()
g3 = g2.returnCopy()
nodea = g3.getNodes()[0]
nodeb = g3.getNodes()[1]
g3.removeEdge(nodea,nodeb)
g3.printNodesDataToAdjSet()
print("adj matrix dist between g and itself")
print(returnAdjMatrixDistance(g,g))
print("adj matrix dist between g and g2")
print(returnAdjMatrixDistance(g,g2))
print("adj matrix dist between g2 and g3")
print(returnAdjMatrixDistance(g3,g2))
print("adj matrix dist between g and g3")
print(returnAdjMatrixDistance(g3,g))
print("-------------------------------------------")
print()
print()
print("Generating a random graph with 5 nodes and 9 edges:")
g = GenRandomGraphNNodes(5,9)
if g:
    g.printNodesDataToAdjSet()
print()
print()
print("Generating a random graph with 5 nodes and 10 edges:")
g = GenRandomGraphNNodes(5,10)
if g:
    g.printNodesDataToAdjSet()
print()
print()
