from collections import deque

def word_ladder(arr, start, end):
    
    n = len(arr)
    word_dict = set(arr) ## create a set ( visited array)
    q = deque()
    q.append((start,1)) ## add to q
    
    while q:
        word,path = q.popleft()
        
        if word == end:
            return path ## reached so return
            
        for i in range(n):
            alphabets = 'abcdefghijklmnopqrstuvwxyz' ## string immutable, slicing possible
            for c in alphabets: ## we slice upto i-1 add the req into i and then go from i+1 to end, as strings are not array
                next_word = word[:i] + c + word[i+1:]  
                if next_word in word_dict:  ## if present
                    q.append((word,path+1)) ## add it to q with path ++
                    word_dict.remove(next_word)  ## remove it if found
    
    return -1 
            