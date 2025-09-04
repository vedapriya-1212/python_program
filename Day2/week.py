# Function to return the day of the week based on the number input
def week(n):
    if n==1:
        return "Monday"
    elif n==2:
        return "Tuesday"
    elif n==3:
        return "Wednesday"
    elif n==4:
        return "Thursday"
    elif n==5:
        return "Friday"
    elif n==6:
        return "Saturday"
    elif n==7:
        return "Sunday"
    else:
        return "Invalid day number"
print(week(3))  # Output: Wednesday
print(week(7))  # Output: Sunday
print(week(0))  # Output: Invalid day number