n = int(input())

ls = [input() for i in range(n)]

ls = list(set(ls)) # 중복제거
ls.sort() # 알파벳순 정렬
ls.sort(key=len) # 길이 순 정렬

for i in ls:
    print(i)