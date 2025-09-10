#1.print who got highest marks and 2.print who got above 75 marks from a list of tuples
def highest(record):
    max=record[0][2]
    for i in record:
        if i[2]>max:
            max=i[2]
            name=i[1]
    return name,max
def above(record):
    print("Students scored above 75 marks are:")
    for i in record:
        if i[2]>75:
            m=i[2]
            n=i[1]
            r=i[0]
            print(f"{r},{n},{m}")
record=[(1,'teju',76),(2,'deepthi',59),(3,'ved',96),(4,'jah',80),(5,'priya',33)]
n,marks=highest(record)
print(f"Highest Marks {marks} scored by {n}")
above(record)