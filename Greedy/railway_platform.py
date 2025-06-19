def minimum_railway(arrival,departure):
    # if arrival of one coinicdes with departure, then another platform required
    n = len(arrival)
    
    maxi = 0
    arrival.sort()
    departure.sort()
    a,d = 0,0
    counter = 0

    while a < n:
        if arrival[a] <= departure[d]: # arrival is before, platform req
            counter += 1
            maxi = max(maxi,counter)
            a += 1
        else: # departure has happened, so reduce the counter
            counter -= 1
            d += 1

    return maxi