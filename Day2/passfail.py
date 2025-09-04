def student(m):
    if m>=40:
        if m<50:
            return "C"
        elif m<70:
            return "B"
        elif m<80:
            return "A"
        else:
            return "S"
    else:
        return "Fail"
sno=[101,102,103,104]
sname=['Alice','Bob','Charlie','David']
marks=[95,67,45,25]
for i in range(len(sno)):
    print(f"Student Number: {sno[i]}, Name: {sname[i]}, Marks: {marks[i]}, Grade: {student(marks[i])}") 