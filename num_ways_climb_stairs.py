def num_ways_climb_stairs(n):
    #using step intervals of 1, 2, 3 or 4
    list_so_far = [1,1,2,4,8]
    for i in range(5,n+1):
        list_so_far.append(list_so_far[i-4]+list_so_far[i-3]+list_so_far[i-2]+list_so_far[i-1])
    print(list_so_far)
    return list_so_far[n]

print(num_ways_climb_stairs(20))
