Count number of digits in an Integer using while loop

Ans:
number = int(input("Enter an integer: "))

count = 0

temp = abs(number)

while temp > 0:
    temp //= 10  
    count += 1
# If the number is 0, count should be 1
if number == 0:
    count = 1

print(f"The number of digits in {number} is: {count}")
