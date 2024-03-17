import sys

k = int(input())
cn = 1
cl = []

for i in range(k):
    score_info =list(map(int, sys.stdin.readline().split()))
    
    cl = score_info[1:]
    cl.sort(reverse=True)
    
    largest_gap = 0
    
    for j in range (len(cl)-1):
        if cl[j] - cl[j+1] > largest_gap:
            largest_gap = cl[j] - cl[j+1]


    print("Class", i+1)
    

    print(f"Max {cl[0]}, Min {cl[-1]}, Largest gap {largest_gap}")
