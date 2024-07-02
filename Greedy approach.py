
def min_coins(d, amount):
    
    d.sort(reverse=True)
    
    
   
    coins = 0
    rem = amount
    i = 0 
    
    while rem > 0 and i < len(d):
        if rem >= d[i]:
            coins += 1
            rem -= d[i]
        else:
            i += 1
    
    return coins


d = [1, 5, 7]
bill = 18

min_coins = min_coins(d, bill)
print(f"Minimum coins {min_coins}")