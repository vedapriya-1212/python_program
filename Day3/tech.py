#remove duplicates from each day lists(clean)
def remove_duplicates(day1,day2,day3):
    d1=[]
    d2=[]
    d3=[]
    for i in day1:
        if i not in d1:
            d1.append(i)
    for i in day2:
        if i not in d2:
            d2.append(i)
    for i in day3:
        if i not in d3:
            d3.append(i)
    print("after removing duplicates from day1:",d1)
    print("after removing duplicates from day2:",d2)
    print("after removing duplicates from day3:",d3)
#all unique emails from three days
def unique(day1,day2,day3):
    u=[]
    for i in day1:
        if i not in u:
            u.append(i)
    for i in day2:
        if i not in u:
            u.append(i)
    for i in day3:
        if i not in u:
            u.append(i)
    print("All unique emails from three days:",u)
#print emails present in all three days
def common(day1,day2,day3):
    c=[]
    for i in day1:
        if i in day2 and i in day3:
            c.append(i)
    print("attendees in all three days:",c)
#print emails that are in exactly one day
def one(day1,day2,day3):
    o=[]
    for i in day1:
        if i not in day2 and i not in day3:
            o.append(i)
    for i in day2:
        if i not in day1 and i not in day3:
            o.append(i)
    for i in day3:
        if i not in day2 and i not in day1:
            o.append(i) 
    print("attendees in exactly one day:",o)   
#pair wise overlap counts day1&day2, day2&day3, day3&day1
def pair(day1,day2,day3):
    d12=[]
    d23=[]
    d31=[]
    for i in day1:
        if i in day2:
            d12.append(i)
    for i in day2:
        if i in day3:
            d23.append(i)
    for i in day3:
        if i in day1:
            d31.append(i)
    print("day1&day2:",d12)
    print("day2&day3:",d23)
    print("day3&day1:",d31)
day1=['ab@gmail.com','bc@gmail.com','dd@gmail.com']
day2=['b@gmail.com','dd@gmail.com','l@gmail.com']
day3=['ab@gmail.com','v@gmail.com','bc@gmail.com','ab@gmail.com']
remove_duplicates(day1,day2,day3)
unique(day1,day2,day3)
common(day1,day2,day3)
one(day1,day2,day3)
pair(day1,day2,day3)