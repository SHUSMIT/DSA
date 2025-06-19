def interval_removal_overlap(interval):
    n = len(interval)
    # (start,end)
    sort_interval = sorted(interval , key = lambda x : x[1]) # sort based on end, as that is imp

    index = []
    boundary = -1

    for idx, (start,end) in enumerate(sort_interval):

        if start >= boundary:
            index.append(idx) # valid, store its index
            boundary = end # update the boundary 
    
    return n - len(index)

#Greedy by end time ensures the most room for future intervals.