from collections import deque

def word_ladder(arr, start, end):
    
    n = len(arr)
    word_dict = set(arr) ## create a set ( visited array)
    q = deque()
    q.append((start,[start])) ## add to q the start and resulting pattern
    
    result = []
    found = False # early break
    
    while q:
        
        q_length = len(q) ## level wise traversal
        q_node = set()
        
        for _ in range(q_length): ## till all elements in that q is present we do it
        
            word,path = q.popleft()
            
            for i in range(len(word)): ## check for all possible digit
            
                alphabets = 'abcdefghijklmnopqrstuvwxyz' ## string immutable, slicing possible
                
                for c in alphabets: ## we slice upto i-1 add the req into i and then go from i+1 to end, as strings are not array
                
                    next_word = word[:i] + c + word[i+1:]  
                    
                    if next_word in word_dict:  ## if present
                        
                        if next_word == end: # found
                            found = True
                            result.append(path+[next_word]) # add that word to path and into result
                        else:
                            q.append((next_word, path + [next_word] )) ## if word present but not equal we add it to path and also next word
                            q_node.add(next_word) ## add to current q, wich would be removed when traversed completed
        
        word_dict -= q_node
        
        if found:
            return result
                            
    
    return -1 
            