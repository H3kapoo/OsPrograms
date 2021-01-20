maxList = []
allocList = []
allocList2 = []
allocList3 = []
addReq = 0
firstProc = 0

#Line 1 MAX
#Line 2 ALLOC List 1
#Line 3 ALLOC List 2
#Line 4 ALLOC List 3
#Line 5 FIRST_PROC
#Line 6 ADD_REQUEST 

#Extract data from file
with open("../dlData.txt","r") as f:
    maxList     = [int(x) for x in f.readline().strip('\n').split(",")]
    allocList   = [int(x) for x in f.readline().strip('\n').split(",")]
    allocList2  = [int(x) for x in f.readline().strip('\n').split(",")]
    allocList3  = [int(x) for x in f.readline().strip('\n').split(",")]
    firstProc   = int(f.readline().strip('\n'))
    addReq      = int(f.readline().strip('\n'))


#Returns safe seq if any for the specific parameters
def bankerAlg(_max,_alloc,work,log = False):
    _pCount = len(_max)
    _solved = []
    _need = []

    for p in range(0,_pCount):
        _need.append(_max[p] - _alloc[p])

    for _iter in range(0,_pCount):
        maxFree = -1
        maxFreeInd = -1
        for p in range(0,_pCount):
            if p not in _solved and _need[p] <= work and _alloc[p] >= maxFree:
                maxFree = _alloc[p]
                maxFreeInd = p 

        if maxFreeInd == -1:
            return []
        
        _solved.append(maxFreeInd)
        work+=_alloc[maxFreeInd]
        
        if log:
            print()
            if len(_solved) != _pCount:
                print("========= ALLOC === MAX === NEED =====")
            for i in range(0,_pCount):
                if i not in _solved:
                    print(f"= P{str(i+1).ljust(4)}|",end='')
                    print(f"{str(_alloc[i]).center(8)}|",end='')
                    print(f"{str(_max[i]).center(8)}|",end='')
                    print(f"{str(_need[i]).center(8)}   =")
            if len(_solved) != _pCount:
                print("======================================")
            print(f"What happened:\nP{maxFreeInd+1} got executed.\nFreed {_alloc[maxFreeInd]}.\nPrev available {work-_alloc[maxFreeInd]}.\nNew available {work}")


    return [p+1 for p in _solved]

#Returns total number of resources after init alloc2 for subpoint b)
def a12(_max,_alloc,_alloc2 = []):
    initWork = 0

    while True:
        solved = bankerAlg(_max,_alloc,initWork)

        if len(solved) == 0:
            initWork+=1
        else:
            bankerAlg(_max,_alloc,initWork)
            break
    
    #Print stuff
    print("="*19,"SAFE SEQ","="*18)
    print(solved)
    print("="*20,"STATS","="*20)
    print(f"Minimum resources needed after alloc     : {initWork}")
    print(f"Total minumum resources needed           : {sum(_alloc) + initWork}")
    print("="*47)

    return sum(_alloc) + initWork -sum(_alloc2) 

print("For a1) :")
b1Available = a12(maxList,allocList,allocList3)

#An additional alloc..
allocList = [allocList[i] + allocList2[i] for i in range(0,len(allocList))]

print("\nFor a2) :")
a12(maxList,allocList)

print("\nFor b1) :")
print("========= ALLOC === MAX === NEED =====")
for i in range(0,len(maxList)):
    print(f"= P{str(i+1).ljust(4)}|",end='')
    print(f"{str(allocList3[i]).center(8)}|",end='')
    print(f"{str(maxList[i]).center(8)}|",end='')
    print(f"{str(maxList[i] - allocList3[i]).center(8)}   =")
print("======================================")
print(f"Available resources to give: {b1Available}")
print(f"Split them across processes so that it causes a deadlock")
print(f"({b1Available}/x,{b1Available}/y, ... x7)")

print("\nFor b2) :")

#Computes the second process for subpoint b2)
def b2(process,addedReq,work,_max,_alloc):
    _pCount = len(_max)
    index = 0
    _maxCopy = _max.copy()

    while True:
        _maxCopy[process] += addedReq  
        if process != index:
            print("Trying with process..",index+1)
            _maxCopy[index] += addedReq
            if len(bankerAlg(_maxCopy,_alloc,work)) != 0:
                return index
        if index < _pCount-1:
            index+=1
            _maxCopy = _max.copy()
        else:
            break
    return "[None]"

secondProc = b2(firstProc-1,addReq,b1Available,maxList,allocList3)

if secondProc != "[None]":
    maxList[firstProc-1] += addReq
    maxList[secondProc] += addReq

    print("========= ALLOC === MAX === NEED =====")
    for i in range(0,len(maxList)):
        print(f"= P{str(i+1).ljust(4)}|",end='')
        print(f"{str(allocList3[i]).center(8)}|",end='')
        print(f"{str(maxList[i]).center(8)}|",end='')
        print(f"{str(maxList[i] - allocList3[i]).center(8)}   =")
    print("======================================")
    print(f"{addReq} additional resources added to P{firstProc} MAX")
    print(f"If P{secondProc+1} gets an additional {addReq} resources, the system is still safe, MAX = {maxList[secondProc]}")
else:
    print(f"{addReq} additional resources added to P{firstProc} MAX")
    print(f"No process can be granted an additional {addReq} and be safe")

