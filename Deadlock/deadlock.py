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

#Returns safe seq (if any) for the specific parameters
def bankerAlg(_max,_alloc,work,log):
    _pCount = len(_max)
    _solved = []
    _need = []
    _workLog = []

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
        _workLog.append(work)

    if log:
        print("========= ALLOC === MAX === NEED =====")
        for i in range(0,_pCount):
            print(f"= P{str(i+1).ljust(4)}|",end='')
            print(f"{str(_alloc[i]).center(8)}|",end='')
            print(f"{str(_max[i]).center(8)}|",end='')
            print(f"{str(_need[i]).center(8)}   =")
        print("============== STEPS =================")

        for i,p in enumerate(_solved):
            print(f"Step {i+1}:")
            print(f"|-- Execute P{p+1}")
            print(f"    |-- Freed: {_alloc[p]}")
            print(f"    |-- Av. now: {_workLog[i]}")

    return [p+1 for p in _solved]

#Find minimum necessary work and return the total minimum necessary available work for a1)
#Also print the steps for the target work found
def solveA1_A2(_max,_alloc):
    initWork = 0

    while True:
        solved = bankerAlg(_max,_alloc,initWork,False)

        if len(solved) == 0:
            initWork+=1
        else:
            bankerAlg(_max,_alloc,initWork,True)
            break
    
    #Print output
    print("="*20,"STATS","="*20)
    print(f"Minimum resources needed after alloc     : {initWork}")
    print(f"Total minumum resources needed           : {sum(_alloc) + initWork}")
    print("="*47)

    return sum(_alloc) + initWork

#Computes the second process for subpoint b2)
def computeSecondProcess(firstProc,addedReq,work,_max,_alloc):
    _pCount = len(_max)
    index = 0
    _maxCopy = _max.copy()

    while True:
        _maxCopy[firstProc] += addedReq  
        if firstProc != index:
            print("Trying with process..",index+1)
            _maxCopy[index] += addedReq
            if len(bankerAlg(_maxCopy,_alloc,work,False)) != 0:
                return index
        if index < _pCount-1:
            index+=1
            _maxCopy = _max.copy()
        else:
            break
    return "[None]"


#Extract data from file
with open("../dlData.txt","r") as f:
    maxList     = [int(x) for x in f.readline().strip('\n').split(",")]
    allocList   = [int(x) for x in f.readline().strip('\n').split(",")]
    allocList2  = [int(x) for x in f.readline().strip('\n').split(",")]
    allocList3  = [int(x) for x in f.readline().strip('\n').split(",")]
    firstProc   = int(f.readline().strip('\n'))
    addReq      = int(f.readline().strip('\n'))

print("For a1) :")
b1Available = solveA1_A2(maxList,allocList)  #retrieve data for b1)

#An additional alloc for a2)..
allocList = [allocList[i] + allocList2[i] for i in range(0,len(allocList))]

print("\nFor a2) :")
solveA1_A2(maxList,allocList)

print("\nFor b1) :")
print("========= ALLOC === MAX === NEED =====")
for i in range(0,len(maxList)):
    print(f"= P{str(i+1).ljust(4)}|",end='')
    print(f"{str(allocList3[i]).center(8)}|",end='')
    print(f"{str(maxList[i]).center(8)}|",end='')
    print(f"{str(maxList[i] - allocList3[i]).center(8)}   =")
print("======================================")
print(f"Available resources to give: {b1Available}")
print(f"Split them across processes so that it causes a deadlock (i.e. it won't even start)")
print(f"(P0/{b1Available},P1/{b1Available}, ... x{len(maxList)})")

print("\nFor b2) :")

secondProc = computeSecondProcess(firstProc-1,addReq,b1Available,maxList,allocList3)

if secondProc != "[None]":
    maxList[firstProc-1] += addReq
    maxList[secondProc] += addReq

    print("New matrix after additional allocation:")
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

