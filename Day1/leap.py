def leap(y):
    if (y%4==0 and y%100!=0) or y%400==0:
        print("Leap year")
    else:
        print("Not leap year")
leap(2040)
leap(1600)
leap(2000)
leap(1000)