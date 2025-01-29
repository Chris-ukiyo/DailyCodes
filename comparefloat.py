Compare Floats Up to Three Decimals

Ans:
def compare_floats(a, b):

    a_int = int(a * 1000)
    b_int = int(b * 1000)

    return a_int == b_int

a = float(input("Enter a float value:"))
b = float(input("Enter b float value:"))
print(compare_floats(a, b))
