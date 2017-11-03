import math

class Stack(object):
    def __init__(self,top=None):
        self.top = top

    def is_empty(self):
        return (self.top == None)
        
    def push(self,treenode):
        new_node = StackNode(treenode)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.Next = self.top
            self.top = new_node

    def pop(self):
        ret = self.top.data
        self.top = self.top.Next
        return ret
        
    def peek(self):
        return self.top.data

class StackNode(object):
    def __init__(self,data,Next=None):
        self.data = data
        self.Next = Next

#TODO FIX DELTE NUM METHOD

class TreeNode(object):
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def addNum(self,num):
        parent = None
        current = self
        while current != None:
            if current.data > num:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right
        new_node = TreeNode(num)
        if parent.data < num:
            parent.right = new_node
        else:
            parent.left = new_node

    def deleteNum(self,num):
        #find num in bstree
        #keeping track of parent
        parent = None
        current = self
        while current.data != num:
            if current.data < num:
                parent = current
                current = current.right
            else:
                parent = current
                current = current.left
        #once find num
        #if num has zero children just make parent point to None instead of num node
        #if has one child make parent point to that one child
        #else has two children
        #find smallest elt in subtree of right child
        #make the current node containt that data then delete where that data was before
        #using this method so it will need to be recursive
        #stop condition should be if num is at a leaf
        #or if it only has 1 child
        #if it has two children the recursing will need to keep happening
        if current.left == None and current.right == None:
            if parent.data < current.data:
                #current is a right child
                parent.right = None
            else:
                #current is a left child
                parent.left = None
        elif current.left == None:
            #and current.right != None
            if parent.data < current.data:
                #current is a right child
                parent.right = current.right
            else:
                #current is a left child
                parent.left = current.right
        elif current.right == None:
            #and current.left != None
            if parent.data < current.data:
                #current is a right child
                parent.right = current.left
            else:
                #current is a left child
                parent.left = current.left
        else:
            #current has two children
            self.findSmallestInSubtreeAndUpdateCurrentVal(current)
            

    def findSmallestInSubtreeAndUpdateCurrentVal(self,current_node):
        parent_of_smallest = None
        smallest_data = math.inf
        queue = [[None,current_node]]
        while len(queue) > 0:
            [parent,current] = queue.pop(0)
            if current < smallest_data:
                parent_of_smallest = parent
                smallest_data = current
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
        current.node.data = smallest_data
        return smallest_data

    def PostOrderIteratively(self):
        ret = []
        current = self
        stack = Stack()
        stack.push(self)
        print("roots data")
        print(self.data)
        while not stack.is_empty():
            current = stack.peek()
            print("current == None")
            print(current == None)
            if current:
                print("current.data")
                print(current.data)
            if current.left != None and current.left not in ret:
                print("did option 1")
                current = current.left
                stack.push(current)
            elif current.right != None and current.right not in ret:
                print("did option 2")
                current = current.right
                stack.push(current)
            else:
                print("did option 3")
                ret_itm = stack.pop()
                ret.append(ret_itm)
            print("ret_so_far")
            print([itm.data for itm in ret])
        return ret
            

def iterativelyFindMids(sorted_array):
    length = len(sorted_array)
    queue = []
    queue.append([0,length])
    idxs = []
    while len(queue) > 0:
        [start,end] = queue.pop(0)
        mid = math.floor((start + end)/2.0)
        idxs.append(mid)
        if start<mid:
            queue.append([start,mid])
        if mid+1<end:
            queue.append([mid+1,end])
    ret = []
    for idx in idxs:
        ret.append(sorted_array[idx])
    return ret

def constructBST(sorted_array):
    #constructs a BST with minimal height from a sorted array
    list_to_add = iterativelyFindMids(sorted_array)
    root = TreeNode(list_to_add[0])
    for i in range(1,len(list_to_add)):
        root.addNum(list_to_add[i])
    return root

        
a = [i for i in range(16)]
print(iterativelyFindMids(a))
BST = constructBST(a)
print(BST.PostOrderIteratively())
    
