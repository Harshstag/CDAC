from django.shortcuts import render
from django.http import HttpResponse
import random
import string
import os


def gen1():
    
    #######################################    Selecting words from file     ################################################

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'mnames.txt')  #full path to text.
    data_file = open(file_path , 'r',encoding='utf-8') 
    mname = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'fnames.txt')  #full path to text.
    data_file = open(file_path , 'r',encoding='utf-8') 
    fname = data_file.read().split("\n")


    #------------------------------------------------------------------------------------------------------------#

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'peenewale.txt')  #full path to text.
    data_file = open(file_path , 'r',encoding='utf-8')
    drinkable = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'dekhna.txt')  #full path to text.
    data_file = open(file_path , 'r',encoding='utf-8')
    watchable = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'khaanewale.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    cookable = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'khelnewale.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    playable= data_file.read().split("\n")


    #------------------------------------------------------------------------------------------------------------#


    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'cv.txt')  #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    verbs_c = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'playverbs.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    verbs_p = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'drink_kriya.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    verbs_d = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'dekh_kriya.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    verbs_see = data_file.read().split("\n")


    #------------------------------------------------------------------------------------------------------------#


    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'f_cv.txt')  #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    f_verbs_c = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'f_playverbs.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    f_verbs_p = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'f_drink_kriya.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    f_verbs_d = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'f_dekh_kriya.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    f_verbs_see = data_file.read().split("\n")


    #------------------------------------------------------------------------------------------------------------#





    def mnames():
        return mname[random.randint(0,len(mname)-1)]
    def fnames():
        return fname[random.randint(0,len(fname)-1)]
    
    ###################    Selecting Subject  First   ############################

    ran = random.randint(1,4)
    
    if(ran == 1):
            n1 = mnames()
            n2 = fnames()
    elif(ran == 2):
            n1 = fnames() 
            n2 = mnames()
    elif(ran == 3):
            n1 = fnames() 
            n2 = fnames() 
    elif(ran == 4):
            n1 = mnames()
            n2 = mnames() 


    # if both name are same then loop till its different 
    if(n1 == n2):
        while(n1==n2):
            n2=fnames() 



    
    ###################    Selecting Object     ############################

    def objects():
        rt=random.randint(1,4)
        if(rt==1): 
            term = cookable[random.randint(0,len(cookable)-1)] 
        elif(rt==2):
            term = playable[random.randint(0,len(playable)-1)]
        elif(rt==3):
            term = drinkable[random.randint(0,len(drinkable)-1)]   
        elif(rt==4):
            term = watchable[random.randint(0,len(watchable)-1)]  
            
        return term

