from queue import Queue

def fifoAlgorithm(pages, frames):
    n = len(pages)
    s = set()

    indexes = Queue()
    fr2 = []
    frLists = []

    page_faults = 0

    for i in range(n):
        
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
            fr2.append(x)
        fr2.reverse()
        frLists.append(fr2.copy())
        fr2.clear()

    return page_faults,frLists
