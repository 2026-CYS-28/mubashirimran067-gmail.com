s = {1,2,3,3}
print(s)

#give dictionary type
s = {}
print(type(s))

#give set type
s = set()
print(type(s))

x = set([1,2,3])
print(x)
print(type(x))

s = {1,2,3,3}
print(s)

# give dictionary type
s = {}
print(type(s))

# give set type
s = set()
print(type(s))

x = set([1,2,3])
print(x)
print(type(x))

 s = {"CE","SE","CS","CIVIL","ELECTRICAL","SE"}
for i in s:
    print(i)
if "CE" in s:
    print("CE")
s.add("ME")
s.discard("CS")
s.discard("SE")
s.discard("mathematics")
s.remove("mathematics")
s.pop()
s.clear()
print(s)
print(type(s))


s1 = {"Hamza","Obaid","Abdullah","Ahmad"}
s2 = {45,47,28,49}
s1.update(s2)
print(s1)
print(s2)
z=s1.union(s1)
print(z)

s3 = {1,"cat",(1,2,3)}
print(s3)

s1={1,2,3}
s2={"UET","CS","CE"}
s3={7,5,9}
c=s1.intersection(s2)
print(c)

s1={1,2,3,4}
s2={"UET","CS","CE",2}
s3={1,2,3}
s1.intersection_update(s2)
s1.discard(2)
s2.discard(2)
z=s1.difference(s2)
m=s1.symmetric_difference(s2)
z=s1.isdisjoint(s2)
print(m)
print(z)
print(s1)
print(s2)
z=s1.isdisjoint(s3)
z = s1.issubset(s3)
z = s3.issubset(s1)
print(z)