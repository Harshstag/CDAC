# CDAC
version 1 hrs
Django framework has been used to integrate html+css+javascript(FRONTEND) with python(BACKEND).
Details of Django setup and files related to "Clause Simulator" is provided in this document.
---------------------------------------------------------------------------------------------------
The following commands are used to setup and start the server.
Steps:
1) Install python 

We create virtual environment wrapper
2) pip install vritualenvwrapper-win

3) mkvirtualenv test1

Install django in this setup
4) pip install django

Open the folder and start the project named "olab"
5) mkdir olabfront
6) cd olabfront
7) django -admin startproject olab
````````
8) cd olab

Run the server
9) python manage.py runserver
   python manage.py startapp eng
````````
------------------------------------------------------------------------------------------------------

There are two exercises in this clause simulator.
1) Identification of Independent Clause
   
   BACKEND FILE: olab\eng\views.py
   DATA FILES FOR BACKEND: drinkable
                           names
                           verbs
                           places
                           playable
                           playable_plu
                           days
                           group
                           playable2
                           eatable
                           cookable
                           watchable
   FRONTEND FILES: olab\templates\ex1.html
                   olab\templates\next.html
                   olab\templates\explanation.html
                   olab\templates\theory.html
  
Sentence Format: independent clause+ conjunction + independent clause
Conjunction: but,and

2) Identification of Dependent Clause
   
   BACKEND FILE: olab\eng\views1.py
   DATA FILES FOR BACKEND:names1
                          names2
                          verb1
                          verb2
                          food1
                          hungry
                          places1
                          class
                          verb3
                          books
   FRONTEND FILES: olab\templates\ex2.html
                   olab\templates\next2.html
                   olab\templates\explanation2.html
                   olab\templates\theory2.html


Sentence Format: independent clause+ conjunction +,+ dependent clause
                 conjunction+ dependent clause+,+ independent clause

Conjunction: because,since,as,after,later,although
