import re

texts = re.split(r'(?=[A-Z])', input())
for i in texts:
    if i and i[:4].lower() == 'what' and '?' in i:
        i = i.strip()
        i = i.replace('What', 'Forty-two')
        i = i.replace('?', '.')
        print(i)