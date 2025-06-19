def jump_game(arr):
    maxId = 0
    for i in range(len(arr)):
        if i > maxId:
            return False

        maxId = max(maxId , i + arr[i] ) ## max can be reached from that index

        if maxId >= len(arr) - 1:
            return True 
    
    return True