def is_palindromme(i,s,n):
    if (i >= n//2):
        return True
    if s[i] != s[n-i-1]:
        return False
    return is_palindromme(i+1,s,n)

w = ['abcede' , 'abcba' , '1234' , '123454321']
for word in w:
    print(is_palindromme(0,word,len(word)))