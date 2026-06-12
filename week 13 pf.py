def name():
    print("hamza")

name()

def info():
    print("name : hamza")
    print("address : ...")
    print("city : lahore")

info()
from logging import exception

def show(n):
    if n==0 or n==1:
        return 1
    else:
        # print(n)
        return n*show(n-1)

print(show(999))

# febonocci series

def show(n):
    if n==0 or n==1:
        return 1
    else:
        # print(n)
        return show(n-1)+show(n-2)

print(show(5))
try:
 name=int(input("enter any number : "))
 print("hello world")

except Exception as e:
    print(e)

# task 2
s = {1,2,3,3}
print(s)
s2= {1,2,3,"AYFA"}
print(s2)
f= {}
print(type(f))
q= set()
print(type(q))
a= set([1,2,3,4])
print(type(a))
set= {"CE","CS","IBM","ME","CE"}
for i in set:
    print(i)

# task 3

s1= {1,2,3,4}
s2= {1,2,3,4}
print(s2.issubset(s1))

#task 4

s1= {1,2,3}
s2= {'abdullah','ilyas',3}
a= s1.isdisjoint(s2)
print(a)

# task 5

s1= {'abdullah','hamza','obaid'}
s2= {24,(1,2,3),(1,2,3)}
s3= {'a','e','i'}
s= s1.update(s2)
print(s1,s2)

#task 6

s1={1,2,3}
s2= {'abdullah','ear'}
print((set.intersection(s1,s2)))

#task 7
set= {"CE","IBM","ME"}
set.clear()
print(type(set))

#task 8

s1= {1,2,3,4}
s2= {'abdullah',4,'ear'}
s3= {"lahore",'karachi',4}

common = s1 & s2 & s3
s1 -= common
s2 -= common
s3 -= common

print(s1)
print(s2)
print(s3)