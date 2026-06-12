#task 1

# def hello():
#     print ("hello world")
# print(hello(4))
def sum(a,b):
    return a+b
c=4
d=6
print(sum(c,d))
print("my name is abdullah")
a= "my name is abdullah"
print(len(a))
print(min(-20,20))
print(type(a))

#task 2

value = input("Enter something: ")
try:
    int(value)
    print("Integer")
except ValueError:
    try:
        float(value)
        print("Float")
    except ValueError:
        print("String")

#task 3

def info(name, rollno):
    print(f"My name is {name} and my roll number is {rollno}.")


info('abdullah', '28')

