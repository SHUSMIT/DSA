import math

def k_th_permu(n,k):
    k -= 1 
    ans = ''
    number = [str(x) for x in range(1,n+1)]
    while(True):
        
        ans = ans + number[k//math.factorial(n-1)]  ## we add that number which is in the k//(n-1) factorial postion
        number.pop(k//math.factorial(n-1))  ## we remove that number then update n,k
        
        if len(number) == 0:
            break
        
        k = k % math.factorial(n-1)
        n -= 1
    
    return ans
        
print(k_th_permu(4,17)) ## 3412