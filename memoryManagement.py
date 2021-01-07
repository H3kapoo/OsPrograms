#MEMORY MANAGEMENT EXERCISE

from memOptimal import optimalAlgorithm #most credit goes to Geeks4Geeks
from memClock import clockAlgorithm     #most credit goes to Geeks4Geeks
from memFIFO import fifoAlgorithm       #most credit goes to Geeks4Geeks

#Get Inputs From User
processAccessList = [int(x) for x in input("Input access to the pages (as list comma separated): ").split(",")]

systemBits = int(input("How many bits does the machine have (bit): "))

pageSize = int(input("Page size (bytes): "))

ramAvailable = int(input("Input machine RAM size (kb): "))

pagesMemoryMappingAtMoment = int(input("Memory mapping at moment (int): "))

pageFrameAtAddress = int(input("Corresponding page frame at address (hex): "),16)

#Calculate Responses
numberOfVirtualPages = 2**systemBits // pageSize
numberOfPageFrames = ramAvailable*1024 // pageSize

optimalFail,optimalPagesMemoryMapping = optimalAlgorithm(processAccessList,numberOfPageFrames,pagesMemoryMappingAtMoment)
clockFail,clockPagesMemoryMapping =clockAlgorithm(processAccessList,numberOfPageFrames,pagesMemoryMappingAtMoment)
fifoFail,fifoPagesMemoryMapping = fifoAlgorithm(processAccessList,numberOfPageFrames,pagesMemoryMappingAtMoment)

#Print them out nicely
print("="*40)
print(f"a) Number of virtual pages is: {numberOfVirtualPages}\n   Number of page frames is: {numberOfPageFrames}")
print(f"b) Optimal failure count: {optimalFail}")
print(f"   Clock failure count: {clockFail}")
print(f"   FIFO failure count: {fifoFail}")
print(f"c) Optimal pages memory mapping at moment {pagesMemoryMappingAtMoment} : {optimalPagesMemoryMapping}")
print(f"   Clock pages memory mapping at moment {pagesMemoryMappingAtMoment} : {clockPagesMemoryMapping}")
print(f"   FIFO pages memory mapping at moment {pagesMemoryMappingAtMoment} : {fifoPagesMemoryMapping}")


# D) IS FOR SURE WRONG IDK HOW TO FIX ;0
print(f"d) Corresponding page frame number at address {pageFrameAtAddress} : { pageFrameAtAddress//pageSize }")

print("="*40)