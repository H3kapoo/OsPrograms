def replaceAndUpdate(x,arr,secondChance,frames,pointer):
    while True:
        if not secondChance[pointer]:
            arr[pointer] = x 
            return (pointer+1)%frames 
        secondChance[pointer] = False
        pointer = (pointer+1)%frames

def findAndUpdate(x,arr,secondChance,frames):
    for i in range(0,frames):
        if arr[i]==x:
            secondChance[i] = True 
            return True
    return False

def clockAlgorithm(pList,pageFrames,mappingMoment):
    pointer = 0
    pf = 0
    arr = [-1]*pageFrames
    secondChance = [False]*pageFrames
    frcopy = []
    frLists = []

    for i in range(0,len(pList)):
        if not findAndUpdate(pList[i],arr,secondChance,pageFrames):
            pointer = replaceAndUpdate(pList[i],arr,secondChance,pageFrames,pointer)
            pf+=1
        if i ==  mappingMoment:
            frcopy = arr.copy()
        frLists.append(arr.copy())

    return pf,frcopy,frLists

