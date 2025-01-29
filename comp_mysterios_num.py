Imagine you have two mysterious numbers. Your task is to write a program that 
reveals which one of them is the bigger one. How will you solve this puzzle?

Ans:
def compare(a, b):
    if a > b:
        return "a is greater"
    elif b > a:
        return "b is greater"
    else:
        return "both are equal"

a = float(input("Enter a float value for a: "))
b = float(input("Enter a float value for b: "))
print(compare(a, b))
