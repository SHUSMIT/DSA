def job_seq(jobs):
    # jobs - > (id,profit,deadline)
    job = sorted(jobs, key = lambda x : x[1] ) # sort based on profit -> x[1], max profit will be 
    max_wait = max(jobs, key = lambda x: x[2] )[2]  # gets max deadline

    profit = 0
    day = [-1 for  i in range(max_wait+1)]

    for  i in range(len(jobs)):

        j_id,cur_profit,deadline = job.pop() # the last/max profit pops

        for j in range(deadline,0,-1): # check from deadline index to 1, if its -1, fill it
            if day[j] == -1:
                day[j] = j_id # assign it the j _id
                profit += cur_profit # add to cur profit
                break # break out after possible assign
    
    return profit


def job_seq(jobs):
    # jobs - > (id,profit,deadline)
    job = sorted(jobs, key = lambda x : x[1] , reverse = True ) # sort based on profit -> x[1], max profit will be first
    max_wait = max(job, key = lambda x : x[2])[2] # max deadline ( tuple first )

    profit = 0
    day = [-1 for  i in range(max_wait+1)]

    for j_id,cur_profit,deadline in job:

        for j in range(deadline,0,-1): # check from deadline index to 1, if its -1, fill it
            if day[j] == -1: # assign it the j _id
                day[j] = j_id 
                profit += cur_profit # add to cur profit
                break # break out after possible assign

    return profit

