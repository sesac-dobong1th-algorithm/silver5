n = int(input())

a, b = 1, 1 # n이 1,2일때의 피보나치 수
for i in range(3, n+1):
    a, b = b, a+b # a는 n-1, b=n
    
print(b)