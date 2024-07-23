from random import randint
from statistics import mean
acclist=[]
for i in range(10):
    this_acc = randint(0,1)
    acclist.append(this_acc)
accuracy_rate = mean(acclist)
print(acclist)
print(accuracy_rate)