maxList = []
needList = []
needListCopy = []
allocList = []
pCount = 0
availableRes = 0
resolveList = []
minAvailableRes = 0

#Line 1 MAX
#Line 2 ALLOC List

#Extract data from file
with open("../dlData.txt","r") as f:
    maxList = [int(x) for x in f.readline().strip('\n').split(",")]
    allocList = [int(x) for x in f.readline().strip('\n').split(",")]
    pCount = len(maxList)

#Calculate need list
for i in range(0,pCount):
    minAvailableRes += maxList[i]-1
    needList.append(maxList[i] - allocList[i])
needListCopy = needList.copy()

#Minimum available resources so that the system will not go into deadlock
#no matter the order
availableRes = min(needList)   #Minim

print("="*36)
print(f"= Min initial available resources: {availableRes}")

#While we still have processes to allocate resources to, run Banker's
iterCount=0
while len(resolveList) != pCount:
    if iterCount > pCount+2:
        print("= No safe state found!")
        break
    #Find suitable process based on available res
    for p in range(0,pCount):
        if p+1 not in resolveList and needList[p] <= availableRes:
            resolveList.append(p+1)
            availableRes+=allocList[p]
            needList[p] = 0
            break    
    iterCount+=1


#Print output
print("========= ALLOC === MAX === NEED ===")
for i in range(0,pCount):
    print(f"= P{str(i+1).ljust(4)}|",end='')
    print(f"{str(allocList[i]).center(8)}|",end='')
    print(f"{str(maxList[i]).center(8)}|",end='')
    print(f"{str(needListCopy[i]).center(8)} =")

print("="*14,"SAFE SEQ","="*13)
print(resolveList)
print("="*15,"STATS","="*15)
print(f"= Min value for total av. resources: {sum(needListCopy)-pCount+1}")
print("="*37)