###################    Selecting Verbs     ############################
    
    def m_play_verbs():
        return verbs_p[random.randint(0,len(verbs_p)-1)]
    
    def m_cook_verbs():
        return verbs_c[random.randint(0,len(verbs_c)-1)]
    
    def m_drink_verbs():
        return verbs_d[random.randint(0,len(verbs_d)-1)]
    
    def m_watch_verbs():
        return verbs_see[random.randint(0,len(verbs_see)-1)]
    
    #-------------------------------------------------------------------#
    

    def f_play_verbs():
        return f_verbs_p[random.randint(0,len(f_verbs_p)-1)]
    
    def f_cook_verbs():
        return f_verbs_c[random.randint(0,len(f_verbs_c)-1)]
    
    def f_drink_verbs():
        return f_verbs_d[random.randint(0,len(f_verbs_d)-1)]
    
    def f_watch_verbs():
        return f_verbs_see[random.randint(0,len(f_verbs_see)-1)]
    

    

    ###################  sentence first & second  ############################  

    def mk_sen1():

        global obj1
        obj1 = objects() # selecting object

        if n1 in mname:
            # selecting male Verbs
            c_v1 = m_cook_verbs()
            p_v1 = m_play_verbs()
            d_v1 = m_drink_verbs()
            w_v1 = m_watch_verbs()
            
        elif n1 in fname:
            # selecting female Verbs
            c_v1 = f_cook_verbs()
            p_v1 = f_play_verbs()
            d_v1 = f_drink_verbs()
            w_v1 = f_watch_verbs()
        

        if obj1 in cookable:
            sen1 = n1 + " " + obj1 + " " + c_v1
            return sen1
        elif obj1 in playable:
            sen1 = n1 + " " + obj1 + " " + p_v1
            return sen1
        elif obj1 in drinkable:
            sen1 = n1 + " " + obj1 + " " + d_v1
            return sen1
        elif obj1 in watchable:
            sen1 = n1 + " " + obj1 + " " + w_v1
            return sen1

    #---------------------------------------------------------------------#

    def mk_sen2():  
        
        global obj2 
        obj2 = objects() 

        if(obj1 == obj2): 
            while(obj1 == obj2):
                obj2 = objects()

        if n2 in mname:
            # selecting male Verbs
            c_v2 = m_cook_verbs()
            p_v2 = m_play_verbs()
            d_v2 = m_drink_verbs()
            w_v2 = m_watch_verbs()
            
        elif n2 in fname:
            # selecting female Verbs
            c_v2 = f_cook_verbs()
            p_v2 = f_play_verbs()
            d_v2 = f_drink_verbs()
            w_v2 = f_watch_verbs()


        # if object of both sentence are same then infront of subject / name "भी" should be added
        # if(obj1 == obj2):
        #     n22 = n2 + " " + 'भी'
        # else:
        #     n22 = n2
        

        if obj2 in cookable:
            sen2 = n2 + " " + obj2 + " " + c_v2
            return sen2
        elif obj2 in playable:
            sen2 = n2 + " " + obj2 + " " + p_v2
            return sen2 
        elif obj2 in drinkable:
            sen2 = n2 + " " + obj2 + " " + d_v2
            return sen2 
        elif obj2 in watchable:
            sen2 = n2 + " " + obj2 + " " + w_v2
            return sen2 
        

        
    ###################  sentence conjunction  ############################


    
    def conjunction():

        rt = random.randint(1,2)

        if(rt == 1):
            conj =" "+'और'+" "
        else:
            conj =" "+'पर'+" "
        return conj


    ############################################################################



    def make_sentence():

        # Making sentence now  # Subject + Object + Verb

        s1 = mk_sen1() #1st Sentence making
        s2 = mk_sen2() #2nd Sentence making
        conj = conjunction() # selecting conjuction

        f_s = s1 + " " + conj + " " + s2 + " |"

        # ans1 is first independent clause
        ans1 = s1 
        
        #ans2 is second independent clause
        ans2 = s2

        #res2 = sum([i.strip(string.punctuation).isalpha() for i in ans2.split()])
        return [f_s, ans1, ans2, s1, s2, conj]
    

    ############################################################################



    # Sentence Making start's here
    data = make_sentence()


    return (data)


def next(request):
    dataa = request.session.get('dataa')
    dataa = gen1()
    request.session['dataa'] = dataa
    daaa=dataa
    return render(request,'next.html',{'data':daaa[0],'ans1':daaa[1],'ans2':daaa[2],'n':daaa[3],'obj1':daaa[4],'c_v':daaa[5]})


def theory(request):
    return render(request,'theory.html')

def explanation(request):
    dataa = request.session.get('dataa')
    daaa=dataa
    return render(request,'explanation.html',{'data':daaa[0],'ans1':daaa[1],'ans2':daaa[2],'n':daaa[3],'obj1':daaa[4],'c_v':daaa[5]})
    
def ex1(request):
    dataa = request.session.get('dataa')
    daaa=dataa
    return render(request,'ex1.html',{'data':daaa[0],'ans1':daaa[1],'ans2':daaa[2],'n':daaa[3],'obj1':daaa[4],'c_v':daaa[5]})

def main(request):
    return render(request,'main.html')