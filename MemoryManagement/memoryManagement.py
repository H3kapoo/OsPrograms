#MEMORY MANAGEMENT EXERCISE

from memOptimal import optimalAlgorithm 
from memClock import clockAlgorithm     
from memFIFO import fifoAlgorithm       

processAccessList = []
systemBits = 0
pageSize = 0 
ramAvailable = 0
pagesMemoryMappingAtMoment = 0
pageFrameAtAddress = 0

#Line 1 processList
#Line 2 systemBits (bits)
#Line 3 pageSize (bytes)
#Line 4 ramAv (kb)
#Line 5 memory mapping at moment (int)
#Line 6 page frame at address (HEX)

#Extract data from file
with open("../mmData.txt","r") as f:

    processAccessList = [int(x) for x in f.readline().strip('\n').split(",")]
    systemBits = int(f.readline().strip('\n'))
    pageSize = int(f.readline().strip('\n'))
    ramAvailable = int (f.readline().strip('\n'))
    pagesMemoryMappingAtMoment = int(f.readline().strip('\n'))
    pageFrameAtAddress = int(f.readline().strip('\n'),16)


#Calculate Responses
numberOfVirtualPages = 2**systemBits // pageSize
numberOfPageFrames = ramAvailable*1024 // pageSize

optimalFail,optimalPagesMemoryMapping = optimalAlgorithm(processAccessList,numberOfPageFrames,pagesMemoryMappingAtMoment)
clockFail,clockPagesMemoryMapping     = clockAlgorithm(processAccessList,numberOfPageFrames,pagesMemoryMappingAtMoment)
fifoFail,fifoPagesMemoryMapping       = fifoAlgorithm(processAccessList,numberOfPageFrames,pagesMemoryMappingAtMoment) #TODO: gives wrong output

#Find page frame for each algorithm at moment and address
#Find 'vp' index in the above ^ memory mappings
vp = pageFrameAtAddress // pageSize
pfOptimal = [x for x in range(0,numberOfPageFrames) if optimalPagesMemoryMapping[x] == vp]
pfFIFO = [x for x in range(0,numberOfPageFrames) if fifoPagesMemoryMapping[x] == vp]
pfClock = [x for x in range(0,numberOfPageFrames) if clockPagesMemoryMapping[x] == vp]


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
print(f"b) Optimal failure count: {optimalFail}")
print(f"   FIFO failure count: {fifoFail}")
print(f"   Clock failure count: {clockFail}")
print(f"c) Optimal pages memory mapping at moment {pagesMemoryMappingAtMoment} : {optimalPagesMemoryMapping}")
print(f"   FIFO pages memory mapping at moment {pagesMemoryMappingAtMoment}    : {fifoPagesMemoryMapping}")
print(f"   Clock pages memory mapping at moment {pagesMemoryMappingAtMoment}   : {clockPagesMemoryMapping}")
print(f"d) The virtual page number is: {vp}")
print(f"   Corresponding page frame number at address {pageFrameAtAddress} for optimal: { pfOptimal[0] }")
print(f"   Corresponding page frame number at address {pageFrameAtAddress} for fifo   : { pfFIFO[0] }")
print(f"   Corresponding page frame number at address {pageFrameAtAddress} for clock  : { pfClock[0] }")
print("="*40)
