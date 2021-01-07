#PROCESS SCHEDULING EXERCISE SHORTEST JOB FIRST

from queue import Queue 

pCount = 0
currTime = 0
prevTime = currTime
pArrival= []
pBurst =[]
pQueue = Queue()
pUsed = []

#Extract data from file
with open("scData.txt","r") as f:

    while True:
        line = f.readline().strip('\n')

        if not line:
            break

        pCount+=1
        pArrival.append(int(line.split(",")[0]))
        pBurst.append(int(line.split(",")[1]))

completionTime = [-1]*len(pArrival)
turnAroundTime = [-1]*len(pArrival)
waitTime = [-1]*len(pArrival)
responseTime = [-1]*len(pArrival)
allocatedAt = [-1]*len(pArrival)

pBurstCopy = pBurst.copy()


def startProc():

    minV = min(pArrival)

    for index,val in enumerate(pArrival):
        if minV == val:
            pUsed.append(index) #mark pid as used
            return index

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

sProc = startProc()

currTime = pArrival[sProc]

pQueue.put(sProc)

#While we still have burst,do this
while sum(pBurst) != 0:

    print(f"Ready queue at time {currTime} : {[x+1 for x in pQueue.queue]}")

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
    
    if responseTime[qProc] == -1:
        responseTime[qProc] = currTime - pArrival[qProc]

    #update time and burst 
    currTime += pBurst[qProc]
    pBurst[qProc] = 0

    #print(f"Time {prevTime} to {currTime} ==> P{qProc+1} ==> New Burst is {pBurst[qProc]}")

    #check if someone arrived meanwhile and put them in queue
    arrivedMeanwhile = getProcessesArrived(prevTime,currTime) #should also return an array specifying the exact arrival for each of the pids
        
    for p in arrivedMeanwhile:
        pQueue.put(p[1])
        print(f"Ready queue at time {p[0]} : {[x+1 for x in pQueue.queue]} => {p[1]+1} arrived")    

    #compute time because qProc finished
    completionTime[qProc] = currTime
    turnAroundTime[qProc] = completionTime[qProc] - pArrival[qProc]
    waitTime[qProc] = turnAroundTime[qProc] - pBurstCopy[qProc]
    print(f'P{qProc+1} just finished at time {currTime}')

    prevTime = currTime





#Print output
if True    :
    if False:
        print("AT - Arrival Time")
        print("BT - Burst Time")
        print("CT - Completion Time")
        print("TR - Turnaround Time")
        print("TW - Wait Time")
        print("RT - Response Time")

    print("======== AT === BT === CT === TR === TW === RT ========")
    for i in range(0,pCount):
        print(f"= P{str(i+1).ljust(4)}|{str(pArrival[i]).center(5)}| {str(pBurstCopy[i]).center(5)}|{str(completionTime[i]).center(5)}| {str(turnAroundTime[i]).center(5)}| {str(waitTime[i]).center(5)}| {str(responseTime[i]).center(5)}=")

    print('-'*55)

    print(f"Avg TR: {sum(turnAroundTime) / pCount}")
    print(f"Avg TW: {sum(waitTime) / pCount}")
    print(f"Avg RT: {sum(responseTime) / pCount}")
    print('='*55)
