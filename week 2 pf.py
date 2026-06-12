#task 1

binary_number = input("Enter binary number: ")
decimal = 0

for digit in binary_number:
    decimal = decimal * 2
    decimal = decimal + int(digit)

print("Decimal of", binary_number, "is", decimal)

#task 2

sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0

for ch in sentence:

    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):

        for v in "aeiouAEIOU":
            if ch == v:
                vowels += 1
                break
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)

#task 3

limit=int(input("Enter range: "))
prime_sum=0
print(f"Prime number up to {limit}:")

for num in range(2, limit+1):
    isPrime = True

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            isPrime = False
            break
        if num % i == 0:
            isPrime = False
            break

    if isPrime:
            print(num, end=" ")
            prime_sum += num
print(f"/nsum of these numbers: {prime_sum}")

#task 4

import random
import string

length = int(input("Enter password length: "))

use_upper = input("Include uppercase letters? (yes/no): ")
use_lower = input("Include lowercase letters? (yes/no): ")
use_digits = input("Include digits? (yes/no): ")
use_special = input("Include special characters? (yes/no): ")

characters = ""

if use_upper == "yes":
    characters += string.ascii_uppercase

if use_lower == "yes":
    characters += string.ascii_lowercase

if use_digits == "yes":
    characters += string.digits

if use_special == "yes":
    characters += string.punctuation

if characters == "":
    print("You must select at least one character type!")
else:
    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)

#task 5

for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(3, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
