def prep_count(words, index):
    count = {}
    for word in words:
        char = word[index]
        if char in count.keys(): 
            count[char] +=1
        else:
            count[char] = 1
    return count
def is_it_possible(words, index1, index2):
    firstLett =prep_count(words, index1)
    lastLett =prep_count(words, index2)
    prunik = set(firstLett.keys()).intersection(set(lastLett.keys()))
 ## print(set(firstLett.keys()))
## print(set(lastLett.keys()))
## print (prunik)
    for i in prunik:
        value=firstLett[i]
    firstLett[i]-=value
    lastLett[i]-=value
    if firstLett [i] == 0:
        del firstLett[i]
    if lastLett [i] == 0:
        del lastLett[i]    
 ## print (firstLett)
## print (lastLett)

words_to_control = ["ahoj", "nevim", "jo"]
index1 = 0
index2 = -1
if is_it_possible(words_to_control, index1, index2):
    print("You can play")
else:
    print("You cant, sorry :(")