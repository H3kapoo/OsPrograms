maxList = []
needList = []
needListCopy = []
allocList = []
pCount = 0
availableRes = 0
resolveList = []
resolved = 0

#Line 1 MAX
#Line 2 ALLOC List

#Extract data from file
with open("../dlData.txt","r") as f:
    maxList = [int(x) for x in f.readline().strip('\n').split(",")]
    allocList = [int(x) for x in f.readline().strip('\n').split(",")]
    pCount = len(maxList)

#Calculate need list
for i in range(0,pCount):
    needList.append(maxList[i] - allocList[i])
needListCopy = needList.copy()

#Minimum available resources so that the system will not go into deadlock
#Start at min(NEED_LIST)
availableRes = min(needList)
aCopy = availableRes

#run Banker's to find min resources needed
while True:
    aCopy = availableRes
    print(f"Available resources {availableRes} attempt:")
    for i in range(0,pCount):
        #Find suitable process based on available res
        for p in range(0,pCount):
            if p+1 not in resolveList and needList[p] <= availableRes:
                resolveList.append(p+1)
                availableRes += allocList[p]
                print(f"Process {p+1} needed {needList[p]} now scheduled. It released {allocList[p]}. Available res: {availableRes}")
                
    #break 
    if len(resolveList) == pCount:
        print("DONE")
        break
    print("INCREMENTING")
    availableRes = aCopy+1
    needList = needListCopy.copy()
    resolveList.clear()
            


#Print output
print("========= ALLOC === MAX === NEED ====")
for i in range(0,pCount):
    print(f"= P{str(i+1).ljust(4)}|",end='')
    print(f"{str(allocList[i]).center(8)}|",end='')
    print(f"{str(maxList[i]).center(8)}|",end='')
    print(f"{str(needListCopy[i]).center(8)}  =")

print("="*14,"SAFE SEQ","="*13)
print(resolveList if len(resolveList) == pCount else f"None for available resources {aCopy}")
print("="*15,"STATS","="*15)
print(f"Min av. res. after initial allocation: {aCopy}")
print(f"Total min resources needed           : { availableRes}")
print("="*37)
