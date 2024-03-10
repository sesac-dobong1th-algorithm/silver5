N = int(input())
candidates = []
for _ in range(N):
    candidates.append(int(input()))

cnt = 0
if N == 1:
    pass
else : 
    while candidates[0] <= max(candidates[1:]):
        candidates[0] += 1
        candidates[candidates[1:].index(max(candidates[1:]))+1] -= 1
        cnt += 1
    
print(cnt)