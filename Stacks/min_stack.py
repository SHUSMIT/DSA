class stack:
    def __init__(self):
        self.arr = []
    
    def push(self,item):
        self.arr.append(item)
    
    def pop(self):
        if self.arr:
            return self.arr.pop()
        else:
            return None
    
    def top(self):
        if self.arr:
            return self.arr[-1]
    
    def size(self):
        return len(self.arr)
    
# store the cur min, and prev min
class min_stack: 
    def __init__(self):
        self.arr = []
    
    def push(self,val):

        if self.arr: # if not empty
            prev_val,prev_min = self.top() # get the min
            self.arr.append((val,min(val,prev_min))) # update the min
        else:
            self.arr.append((val,val))
    
    def get_min(self):
        cur_val,cur_min = self.top()

        return cur_min
    
    def pop(self):
        if self.arr:
            return self.arr.pop()
        else:
            return None
    
    def top(self):
        if self.arr:
            return self.arr[-1]
    
    def size(self):
        return len(self.arr)
    



