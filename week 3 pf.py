#task 1

def factorial(n):
    return 1 if n==0 else n*factorial(n-1)

def premutation(n,r):
    return factorial(n)//factorial(n-r)

def combination(n,r):
    return factorial(n)//(factorial(r)*factorial(n-r))
n=int(input("Enter the value of n: "))
r=int(input("Enter the value of r: "))

print("Premutation:",premutation(n,r))
print("Combination:",combination(n,r))

#task 2

largest = lambda a,b: a if a > b else b
def table(num,limit):
    for i in range(1,limit+1):
        print(num, "x",i,"=",num*i)

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
range_limit = int(input("Enter the table range:"))

large_num=largest(num1,num2)
print("largest number is:",large_num)
table(large_num,range_limit)

#task 3

upper= lambda s: s.upper()

def invert(text):
    print("reversed string: ",text[::-1])

string = input("Enter your string: ")

upper_string=upper(string)
print("Upper case string: ",upper_string)
invert(upper_string)

#task 4

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32
f=float(input("Enter your temperature in Fahrenheit: "))
print("In celsius: ",fahrenheit_to_celsius(f))
c=float(input("Enter your temperature in Celsius: "))
print("In fahrenheit: ",celsius_to_fahrenheit(c))

#task 5

def calculate_gpa(subjects):
    total_grade_points = 0
    total_credit_hours = 0

    for i in range(subjects):
        grade = float(input("Enter your grade_points: "))
        credit = float(input("Enter your credit hours: "))

        total_grade_points += grade * credit
        total_credit_hours += credit

    gpa = total_grade_points / total_credit_hours
    return gpa
subjects = int(input("Enter the number of subjects: "))
gpa = calculate_gpa(subjects)
print("Your gpa is: ", round(gpa,2))
