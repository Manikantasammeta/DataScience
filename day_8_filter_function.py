
import functools

l=[1,2,3,4]
l1=[]
def fun(l):
    for i in l:
        if i%2==0:
            l1.append(i)
list2=filter(fun(l),l1)
print(list(list2))

#out put -->[2, 4]