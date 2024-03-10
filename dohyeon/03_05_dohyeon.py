
# n개 단어 입력
# 짧은것부터 정렬
# 길이가 짧으면 사전순
# 겹치면 하나만 남기고 제거

#%%
n = int(input())
list_word = list()
for _ in range(n):
    list_word.append(str(input()))
#중복제거
list_word = list(set(list_word))    
#sort
list_word.sort()
#먼저 sort하고 그다음 길이 정렬해야 알파벳 순 정렬이 안 무너짐.
list_word = sorted(list_word,key=len)

for word in list_word:
    print(word)
