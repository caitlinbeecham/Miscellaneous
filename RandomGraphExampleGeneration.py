from random import *
"""
1. empty graph
2. for num of verts uniformly pick one permutation of the verts
which is written p_0,p_1,p_2,p_3...p_(n-1)
3. for each i in range(n-1):
    add edge between [p_i and p_(i-1)]
4. choose uniformly m-n+1 edges to add from set of ((possible edges among verts) - (edges already included))


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
verts = graph.nodes

def uniformly_chosen_perm_of_verts(verts):
    ordered_list = []
    while len(verts) > 0:
        # 0 might be wrong
       #n wont actually run will go up to n-1
       #indexing for me will start at 0
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
    start_verts_to_end_verts = dict()
    #wait this might still be technically doing what I wanted to do.....
    #could take a while....
    #well i'll write and test
    for i in range(len(verts)-1):
        val = []
        for j in range(i+1,len(verts)):
            if set([verts[i],verts[j]]) not in edge_set:
                val.append([verts[i],verts[j]])
        start_verts_to_end_verts[verts[i]] = val
    return start_verts_to_end_verts

def constructStartVertArrayAndProbArray(start_verts_to_end_verts):
    start_vert_arr = []
    prob_arr = []
    total_num_end_verts = 0
    for start_vert:end_verts in start_vert_to_end_verts:
        if size(end_verts) > 0:
            total_num_end_verts += len(end_verts)
            start_vert_arr.append(start_vert)
            prob_arr.append(len(end_verts))
    for i in range(len(prob_arr)):
        prob_arr[i] = prob_arr[i]/float(total_num_end_verts)
    return [start_vert_arr,prob_arr]

def chooseStartVertWItsProbability(start_vert_arr,prob_arr):
    randfloat = random()
    for i in range(len(prob_arr)):
        if randfloat < prob_arr[i]:
            return start_vert_arr[i]

def chooseEndVertUniformly(start_vert,start_vert_to_end_verts):
    end_verts = start_vert_to_end_verts[start_vert]
    rand_idx = randint(0,len(end_verts)-1)
    return end_verts[rand_idx]

def UniformlyChooseFromPossibleEdgesNotInEdgeSet(verts,edge_set):
    start_vert_to_end_verts = constructPossibleStartVertsAndEndVertsExludingSomeEdgeSet(verts,edge_set)
    [start_vert_arr,prob_arr] = constructStartVertArrayAndProbArray(start_verts_to_end_verts)
    start_vert = chooseStartVertWItsProbability(start_vert_arr,prob_arr)
    end_vert = chooseEndVertUniformly(start_vert,start_vert_to_end_verts)
    new_edge = set([start_vert,end_vert])
    return new_edge

print(uniformly_chosen_perm_of_verts(verts))
