
# Online Python - IDE, Editor, Compiler, Interpreter
x  = int(input())
n = int(input())

def pow(x,n):
    ans = 1
    while(n):
        if not(n%2):
            #Even
            n = n//2
            x = x * x
            # basically (2x)^(n/2)
        else:
            #odd
            #bascially x * (2x)^(n-1)/2 ... multiply to ans * x
            ans = ans * x 
            n = n - 1 
    return ans

print(pow(x,n))

    
            