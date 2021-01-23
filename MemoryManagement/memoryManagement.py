#MEMORY MANAGEMENT EXERCISE

from memOptimal import optimalAlgorithm 
from memClock import clockAlgorithm     
from memFIFO import fifoAlgorithm       

processAccessList = []
systemBits = 0
pageSize = 0 
ramAvailable = 0
pagesMemoryMappingAtMoment = 0
pageFrameAtAddressTime = 0
pageFrameAtAddress = 0

#Line 1 processList
#Line 2 systemBits (bits)
#Line 3 pageSize (bytes)
#Line 4 ramAv (kb)
#Line 5 memory mapping at moment (int)
#Line 6 page frame at address (HEX)
#Line 7 page frame at address time (int)

#Extract data from file
with open("../mmData.txt","r") as f:

    processAccessList = [int(x) for x in f.readline().strip('\n').split(",")]
    systemBits = int(f.readline().strip('\n'))
    pageSize = int(f.readline().strip('\n'))
    ramAvailable = int (f.readline().strip('\n'))
    pagesMemoryMappingAtMoment = int(f.readline().strip('\n'))
    pageFrameAtAddress = int(f.readline().strip('\n'),16)
    pageFrameAtAddressTime = int(f.readline().strip('\n'))


#Calculate Responses
numberOfVirtualPages = 2**systemBits // pageSize
numberOfPageFrames = ramAvailable*1024 // pageSize

optimalFail,optimalLists   = optimalAlgorithm(processAccessList,numberOfPageFrames)
clockFail,clockLists       = clockAlgorithm(processAccessList,numberOfPageFrames)
fifoFail,fifoLists         = fifoAlgorithm(processAccessList,numberOfPageFrames)

#Find page frame for each algorithm at moment and address
#Find 'vp' index in the above ^ memory mappings
vp = (pageFrameAtAddress // pageSize) #% numberOfPageFrames

pfOptimal = [x for x in range(0,numberOfPageFrames) if optimalLists[pageFrameAtAddressTime-1][x] == vp][0]
pfFIFO    = [x for x in range(0,numberOfPageFrames) if fifoLists[pageFrameAtAddressTime-1][x] == vp][0]
pfClock   = [x for x in range(0,numberOfPageFrames) if clockLists[pageFrameAtAddressTime-1][x] == vp][0]

#Print them out nicely
print("="*40)
print(f"Access list (comma separated) : {processAccessList}")
print(f"System bits (bit)             : {systemBits}")
print(f"Page size (bytes)             : {pageSize}")
print(f"Ram available (kb)            : {ramAvailable}")
print(f"Mapping at moment (int)       : {pagesMemoryMappingAtMoment}")
print(f"Page frame at address (hex)   : dec: {pageFrameAtAddress} hex :{hex(pageFrameAtAddress)}")

print("="*40)
print(f"a) Number of virtual pages is: {numberOfVirtualPages}\n   Number of page frames is: {numberOfPageFrames}")

print(f"b) \nOptimal failure count: {optimalFail}")
prevOptimal = []
for i,x in enumerate(optimalLists):
    if x != prevOptimal:
        if i == 0:
            print(f'>---|')
            print(f'    |--t{str(i).ljust(3)}',x)
        else:
            print(f'    |--t{str(i).ljust(3)}',x)
    prevOptimal = x

print(f"\nFIFO failure count: {fifoFail}")
prevFIFO = []
for i,x in enumerate(fifoLists):
    if x != prevFIFO:
        if i == 0:
            print(f'>---|')
            print(f'    |--t{str(i).ljust(3)}',x)
        else:
            print(f'    |--t{str(i).ljust(3)}',x)
    prevOptimal = x

print(f"\nClock failure count: {clockFail}")
prevClock = []
for i,x in enumerate(clockLists):
    if x != prevClock:
        if i == 0:
            print(f'>---|')
            print(f'    |--t{str(i).ljust(3)}',x)
        else:
            print(f'    |--t{str(i).ljust(3)}',x)
    prevClock = x

print(f"c) Optimal pages memory mapping at moment {pagesMemoryMappingAtMoment} : {optimalLists[pagesMemoryMappingAtMoment-1]}")
print(f"   FIFO pages memory mapping at moment {pagesMemoryMappingAtMoment}    : {fifoLists[pagesMemoryMappingAtMoment-1]}")
print(f"   Clock pages memory mapping at moment {pagesMemoryMappingAtMoment}   : {clockLists[pagesMemoryMappingAtMoment-1]}")
print(f"d) The virtual page number is: {vp}")
print(f"   Corresponding page frame number at address {pageFrameAtAddress} moment {pageFrameAtAddressTime} for optimal: { pfOptimal }")
print(f"   Corresponding page frame number at address {pageFrameAtAddress} moment {pageFrameAtAddressTime} for fifo   : { pfFIFO }")
print(f"   Corresponding page frame number at address {pageFrameAtAddress} moment {pageFrameAtAddressTime} for clock  : { pfClock }")
print("="*40)
