#task 1

# Functions
def hello():
    print("Hello World")
hello()


def info():
    print("Name:abdullah\nSemester:1\nDepartment:Computer Engineering")
info()


def sum(a,b):
    return a+b
print(sum(a=1,b=2))

def sum(c,d):
    return c+d
print(sum(1,2))

print(len("abdullah"))
print(max(20,20))
print(min(-20,20))
print(type(5))
print(type(5.5))
print(type("a"))

a = float(input("Enter your input:"))
print(type(a))

def info(rollnumber,name):
    print(f"Hello {name},your roll number is {rollnumber}")
info(48,"Hamza shahid")
info(28,"abdullah")
info(45,"Hamza Shafiq")