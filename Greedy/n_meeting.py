def n_meeting(start,end):
    n = len(start)
    ## stack
    st = list()
    
    for i in range(n):
        st.append((start[i],end[i],i)) ## startTime,endTime,index
    
    st_sort = sorted(st, key = lambda x: x[1]) # end time sort, i want faster end

    index = list() # store the index/id

    finishTime = 0 # keep a record of last finish time

    for startTime,endTime,idx in st_sort:

        if startTime > finishTime: # start > last finish, store it, viable
            index.append(idx) 
            finishTime = endTime # update the finish time
    
    return len(index) , index


