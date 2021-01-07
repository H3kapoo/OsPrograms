from queue import Queue

def fifoAlgorithm(pages, frames,mappingMoment):
    n = len(pages)
    s = set()

    indexes = Queue()
    fr = []

    page_faults = 0

    for i in range(n):
    
        fr.clear()
        if (len(s) < frames):
            if (pages[i] not in s):
                s.add(pages[i])
                page_faults += 1
                indexes.put(pages[i])
        else:
            if (pages[i] not in s):

                val = indexes.queue[0]
                indexes.get()
                s.remove(val)
                s.add(pages[i])
                indexes.put(pages[i])
                page_faults += 1
            
        for x in list(indexes.queue):
            fr.append(x)

    return page_faults,fr
