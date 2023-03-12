from django.shortcuts import render
from django.http import HttpResponse
import random
import string
import os


def gen2():

    #get nouns
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'names1.txt')   #full path to text.
    data_file = open(file_path , 'r')
    names1 = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'names2.txt')   #full path to text.
    data_file = open(file_path , 'r')
    names2 = data_file.read().split("\n")

    #get verb1
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'verb1.txt')   #full path to text.
    data_file = open(file_path , 'r')
    verbs = data_file.read().split("\n")
    
    #get verb2
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'verb2.txt')   #full path to text.
    data_file = open(file_path , 'r')
    verbs2 = data_file.read().split("\n")
    
    #get food1
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'food1.txt')   #full path to text.
    data_file = open(file_path , 'r')
    foods = data_file.read().split("\n")
    
    #get hungry
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'hungry.txt')   #full path to text.
    data_file = open(file_path , 'r')
    hung = data_file.read().split("\n")

    #get places
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'places1.txt')  
    data_file = open(file_path , 'r')
    places = data_file.read().split("\n")

    #get class
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'class.txt')  
    data_file = open(file_path , 'r')
    classes = data_file.read().split("\n")

    #get verb3
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'verb3.txt')  
    data_file = open(file_path , 'r')
    verbs3 = data_file.read().split("\n")

    #get books
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'books.txt')  
    data_file = open(file_path , 'r')
    book = data_file.read().split("\n")


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
        b1=book1()
        b2=book1()

        while(b1==b2):
            b2=book1()
        

        #random names gn:girls names, bn:boys names
        #Separate files are made to determine pronouns (she/he) accordingly
        if(r1==1):
            n1=gn
            n2=bn
        else:
            n1=bn
            n2=gn 
    
        #random conj1: because, since, as
        r3=random.randint(1,4) 
        if(r3==1):
            conj1='because'    
        elif(r3==2):
            conj1='since'
        else:
            conj1='as'
    
        #random conj2: after, later
        r4=random.randint(1,3)
        if(r4==1):
            conj2='after'
        else:
            conj2='later'

         #independent clauses
        cl1=n1+" "+eating(v1)
        cl11=n1+" "+going(v2)
        cl12=n1+" "+v3+" "+b1

        # uses as independent and dependent clauses both
        cl23=n2+" "+v3+" "+b2
        
        #dependent clauses
        #adding pronouns 
        if(n1==gn):
            cl2="she was"+" "+h
            cl22="she finished"+" "+c
        else:
            cl2="he was"+" "+h
            cl22="he finished"+" "+c

        #variables values:- 
        #s: sentence, ans: conjunction+correct part of sentence(dependent clause)
        #nta: not a clause(independent clause)
        #r: part of dependent clause without conjuction
        #con= conjunction

        #make sentence
        rc=random.randint(1,10)
        if(rc==1 or rc==2 or rc==7):
            s=cl1+", "+conj1+" "+cl2
            ans=conj1+" "+cl2
            nta=cl1
            r=cl2
            con=conj1
        elif(rc==3 or rc==5 or rc==8):
            s=cl11+", "+conj2+" "+cl22
            ans=conj2+" "+cl22
            nta=cl11
            r=cl22
            con=conj2

        #Conjunction: although
        elif(rc==4 or rc==6):
            s="Although "+cl12+", "+cl23 #cl23 act as independent clause
            ans="Although "+cl12
            nta=cl23
            r=cl12
            con="Although"
        else:
            s=cl12+", although "+cl23  #cl23 act as dependent clause
            ans="although "+cl23
            nta=cl12
            r=cl23
            con="although"


        return [s,ans,con,nta,r]

    sen2=sen()

    return (sen2)

def theory2(request):
    return render(request,'theory2.html')

def next2(request):
    dataa2 = request.session.get('dataa2')
    dataa2 = gen2()
    request.session['dataa2'] = dataa2
    daaa2=dataa2
    return render(request,'next2.html',{'data':daaa2[0],'ans':daaa2[1],'con':daaa2[2],'nta':daaa2[3],'r':daaa2[4]})
    

def explanation2(request):
    dataa2 = request.session.get('dataa2')
    daaa2=dataa2
    return render(request,'explanation2.html',{'data':daaa2[0],'ans':daaa2[1],'con':daaa2[2],'nta':daaa2[3],'r':daaa2[4]})
    
def ex2(request):
    dataa2 = request.session.get('dataa2')
    daaa2=dataa2
    return render(request,'ex2.html',{'data':daaa2[0],'ans':daaa2[1],'con':daaa2[2],'nta':daaa2[3],'r':daaa2[4]})







    






    



    

    










    