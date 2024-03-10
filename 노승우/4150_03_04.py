'''
import sys
sys.setrecursionlimit(10**6)

요셉님이 알려주셨는데 백준에서는 피보나치의 제한이 걸려있다합니다
백준 코드 제출시에는 최대 수인 10^6으로 해두었습니다
'''
import time
import timeit
'''
피보나치 시간 차이를 알기위해 데코레이터를 만들어 비교

데코레이터란? 함수를 인자로 받아 다시 함수의 형태로 반환하는 함수
'''
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() # 함수 실행 전 시간 기록
        result = func(*args, **kwargs) # *는 가변인자 **연속되는 키워드를 딕셔너리 형태로 저장 절대 순서를 바꿔쓰면안됨
        end_time = time.time()
        print(f'실행 시간:{end_time - start_time:.4f}초')
        return result
    return wrapper
# 데코레이터 예시
# # 예제 사용
# @timeit
# def example_function(n):
#     s = 0
#     for i in range(n):
#         s += i
#     return s

# # 함수사용

# example_function(1_000_000)
user = int(input()) 
@timeit
def test_fibo(n):
    if n==1 or n==2:
        return n
    else:
        return test_fibo(n-1) + test_fibo(n-2)
    

# print(test_fibo(user)) # 100입력시 넘 오래걸려서 측정불가

dictionary = {1: 1, 2: 1}
@timeit
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output
    
print(fibonacci(user)) #100입력 실행 시간:0.0193초

'''
아래는 요셉님이 스레드에 올려주신 행렬곱에 대한 연산입니다.

#2차원 리스트
def mul(A: list, B: list) -> list:
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]

#####

# 1차원 리스트
def mul(A: list, B: list) -> list:
    return [
        A[0] * B[0] + A[1] * B[1],
        A[0] * B[1] + A[1] * B[2],
        A[1] * B[1] + A[2] * B[2],
    ]

'''

