#PROCESS SCHEDULING EXERCISE SHORTEST JOB FIRST

from queue import Queue 

pCount = 0              #Total number of processes
currTime = 0            #Current scheduling time
prevTime = currTime     #Previous scheduling time
pArrival= []            #Process arrival list
pBurst =[]              #Process burst list
pQueue = Queue()        #Process queue
pUsed = []              #Already queued processes list
granttList = []         #Keeps track of processes execution to construct GRANTT
contextSwitches = 0     #How many context switches did the RR perform

#Get first process that will be runned
def startProc():
    minV = min(pArrival)
    for index,val in enumerate(pArrival):
        if minV == val:
            pUsed.append(index) #mark pid as used
            return index

#Get the ordered by arrival time processes that arrived between [startTime,endTime]
def getProcessesArrived(startTime,endTime):
    pList = []
    pListVal = []
    for index,val in enumerate(pArrival):
        if index not in pUsed:
            if startTime <= val and val <= endTime:
                pList.append(index)
                pListVal.append(pArrival[index])
                pUsed.append(index)

    Z = [(x,y) for x,y in sorted(zip(pListVal,pList),key=lambda pair: pair[0])]
    return Z

#Does exactly what it says
def getContextSwitches():
    cs = 0
    for i in range(0,len(granttList)-1):
        if granttList[i][1] != granttList[i+1][1]:
            cs+=1
    return cs

#Extract data from file
with open("../scData.txt","r") as f:
    while True:
        line = f.readline().strip('\n')
        if not line:
            break
        pCount+=1
        pArrival.append(int(line.split(",")[0]))
        pBurst.append(int(line.split(",")[1]))

#Initialize data arrays
completionTime = [-1]*len(pArrival)
turnAroundTime = [-1]*len(pArrival)
waitTime = [-1]*len(pArrival)
responseTime = [-1]*len(pArrival)
allocatedAt = [-1]*len(pArrival)
pBurstCopy = pBurst.copy()

#Preinitialize Shortest Job First
sProc = startProc()
currTime = pArrival[sProc]
pQueue.put(sProc)

print('='*18,' READY QUEUE SJF ','='*19)
print(f"<{str(currTime).center(3)}> Put in {sProc+1}")

#While we still have burst,do this
while sum(pBurst) != 0:

    #same as fcfs but we take min burst from queue
    pQueueCopy =  Queue()
    minBurst = 9999
    qProc = -1
    pQueueList = [x for x in pQueue.queue]

    for p in pQueueList:
        pQueue.get()
        pQueueCopy.put(p)
        if pBurst[p] < minBurst:
            minBurst = pBurst[p]
            qProc = p

    for p in pQueueCopy.queue:
        if p != qProc:
            pQueue.put(p)

    print(f'<{str(currTime).center(3)}> Cross out {qProc+1}')
    
    granttList.append((currTime,qProc))

    #Populate responseT array
    if responseTime[qProc] == -1:
        responseTime[qProc] = currTime - pArrival[qProc]

    #Update time and burst 
    currTime += pBurst[qProc]
    pBurst[qProc] = 0

    #check if someone arrived meanwhile and put them in queue
    arrivedMeanwhile = getProcessesArrived(prevTime,currTime) #should also return an array specifying the exact arrival for each of the pids
        
    for p in arrivedMeanwhile:
        pQueue.put(p[1])
        print(f'<{str(p[0]).center(3)}> Put {p[1] + 1} in .Cross out {qProc+1} (if any)')

    #Compute time because qProc finished
    completionTime[qProc] = currTime
    turnAroundTime[qProc] = completionTime[qProc] - pArrival[qProc]
    waitTime[qProc] = turnAroundTime[qProc] - pBurstCopy[qProc]

    prevTime = currTime

#Print output
print('='*23,' GRANTT ','='*23)

#Print processes
print('  |',end='')
for p in granttList:
    print(f" P{p[1]+1} |",end='')
print()

#Print ^
print('  ^',end='')
for p in granttList:
    if p[1]+1 >= 10:
        print("     ^",end='')
    else:
        print("    ^",end='')
print()

#Print time stamp
i=0
for p in granttList:
    if p[1]+1 >= 10 and i != 0:
        print(f" {str(p[0]).center(5)}",end='')
    else:
        print(f"{str(p[0]).center(5)}",end='')
    i=1
print(f"{str(currTime).center(5)}")

print('='*22,"EXPLICIT",'='*22)
print("         Rt = Ct - Arr            Wt = Tr - Bst")
for i in range(0,pCount):
    print(f"P{i+1}:")
    print(f" |-> Rt: {str(completionTime[i]).center(0)}-{str(pArrival[i]).center(0)} = {str(turnAroundTime[i]).center(0)}")
    print(f" |-> Wt: {str(turnAroundTime[i]).center(0)}-{str(pBurstCopy[i]).center(0)} = {str(waitTime[i]).center(0)}")

print('='*22,' AVERAGES ','='*22)

print(f"= Avg TR (Turn Around)  : {sum(turnAroundTime) / pCount}")
print(f"= Avg TW (Wait Time)    : {sum(waitTime) / pCount}")
print(f"= Avg RT (Response Time): {sum(responseTime) / pCount}")
print(f"= Context switches      : {getContextSwitches()}")