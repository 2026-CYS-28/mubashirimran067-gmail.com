#task 1

a = int(input("enter obtained number: "))
b = int(input("enter total number: "))

c = (a/b)*100

print(c)
if b==0:
    print("invalid")
elif a>b:
    print("invalid")
elif c >= 90:
    print("Your Grade is A+")
elif c >= 85:
    print("Your Grade is A")
elif c >= 80:
    print("Your Grade is B+")
elif c >= 75:
    print("Your Grade is B")
elif c >= 70:
    print("Your Grade is B-")
elif c >= 65:
    print("Your Grade is C+")
elif c >= 60:
    print("Your Grade is C")
elif c >= 55:
    print("Your Grade is C-")
else:
    print("fail")



#task 2

obtained_marks = int(input("Enter your obtained marks:"))
total_marks = int(input("Enter total marks:"))

result = (obtained_marks/total_marks)*100
print("your marks percentage is:",result)