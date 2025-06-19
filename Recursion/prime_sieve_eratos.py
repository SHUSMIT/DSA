import math
# Online Python - IDE, Editor, Compiler, Interpreter
n = int(input('Enter 1st number: '))
#[] --> n sie array, all 1, then loop from i=1 to root n and j = i*i to j<=n; j += j (j multiples) .. if number present put it 0
def prime(n):
    arr = [1 for _ in range(n+1)]
    for i in range(2,int(math.sqrt(n)) + 1):
        if arr[i]:
            for j in range(i*i , n+1, i):
                arr[j] = 0
    return arr
    
prime_arr = prime(n)

for i in range(2,n+1):
    if prime_arr[i]:
        print(i)
