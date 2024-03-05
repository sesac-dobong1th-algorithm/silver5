#유명한 재귀함수 예제이지만 
#숫자가 매우 클때 안돌아가는 문제 발생하였다. << list화 시켜서 풀이했음

n = int(input())
fibo = [0, 1, 1]
for index in range(3,n+1):
    num = fibo[index-1] + fibo[index-2]
    fibo.append(num)
print(fibo[n])