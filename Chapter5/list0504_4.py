import datetime
import random
ALP =["A","B","C","D","E","F","G","H","I","J","K","L","M","N"
      ,"O","P","Q","R","S","T","U","V","W","X","Y","Z"]
r = random.choice(ALP)
alp = ""
for i in ALP:
    if i != r:
        alp += i
print(alp)
st = datetime.datetime.now()
print("抜けているアルファベットは？")
while True:
    ans = input()
    if ans == r:
        print("正解です")
        et = datetime.datetime.now()
        print(str((et-st).seconds)+"秒かかりました")
        break
    else:
        print("違います")