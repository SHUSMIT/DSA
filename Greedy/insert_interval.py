def insert_interval(interval, insert):
    new_interval = []

    # i need left part not overlapping, overlapping and right part not overlapping.
    # in over lapping with inser, [min , max] of all would be ans

    # left -> right extreme is less than insert start
    # right ->  left start is more than insert end

    n = len(interval)
    i = 0

    while i < n and interval[i][1] < insert[0]: # right extreme is less than insert start

        new_interval.append(interval[i])
        i += 1

    #overlap
    start,end = insert[0],insert[1]
    while i < n and interval[i][0] <= end:
        start = min(start,interval[i][0])
        end = max(end,interval[i][1])
    
    new_interval.append([start,end])

    #remaining
    while i<n:
        new_interval.append(interval[i])

    return new_interval