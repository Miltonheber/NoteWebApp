from django.urls import path
from .views import *


urlpatterns = [
    path('create/', create, name='create'),
    path('list/', list_notes, name='list_notes'),
    path('delete/<int:pk>', delete_note, name="delete_note"),
    path('update/<int:pk>', update_note, name='update_note'),
    
]
