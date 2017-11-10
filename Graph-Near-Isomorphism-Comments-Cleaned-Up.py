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
    def __init__(self,nodes=None,adj_matrix=None):
        if not nodes:
            nodes = []
        self.nodes = nodes
        self.num_edges = 0
        if not adj_matrix:
            adj_matrix = []
        self.adj_matrix = adj_matrix
        self.node_to_node_idx = dict()

    def getNodes(self):
        return self.nodes

    def addNode(self,data):
        ###REWRITE SO UPDATE ADJ MATRIX#####
        """
        as add node need to add a row and col to adj matrix
        inc_number will initially be zero so can stay at end of matrix
        also need to add node and idx to node_to_node_idx
        """
        ###THIS SHOULD BE DONE NOW---TESTTTTT#######
        new_node = GraphNode(data)
        if new_node not in self.nodes:
            node_idx = len(self.nodes)
            self.nodes.append(new_node)
            self.node_to_node_idx[new_node] = node_idx
            #add col to self.adj_matrix
            for row in self.adj_matrix:
                row.append([None,None])
            new_row = [[None,None] for node in self.nodes]
            self.adj_matrix.append(new_row)
        ######TODO TEST########

    def addNodeByNode(self,node):
        ###THIS SHOULD BE DONE NOW---TESTTTTT#######
        if node not in self.nodes:
            node_idx = len(self.nodes)
            self.nodes.append(node)
            self.node_to_node_idx[node] = node_idx
            #add col to self.adj_matrix
            for row in self.adj_matrix:
                row.append([None,None])
            new_row = [[None,None] for itm in self.nodes]
            self.adj_matrix.append(new_row)

    def addEdgeByNode(self,edge):
        ###REWRITE SO UPDATE ADJ MATRIX#####
        #edge is a set of 2 instances of the GraphNode class
        """
        Note: need to update adj matrix... how?
        well... need to change the entry at the idx i for vert1 and the idx  j for vert2 and vice versa (with i and j swapped)
        then the inc_number of each node will have gone up by one so need to move that row and column up in the adj matrix
        NOTE: ##########################THIS IS NON-TRIVIAL ---------- SPEND TIME FIGURING OUT HOW TO DO THIS###########################
        """
        [vert1,vert2] = edge
        vert1.addAdjNode(vert2)
        vert2.addAdjNode(vert1)
        self.num_edges += 1

    def removeNode(self,node):
        ###REWRITE SO UPDATE ADJ MATRIX#####
        """
        Note: need to update adj matrix... how?
        well... need to decrease the incidence number of every node that was adj to node by 1,
        then need to delete the row and column associated with node COMPLETELY
        NOTE: ##########################THIS IS NON-TRIVIAL ---------- SPEND TIME FIGURING OUT HOW TO DO THIS###########################
        """
        if node in self.nodes:
            for itm in node.adj:
                itm.removeAdjNode(node)
            self.nodes.remove(node)
        #####TEST######

    def removeEdge(self,node1,node2):
        ###REWRITE SO UPDATE ADJ MATRIX#####
        """
        Note: need to update adj matrix... how?
        well need to find the 2 entries corresponding to this edge in adj matrix and make them each [None,None]
        then for the two nodes, need to lower their inc_number by 1
        then need to reorder the adj matrix because these verts' respective inc_numbers have changed
        NOTE: could also NOT do this reordering and then just use a sorting algorithm that works well for data that is MOSTLY in order
        (like bubble sort) each time need to call adj_matrix_distance_method
        OR: could once again not reorder the row and columns as add and remove things and just do this on each subgraph as we find their
        sub-adjacency matrices
        NOTE: ##########################THIS IS NON-TRIVIAL ---------- SPEND TIME FIGURING OUT HOW TO DO THIS###########################
        """
        if node1 in self.nodes and node2 in self.nodes:
            node1.removeAdjNode(node2)
            node2.removeAdjNode(node1)
        #####TEST######

    """
    def constructAdjMatrix(self):



   ########NOTE THIS METHOD IS NOW OBSOLETE AS WE ARE DOING THIS AS WE GO#####


   ##########Instead will need a FIND ALL REORDERINGS WITHIN SAME INC NUMBER Method
   ##########WILL ALSO NEED modify adj matrix method for a given reordering
   ###NOTE: could either make copies of the adj matrix for each reordering
   ###BUT BETTER would be to for each reordering
   #############################reorder the rows and cols of the adj matrix
   #############################find the adj matrix dist using this new reordered matrix
   ####Then choose the lowest adj_matrix_dist as the actual dist
   ####NOTE when computing adj matrix dist between g1 and g2
   ####only need to reorder the adj matrix of ONE of g1 or g2, say g1
   ####and for each reordering compute the distance to the other, say g2
   ####and return the min such distance
      
        self.sortNodesByIncidenceNumber()
        adj_matrix = [[0 for node1 in self.nodes] for node2 in self.nodes]
        for i in range(len(self.nodes)-1):
            for j in range(i,len(self.nodes)):
                if self.nodes[j] in self.nodes[i].getAdj():
                    adj_matrix[i][j] = 1
                    adj_matrix[j][i] = 1
        return adj_matrix
        
    """
    
    def constructIncidenceNumberToNodes(self):
        #####MAY BE ABLE TO MODIFY THIS METHOD TO READ FROM ADJ MATRIX
        #####actually may not need at all
        #grouping  the nodes by incidence number and creating a hashmap
        inc_number_to_nodes = dict()
        for node in self.nodes:
            inc_number = len(node.getAdj())
            if inc_number in inc_number_to_nodes.keys():
                val = inc_number_to_nodes[inc_number]
                val.append(node)
                inc_number_to_nodes[inc_number] = val
            else:
                inc_number_to_nodes[inc_number] = [node]
        return inc_number_to_nodes
        
    def printNodesAndIncNumbers(self):
        ret = ""
        for node in self.nodes:
            ret += "Node Data: " + str(node.data) + "\n"
            ret += "Incidence Number: " + str(node.getNumAdj()) + "\n"
        print(ret)
            
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
            val = [adj_node.data for adj_node in node.adj]
            node_data_to_node_in_g1[key] = None
            node_data_to_adj_node_data[key] = val
        #now have data
        #so make new graph with it
        new_graph = Graph()
        for node_data in node_data_to_adj_node_data.keys():
            new_node = GraphNode(node_data)
            node_data_to_node_in_g2[node_data] = new_node
            node_to_node_data_in_g2[new_node] = node_data
            new_graph.addNodeByNode(new_node)
        for node in new_graph.nodes:
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
        

