import random

ALP =["A","B","C","D","E","F","G"]
r = random.choice(ALP)
alp = ""
for i in ALP:
    if i != r:
        alp += i
print(alp)