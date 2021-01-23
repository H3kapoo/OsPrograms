# Process Scheduling
### Exercise statement
![Imgur Image](https://i.imgur.com/L2hgxm3.png)

### Available algorithms
**RR** (Round Robin) <br/> **SJF** (Shortest Job First) <br/> **SRTN** (Shortest Running Time Next) <br/> **FCFS** (First Come First Served)

### How to feed the program
The program reads data from the file ```scData.txt``` as follows: <br/>
| Arrival    | Burst    |
|------------|----------|
| P1 Arrival | P1 Burst |
| ...        | ...      |
| Pn Arrival | Pn Burst |

### What the program computes
```1.Process queue log``` <br/>
```2.GRANTT diagram``` <br/>
```3.Turn around time and Wait time for each process``` <br/>
```4.Avg turn around / wait time / response time``` <br/>
```5.Context switches```

### Program output example for Round Robin
[Click here for output](https://i.imgur.com/o3q3zQH.png)

# Memory Management
### Exercise statement
![Imgur Image](https://i.imgur.com/Rm9s3ar.png)

### Available algorithms
**Optimal** <br/>
**FIFO** <br/>
**Clock (Second Chance)**

### How to feed the program
The program reads data from the file ```mmData.txt``` as follows: <br/>
| Line # | What to input                    |
|--------|----------------------------------|
| Line 1 | Comma separated process list     |
| Line 2 | System bits [bits]               |
| Line 3 | Page size [bytes]                |
| Line 4 | System RAM [kb]                  |
| Line 5 | Memory mapping at moment [int]   |
| Line 6 | Page frame at address [hex]      |
| Line 7 | Page frame at address time [int] |

### What the program computes
```1.Number of virtual pages & page frames``` <br/>
```2.Failure count with process queue log``` <br/>
```3.Memory mapping description at specifiet moment``` <br/>
```4.Corresponding page frame at specified address and moment``` 

### Program output example
[Click here for output part1](https://i.imgur.com/dEU83OF.png) <br/>
[Click here for output part2](https://i.imgur.com/ck0Vr2p.png)