class GraphNode(object):
    def __init__(self,data,adj=None,inc_number=0):
        if adj == None:
            adj = []
        self.data = data
        self.adj = adj
        self.inc_number = inc_number

    def getNumAdj(self):
        return len(self.adj)

    def getAdj(self):
        return self.adj

    def removeAdjNode(self,adj_node):
        if adj_node in self.adj:
            self.adj.remove(adj_node)
            self.inc_number -= 1

    def addAdjNode(self,node):
        self.adj.append(node)
        self.inc_number += 1
    

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

#########TODO WRITE THIS METHOD BY LOOKING AT EXAMPLES
#########DO ON PAPER FIRST
#def compareIncNumberToNodes1And2(inc_number_to_nodes_1,inc_number_to_nodes_2,nodes_1,nodes_2):
    ###need to think about how I want to do this first
    ##go through examples first I just realized this wouldnt work!

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
    prob_arr_sum = []
    tally = 0
    for i in range(len(prob_arr)):
        tally += prob_arr[i]
        prob_arr_sum.append(tally)
    for i in range(len(prob_arr_sum)):
        if randfloat < prob_arr_sum[i]:
            return start_vert_arr[i]

def chooseEndVertUniformly(start_vert,start_vert_to_end_verts):
    end_verts = start_vert_to_end_verts[start_vert]
    rand_idx = randint(0,len(end_verts)-1)
    return end_verts[rand_idx]

