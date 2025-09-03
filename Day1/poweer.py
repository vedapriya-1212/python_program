cno=int(input("enetr cno:"))
cname=str(input("enter name:"))
pmr,lmr=map(int,input("enter readings:").split())
tu=pmr-lmr
cbill=tu*3.80
print("total units:",tu)
print("current bill:",cbill)
print("cno\t\tcname\t\tcbill",end='\n')
print(cno,"\t\t",cname,"\t",cbill,end='\n')