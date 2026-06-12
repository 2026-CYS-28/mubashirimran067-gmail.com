# task 1

def greet():
    print("Welcome to Python Programming")

greet()
greet()

#task 2

def displayname(name):
    print("Hello", name)

name = input("Enter your name: ")
displayname(name)

#task 3

def addnumbers(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("sum:", addnumbers(num1, num2))

#task 4

def square(num):
    return num * num

num = int(input("Enter a number: "))
print("square of number is: ", square(num))

#task 5

def power(base,exponent=2):
    return base**exponent
n = int(input("enter a number: "))
m = int(input("enter a exponent power: "))
print("square", power(n))
print("power", power(n,m))

#task 6

def student(name,age):
    print("Student name:",name)
    print("Student age:",age)

student("Abdullah",20)

#task 7

def maximum(a,b,c):
    return max(a,b,c)
a = int(input("enter a number: "))
b = int(input("enter b number: "))
c = int(input("enter c number: "))
print("maximum number is: ", maximum(a,b,c))

#task 8

def total(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print("total = ",sum)
total(5,13,43,49,60)
total(2,8,10,46,5)

#task 9

def average(*numbers):
    total = 0
    for num in numbers:
        total = total + num

    average = total / len(numbers)
    print("average: ", average)
average(15,20,56,34)

#task 10

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("1.Add\n2.Subtract\n3.Multiply\n4.Divide")
choice = int(input("Enter your choice(1-4): "))
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if choice == 1:
    print("Result= ",add(num1,num2))
elif choice == 2:
    print("Result= ",sub(num1,num2))
elif choice == 3:
    print("Result= ",mul(num1,num2))
elif choice == 4:
    print("Result= ",div(num1,num2))
