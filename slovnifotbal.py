def prep_count(words, index):
    count = {}
    for word in words:
        char = word[index]
        if char in count.keys(): 
            count[char] +=1
        else:
            count[char] = 1
    return count

firstLett =prep_count(["ahoj", "oko", "jol"],0)
lastLett =prep_count(["ahoj", "oko", "jol"],-1)

print(set(firstLett.keys()))
print(set(lastLett.keys()))
prunik = set(firstLett.keys()).intersection(set(lastLett.keys()))
print (prunik)
for i in prunik:
    value=firstLett[i]
    firstLett[i]-=value
    lastLett[i]-=value
    if firstLett [i] == 0:
        del firstLett[i]
    if lastLett [i] == 0:
        del lastLett[i]    
print (firstLett)
print (lastLett)

if prep_count(firstLett, lastLett):
    print("You cannot")
else:
    print("You can play")       
 