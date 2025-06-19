def lemonade_change(bills): # bills arr that tells me denominations cutomer has
# each cost 5, return the remaining. if not possible, cant sell

# list of 5,10,20 
# 5 -> +5
# 10 -> +10 , -5
# 20 -> +20 , - (3 * 5) or -(10,5)

    n = len(bills)
    r = 0
    denomination = {5 : 0 , 10 : 0 }
    while r < n:
        
        if bills[r] == 5:
            denomination[5] += 1
        
        elif bills[r] == 10:
            denomination[10] += 1
            denomination[5] -= 1
            
            if denomination[5] < 0:
                return False
        
        else:
            if denomination[10] >= 1 and denomination[5] >= 1:
                denomination[10] -= 1 
                denomination[5] -= 1

            elif denomination[5] >= 3:
                denomination[5] -= 3

            else:
                return False
    
    return True