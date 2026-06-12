#task 1

for i in range(1,11):
    for j in range(1,11):
        print(i * j,end = "\t")
    print()

#task 2

for i in range(1,5):
    for j in range(4-i):
         print( " ", end = " ")
    for j in range(2 * i-1):
        print( "*", end = " ")
    print()

#task 3

for i in range(1,5):
    for j in range(4-i):
         print( "@", end = " ")
    for j in range(2*i-1):
        print( "*", end = " ")
    print()
