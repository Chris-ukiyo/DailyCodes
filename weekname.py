Weekday Name from  user given number

Ans:

def get_week(n):
    match n:
        case 1: return "Sunday"
        case 2: return "Monday"
        case 3: return "Tuesday"
        case 4: return "Wednesday"
        case 5: return "Thursday"
        case 6: return "Friday"
        case 7: return "Satur5day"
        case _: return "Invalid num"

n=int(input("Enter an Integer:"))
print("Weekday name:",get_week(n))
