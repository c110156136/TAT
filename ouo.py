from random import random
import random

tmp=[3,4,5]
qwq=(3,4,5)

k="c1101561"
d=[]
for i in range(1,60):
    d.append(k+'{0:02d}'.format(i))
grade=[]
for i in range(1,60):
    grade.append(random.randint(0,100))
tmp2={"c110156136":70,"c110156101":80}
print(grade[0])
print(tmp2["c110156136"])
tmp2["c110156166"]=69
tmp3={}
for i in range(len(grade)):
    tmp3[d[i]]=grade[i]