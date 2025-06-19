def asteroid(arr):
    st = []
    # keep adding positive to stack
    # if st[-1] > 0 and i <0 --> collission 
    # if negative encountered -
    # if its bigger, keep popping ... once empty reverse it
    # if smaller, remove that and go ahead
    # if equal remove both
    n = len(arr)
    st.append(arr[0])

    for i in range(1,n):

        if st:
            #collision scenarios

            while st and st[-1] > 0 and arr[i] < 0 and abs(arr[i]) > st[-1]: # the negative is more than positve, keep popping
                st.pop()
            
            if st and st[-1] + arr[i] == 0: # both equal
                st.pop()
                continue # skip now
            
            if st and arr[i] < 0 and st[-1] > abs(arr[i]):
                continue # skip if current is smaller

            #non-collision, add to stack

            if len(st) == 0 or st[-1] < 0 or arr[i] > 0:
                st.append(arr[i])
        
        else: # stack empty
            st.append(arr[i])


    return st

