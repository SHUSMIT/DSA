def print_recur(i,n):
    
    if(i>n):
        return
    
    print(i)
    
    return print_recur(i+1,n)

print(print_recur(0,3))

##################################

# its say n =3... 3 + 2 + 1 which is 3 + sum(2) then 2 + sum(1)
def sum_n(n):
    if(n==0):
        return 0
    if (n==1):
        return 1
        
    return n + sum_n(n-1)
        
print(sum_n(10))

####################

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

print(factorial(5))