import random

b = []
cnt_m = 0
for j in range(1,100):
    a = []
    for i in range(1,100):
        cnt = 0
        while True:
            r = random.randint(1,100)
            #print(r)
            cnt += 1
            cnt_m += 1
            if r == 77:
                a.append(cnt)
                break
    ave = sum(a)/len(a)
    #print(a)
    #print(ave,max(a),min(a))
    b.append(ave)
#print(b)
print(sum(b)/len(b))
print(cnt_m)
#print(str(cnt)+"回目でレアキャラをゲット")