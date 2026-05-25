# Assignment-3 : Loops
# 1. Print "Bright IT Career" 10 Times Using For Loop

for i in range(10):
    print("Bright IT Career")

# 2. Print Numbers from 1 to 20 Using While Loop
num = 1
while num <= 20:
    print(num)
    num += 1

# 3. Program for Equal and Not Equal Operators

a = 10
b = 20
print("a == b :", a == b)
print("a != b :", a != b)

# 4. Print Odd and Even Numbers

for i in range(1, 21):
    if i % 2 == 0:
        print(i, "is Even")

    else:
        print(i, "is Odd")

# 5. Largest Number Among Three Numbers

a = 25
b = 40
c = 15
if a > b and a > c:
    print("Largest Number:", a)

elif b > c:
    print("Largest Number:", b)

else:
    print("Largest Number:", c)


# 6. Print Even Numbers Between 10 and 20 Using While Loop
num = 10
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1


# 7. Print 1 to 10 Using Do-While Logic
# Python does not have do-while loop.
# We use while True to simulate it.
num = 1
while True:
    print(num)
    num += 1
    if num > 10:
        break

# 8. Armstrong Number Program
number = 153
temp = number
sum = 0
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10
if sum == number:
    print(number, "is Armstrong Number")

else:
    print(number, "is Not Armstrong Number")


# 9. Prime Number Program

number = 7
count = 0
for i in range(1, number + 1):
    if number % i == 0:
        count += 1

if count == 2:
    print(number, "is Prime Number")

else:
    print(number, "is Not Prime Number")


# 10. Palindrome Number Program

number = 121
temp = number
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10
if reverse == number:
    print(number, "is Palindrome")
else:
    print(number, "is Not Palindrome")


# 11. Check EVEN or ODD Using Match Case
number = 8
match number % 2:
    case 0:
        print("Even Number")

    case 1:
        print("Odd Number")

# 12. Print Gender Using Match Case
gender = "M"
match gender:
    case "M":
        print("Male")
    case "F":
        print("Female")
    case _:
        print("Invalid Input")
