import random

# get nouns
with open("names1.txt","r") as name1:
    names1 = name1.read().split("\n")

with open("names2.txt","r") as name2:
    names2 = name2.read().split("\n")
#get verbs
with open("verb1.txt", "r") as verb1:
    verbs = verb1.read().split("\n")

with open("verb2.txt", "r") as verb2:
    verbs2 = verb2.read().split("\n")

with open("food1.txt", "r") as food1:
    foods = food1.read().split("\n")

with open("hungry.txt", "r") as hungry1:
    hung = hungry1.read().split("\n")

with open("places1.txt", "r") as place1:
    places = place1.read().split("\n")

with open("class.txt", "r") as class1:
    classes = class1.read().split("\n")

with open("verb3.txt", "r") as verb3:
    verbs3 = verb3.read().split("\n")

with open("books.txt", "r") as books:
    book = books.read().split("\n")


def fo():
    return foods[random.randint(0,len(foods)-1)]
def gname():
    return names1[random.randint(0,len(names1)-1)]
def bname():
    return names2[random.randint(0,len(names2)-1)]
def verb():
    return verbs[random.randint(0,len(verbs)-1)]
def hungry():
    return hung[random.randint(0,len(hung)-1)]
def verb22():
    return verbs2[random.randint(0,len(verbs2)-1)]
def place():
    return places[random.randint(0,len(places)-1)]
def classs():
    return classes[random.randint(0,len(classes)-1)]
def verb33():
    return verbs3[random.randint(0,len(verbs3)-1)]
def book1():
    return book[random.randint(0,len(book)-1)]


def eating(verb):
    ve=verb+" "+fo()
    return ve
def going(verb22):
    ve2=verb22+" "+place()
    return ve2
def reading(verb33):
    ve3=verb33+" "+book1()
    return ve3

def sen():
    
    r1=random.randint(1,3)
    r2=random.randint(1,3)
    v1=verb()
    v2=verb22()
    v3=verb33()
    gn=gname()
    bn=bname()
    c=classs()
    h=hungry()
    b=book1()

    #random names
    if(r1==1):
        n1=gn
        n2=bn
    else:
        n1=bn
        n2=gn 
    
    #random conj
    r3=random.randint(1,4) 
    if(r3==1):
        conj1='because'    
    elif(r3==2):
        conj1='since'
    else:
        conj1='as'
    
    r4=random.randint(1,3)
    if(r4==1):
        conj2='after'
    else:
        conj2='later'

    #independent clauses
    cl1=n1+" "+eating(v1)
    cl11=n1+" "+going(v2)
    cl12=n1+" "+reading(v3)

    # uses as independent and dependent clauses
    cl23=n2+" "+reading(v3)

    #dependent clauses
    #adding pronouns 
    if(n1==gn):
        cl2="she was"+" "+h
        cl22="she finished"+" "+c
    else:
        cl2="he was"+" "+h
        cl22="he finished"+" "+c
    

    #make sentence
    rc=random.randint(1,10)
    if(rc==1 or rc==2 or rc==7):
        s=cl1+", "+conj1+" "+cl2
    elif(rc==3 or rc==5 or rc==8):
        s=cl11+", "+conj2+" "+cl22

    elif(rc==4 or rc==6):
        s="Although "+cl12+", "+cl23   #cl23 act as independent clause
    else:
        s=cl12+", although "+cl23   #cl23 act as dependent clause

    return s+"."

print(sen())

