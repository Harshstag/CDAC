from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views #. is current directory
from . import views2

urlpatterns = [
    #path('',views.home,name='home')
    
    path('',views.main,name='main'),
    path('ex1',views.ex1,name='ex1'),
    path('theory',views.theory,name='theory'),
    path('explanation',views.explanation,name='explanation'),
    path('next',views.next,name='next'),

    path('ex2',views2.ex2,name='ex2'),
    path('explanation2',views2.explanation2,name='explanation2'),
    path('next2',views2.next2,name='next2'),
    path('theory2',views2.theory2,name='theory2'),

    # path('op',views.output,name="script")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)