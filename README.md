# Process Scheduling
### 1.Exercise statement
![Imgur Image](https://i.imgur.com/L2hgxm3.png)

### 2.Available algorithms
**RR** (Round Robin) <br/> **SJF** (Shortest Job First) <br/> **SRTN** (Shortest Running Time Next) <br/> **FCFS** (First Come First Served)

### 3.How to feed the program
The program reads data from the file ```scData.txt``` as follows: <br/>
| Arrival    | Burst    |
|------------|----------|
| P1 Arrival | P1 Burst |
| ...        | ...      |
| Pn Arrival | Pn Burst |

### 4.What the program computes
```1.Process queue log``` <br/>
```2.GRANTT diagram``` <br/>
```3.Turn around time and Wait time for each process``` <br/>
```4.Avg turn around / wait time / response time``` <br/>
```5.Context switches```

### 5.Program output example for Round Robin

<details>

<summary>Click here to see the output</summary>

![Imgur Image](https://i.imgur.com/o3q3zQH.png)

</details>

# Memory Management
### 1.Exercise statement
![Imgur Image](https://i.imgur.com/Rm9s3ar.png)

### 2.Available algorithms
**Optimal** <br/>
**FIFO** <br/>
**Clock (Second Chance)**

### 3.How to feed the program
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

### 4.What the program computes
```1.Number of virtual pages & page frames``` <br/>
```2.Failure count with process queue log``` <br/>
```3.Memory mapping description at specified moment``` <br/>
```4.Corresponding page frame at specified address and moment``` 

### 5.Program output example

<details>

<summary>Click here to see the output</summary>

![Imgur Image](https://i.imgur.com/dEU83OF.png)
![Imgur Image](https://i.imgur.com/ck0Vr2p.png)

</details>

# Deadlocks
### 1.Exercise statement
![Imgur Image](https://i.imgur.com/qiEWhY7.png)

### 2.Available algorithms
**Banker's**

### 3.How to feed the program
###### Note: ```lists``` are comma separated
The program reads data from the file ```dlData.txt``` as follows: <br/>
| Line # | What to input               |
|--------|-----------------------------|
| Line 1 | MAX list                    |
| Line 2 | a1) ALLOC list              |
| Line 3 | a2) ALLOC list              |
| Line 4 | b) ALLOC list               |
| Line 5 | Process given at b2)        |
| Line 6 | Additional resources at b2) |

### 4.What the program computes
```1.Minimum number of total resources & steps log for a1) and a2)``` <br/>
```2.Resources to split for a deadlock to occur at b1)``` <br/>
```3.Second process so that the state is still safe for b2)``` <br/>
```4.Corresponding page frame at specified address and moment``` 

### 5.Program output example

<details>

<summary>Click here to see the output</summary>

None yet

</details>





