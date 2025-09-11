class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def display(self):
        print(f"Name: {self.name}\nRollno: {self.rollno}\nMarks: {self.marks}\n")
s1=student("Deepthi",72,98)
s1.display()
s2=student("Veda",101,95)
s2.display()