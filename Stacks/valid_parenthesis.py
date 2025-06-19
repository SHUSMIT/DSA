def valid_parenthesis(s):
    st = []

    pair = {'(' : ')' , '[' : ']' , '{' : '}'}

    if s[0] in ')}]':
        return False # direct imbalance
    
    for char in s:
        if char in '[{(':
            st.append(char)

        else:
            if st: # check if something there
                prev = st.pop()
                if pair[prev] != char: # check corresponding close of last opened equals the current closing char
                    return False
    
    return len(st) == 0