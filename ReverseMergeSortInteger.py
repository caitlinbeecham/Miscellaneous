def Descending_Order(num):
    #Bust a move right here
    num_ints = [int(char) for char in str(num)]
    ret_ints = ReverseMergeSort(num_ints)
    ret_str = ""
    for num in ret_ints:
        ret_str += str(num)
    return int(ret_str)
    
def ReverseMergeSort(a):
    if len(a) == 1:
        return a
    else:
        mid = len(a)//2
        a1 = a[:mid]
        a2 = a[mid:]
        return ReverseMerge(ReverseMergeSort(a1),ReverseMergeSort(a2))

def ReverseMerge(a1,a2):
    idx1 = 0
    idx2 = 0
    ret = []
    while idx1 < len(a1) and idx2 < len(a2):
        if a1[idx1] > a2[idx2]:
            ret.append(a1[idx1])
            idx1 += 1
        else:
            ret.append(a2[idx2])
            idx2 += 1
    
    while idx1 < len(a1):
        ret.append(a1[idx1])
        idx1 += 1
    while idx2 < len(a2):
        ret.append(a2[idx2])
        idx2 += 1
    return ret
