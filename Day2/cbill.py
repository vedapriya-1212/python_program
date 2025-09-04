#current bill distinct for every range of units
def bill(units):
    if units<=50:
        return round(units*3.80,2)
    elif units<=100:
        return round((50*3.80)+(units-50)*4.20,2)
    elif units<=200:
        return round((50*3.80)+(50*4.20)+((units-100)*5.10),2)
    elif units<=300:
        return round((50*3.80)+(50*4.20)+(100*5.10)+((units-200)*6.30),2)
    else:
        return round((50*3.80)+(50*4.20)+(100*5.10)+(100*6.30)+((units-300)*7.50),2)
cno=[1,2,3]
cname=["amy","sam","ved"]
pmr=[23,179,423]
lmr=[0,23,79]
for i in range(len(cno)):
    tu=pmr[i]-lmr[i]
    print(f"cno:{cno[i]}, cname:{cname[i]}, pmr:{pmr[i]}, lmr:{lmr[i]}, bill:{bill(tu)}")