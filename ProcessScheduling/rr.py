#PROCESS SCHEDULING EXERCISE ROUND ROBIN

from queue import Queue 

pCount = 0            #Total number of processes
qTime = 0             #Quantum time
currTime = 0          #Current scheduling time
prevTime = currTime   #Previous scheduling time
pArrival= []          #Process arrival list
pBurst = []           #Process burst list
pQueue = Queue()      #Process queue
pUsed = []            #Already queued processes list
granttList = []       #Keeps track of processes execution to construct GRANTT
contextSwitches = 0   #How many context switches did the RR perform

#Line ARRIVAL,BURST
# ...

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

#Handle user response
userResponse = input("Use optimal quantum time? [y/n]")

if userResponse == "y":
    qTime = round( 8/10 * (sum(pBurst) / pCount ) )
else:
    qTime = int(input("Input quantum time: "))
print()

#Initialize data arrays
completionTime = [-1]*len(pArrival)
turnAroundTime = [-1]*len(pArrival)
waitTime = [-1]*len(pArrival)
responseTime = [-1]*len(pArrival)
allocatedAt = [-1]*len(pArrival)
pBurstCopy = pBurst.copy()

#Preinitialize Round Robin
sProc = startProc()
currTime = pArrival[sProc]
pQueue.put(sProc)

print('='*21,' READY QUEUE ','='*20)

#While we still have bursts, do Round Robin
while sum(pBurst) != 0:
    

    l = [x+1 for x in pQueue.queue]
    print(f"Ready queue at time {str(currTime).center(3)} : {l}")

    qProc = pQueue.get()
  
    granttList.append((currTime,qProc))

    #Populate responseT array
    if responseTime[qProc] ==-1:
        responseTime[qProc] = currTime - pArrival[qProc]

    #Update time and burst  
    if pBurst[qProc] <= qTime:
        currTime += pBurst[qProc]
        pBurst[qProc] -= pBurst[qProc]
    else:
        currTime += qTime
        pBurst[qProc] -= qTime    

    #print(f"Time {prevTime} to {currTime} ==> P{qProc+1} ==> New Burst is {pBurst[qProc]}")

    #Check if someone arrived meanwhile and put them in queue
    arrivedMeanwhile = getProcessesArrived(prevTime,currTime)

    for p in arrivedMeanwhile:
        pQueue.put(p[1])
        ll = [x+1 for x in pQueue.queue]
        print(f"Ready queue at time {str(p[0]).center(3)} : {ll} => {p[1]+1} arrived") 

    #Put handle process back in queue or end it's life
    if pBurst[qProc] != 0:
        pQueue.put(qProc)
    elif pBurst[qProc] == 0:
        completionTime[qProc] = currTime
        turnAroundTime[qProc] = completionTime[qProc] - pArrival[qProc]
        waitTime[qProc] = turnAroundTime[qProc] - pBurstCopy[qProc]
        #print(f'P{qProc+1} just finished at time {currTime}')

    prevTime = currTime

#Print output
print("========= AT ==== BT ==== CT ==== TR ==== TW ==== RT ===")
for i in range(0,pCount):
    print(f"= P{str(i+1).ljust(4)}|",end='')
    print(f"{str(pArrival[i]).center(7)}|",end='')
    print(f"{str(pBurstCopy[i]).center(7)}|",end='')
    print(f"{str(completionTime[i]).center(7)}|",end='')
    print(f"{str(turnAroundTime[i]).center(7)}|",end='')
    print(f"{str(waitTime[i]).center(7)}|",end='')
    print(f"{str(responseTime[i]).center(7)}=")

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

print('='*22,' AVERAGES ','='*22)

print(f"= Avg TR (Turn Around)  : {sum(turnAroundTime) / pCount}")
print(f"= Avg TW (Wait Time)    : {sum(waitTime) / pCount}")
print(f"= Avg RT (Response Time): {sum(responseTime) / pCount}")
print(f"= Context switches      : {getContextSwitches()}")
print(f"= Quantum time          : {qTime}")
print('='*56)
