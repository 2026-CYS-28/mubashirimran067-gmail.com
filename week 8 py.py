#task 1

fruits = {"Apple":"saib","Mango":"aam","orange":"kino","Melon":"kharbooza"}

print(fruits["Mango"])

#task 2

c = int(input("Total number of students: "))

for i in range(c):
    d = input("Enter student name: ")
    e = input("Enter roll no: ")
    obtained_marks = int(input("Enter your marks: "))
    total_marks = int(input("Enter total marks: "))
    print("Student name:", d)
    print("Roll no:", e)

    if total_marks <= 0 or total_marks > 300:
        print("Enter valid numbers")
    elif obtained_marks > total_marks:
        print('Enter valid numbers')
    else:
        result = (obtained_marks / total_marks) * 100
        print(result)
        if result >= 90:
            print("A+")
        elif result >= 85:
            print('A-')
        elif result >= 80:
            print('B+')
        elif result >= 75:
            print('B-')
        elif result >= 70:
            print("C+")
        elif result >= 65:
            print("C-")
        elif result >= 60:
            print('F')

#task 3

c = int(input("Total number of students: "))
i = 1
while i <= c:

    d = input("Enter student name: ")
    e = input("Enter roll no: ")
    obtained_marks = int(input("Enter your marks: "))
    total_marks = int(input("Enter total marks: "))
    print("Student name:", d)
    print("Roll no:", e)

    if total_marks <= 0 or total_marks > 300:
        print("Enter valid numbers")
    elif obtained_marks > total_marks:
        print('Enter valid numbers')
    else:
        result = (obtained_marks/total_marks) * 100
        print(result)
        if result >= 90:
            print("A+")
        elif result >= 85:
            print('A-')
        elif result >= 80:
            print('B+')
        elif result >= 75:
            print('B-')
        elif result >= 70:
            print("C+")
        elif result >= 65:
            print("C-")
        elif result >= 60:
            print('F')

i = i + 1
input("Press enter to exit...")

#task 4

for i in range(1, 10):
    for j in range(i):
        print("*", end=" ")

    print()


