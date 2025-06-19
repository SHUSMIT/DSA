def remove_k(s,k):
    # remove k digits such that number is smallest
    # push into stack, if its bigger remove it, if not add it
    st = []
    count = 0

    for char in s:
        while st and int(st[-1]) > int(char) and count < k: # its greater so keep popping
            st.pop()
            count += 1

        st.append(char) # push it into stack

    
    while count != k: # elements left to be popped -> 1,2,3,4,5 --> no pop
        st.pop()
        count += 1
    
    
    ans = ''.join(st)

    return int(ans) if ans else 0


        
