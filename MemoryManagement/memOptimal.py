def search(key,fr):
    for i in range(0,len(fr)):
        if fr[i] == key:
            return True 
    return False 

def predict(pg,fr,index):
    res = -1 
    far = index 
    
    for i in range(0,len(fr)):
        j = index 

        while j < len(pg):
            if fr[i] == pg[j]:
                if j > far:
                    far = j
                    res = i 
                break 
            j+=1
        if j == len(pg):
            return i 
    return 0 if res == -1 else res


def optimalAlgorithm(pg,fn,mappingMoment):
    hits=0
    fr = []
    frLists = []
    for i in range(0,len(pg)):

        if search(pg[i],fr):
            hits+=1
        else:
            if len(fr) < fn:
                fr.append(pg[i])
            else:
                j = predict(pg,fr,i+1)
                fr[j] = pg[i]
            
        frLists.append(fr.copy())

    return len(pg)-hits,frLists

