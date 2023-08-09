from django.urls import path
from .views import *

urlpatterns = [
   path('login/', login, name='login'),
   path('registar/', cadastro, name='cadastrar'),
   path('logout/', logout, name='logout') 
]