def removeEdgeFromStartVertToEndVerts(start_vert_to_end_verts,edge):
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
    if last_edge_added != None:
        start_vert_to_end_verts = removeEdgeFromStartVertToEndVerts(start_vert_to_end_verts,last_edge_added)
    [start_vert_arr,prob_arr] = constructStartVertArrayAndProbArray(start_vert_to_end_verts)
    start_vert = chooseStartVertWItsProbability(start_vert_arr,prob_arr)
    end_vert = chooseEndVertUniformly(start_vert,start_vert_to_end_verts)
    new_edge = [start_vert,end_vert]
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
    if num_nodes < 1:
        print("Error!  We need at least 1 node!")
        return None
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
    random_perm = uniformly_chosen_perm_of_verts(verts)
    edge_set = []
    for i in range(len(random_perm)-1):
        start_vert = random_perm[i]
        end_vert = random_perm[i+1]
        edge = [start_vert,end_vert]
        g.addEdgeByNode(edge)
        edge_set.append(edge)
    start_vert_to_end_verts = constructPossibleStartVertsAndEndVertsExludingSomeEdgeSet(verts,edge_set)
    last_edge_added = None
    for i in range(num_edges-num_nodes+1):
        edge = UniformlyChooseFromPossibleEdgesNotInEdgeSet(verts,edge_set,start_vert_to_end_verts,last_edge_added,g)
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

def runTestCase(num_nodes,num_edges):
    ###
    """
    generates a graph, makes a copy with one edge removed, makes a copy of that with
    2 edges removed
    looks at distances between them
    from the starting graph, makes a copy and removes a node, then makes
    a copy of that and removes a second node
    reports distances
    """
    ###
    print("----------TEST CASE WITH %d nodes and %d edges: --------" % (num_nodes,num_edges))
    g = GenRandomGraphNNodes(num_nodes,num_edges)
    if g:
        print("node data to adj data for g")
        g.printNodesDataToAdjSet()
        found = False
        while not found:
            randidx1 = randint(0,len(g.getNodes())-1)
            randidx2 = randint(0,len(g.getNodes())-1)
            g2 = g.returnCopy()
            node1 = g2.getNodes()[randidx1]
            node2 = g2.getNodes()[randidx2]
            if (node2 in node1.getAdj()) and (node1 in node2.getAdj()):
                found = True
                #g2 = g.returnCopy()
                g2.removeEdge(node1,node2)
                print("node data to adj data for g2")
                g2.printNodesDataToAdjSet()
        found = False
        while not found:
            randidx1 = randint(0,len(g2.getNodes())-1)
            randidx2 = randint(0,len(g2.getNodes())-1)
            g3 = g2.returnCopy()
            node1 = g3.getNodes()[randidx1]
            node2 = g3.getNodes()[randidx2]
            if node2 in node1.getAdj():
                found = True
                g3.removeEdge(node1,node2)
                print("node data to adj data for g3")
                g3.printNodesDataToAdjSet()
        randidx1 = randint(0,len(g.getNodes())-1)
        g4 = g.returnCopy()
        node1 = g4.getNodes()[randidx1]
        g4.removeNode(node1)
        print("node data to adj data for g4")
        g4.printNodesDataToAdjSet()
        randidx1 = randint(0,len(g4.getNodes())-1)
        g5 = g4.returnCopy()
        node1 = g5.getNodes()[randidx1]
        g5.removeNode(node1)
        print("node data to adj data for g5")
        g5.printNodesDataToAdjSet()
        print("g2 is g with one edge removed")
        print("g3 is g with two edges removed")
        print("g4 is g with one node removed")
        print("g5 is g with two nodes removed")
        print("Dist between g and g2:")
        print(returnAdjMatrixDistance(g,g2))
        print("Dist between g2 and g3:")
        print(returnAdjMatrixDistance(g2,g3))
        print("Dist between g and g3:")
        print(returnAdjMatrixDistance(g,g3))
        print("Dist between g and g4:")
        print(returnAdjMatrixDistance(g,g4))
        print("Dist between g4 and g5:")
        print(returnAdjMatrixDistance(g4,g5))
        print("Dist between g and g5:")
        print(returnAdjMatrixDistance(g,g5))
        print("Dist between g3 and g4:")
        print(returnAdjMatrixDistance(g3,g5))
    print()
    print()
    print()

print("Testing! (Note: some of these should produce errors!)")
for num_nodes in range(2,5):
    max_num_edges = int(num_nodes*(num_nodes-1)*0.5)
    for num_edges in range(max_num_edges + 1):
        runTestCase(num_nodes,num_edges)
