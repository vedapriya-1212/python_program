n=int(input("enter total students:"))
for i in range(n):
    total=0
    sno=int(input("Enter number:"))
    sname=str(input("enter name:"))
    print("Enter student",sname,"details")
    marks1=int(input("Enter maths marks:"))
    total=total+marks1
    marks2=int(input("Enter science marks:"))
    total=total+marks2
    marks3=int(input("Enter social marks:"))
    total=total+marks3
    print("Total marks of",sname,":",total)
    avg=total/3
    print("average marks:",round(avg,2))
'''
print("sno/t/tsname/t/tmaths/t/tscience/t/tsocial/t/total/t/taverage")
for i in range(n):
    print(sno,"/t/t",sname,"/t/t",marks1,"/t/t",marks2,"/t/t",marks3,"/t/t",total,"/t/t",avg)
'''