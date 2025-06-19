def isPal(string):
    return string == string[::-1]
    
def PalSubs(idx,string,path,ans):
    if idx == len(string):
        ans.append(path[:])
        return
    
    for i in range(idx,len(string)):
        if isPal(string[idx:i+1]):  ## check the substring
            path.append(string[idx:i+1]) ## take forward
            PalSubs(i+1,string,path,ans)  ## check further for next part by slicing 
            path.pop  ##bakc track
    
ans = []
path = []
string = 'aabb'
PalSubs(0,string,path,ans)
print(ans)
        
    