from django.urls import path
from .views import *

urlpatterns =[
    path('',home),
    path('signup/',signup),
    path('login/',Login),
    path('tasklist',todolist),
    path('todopage',todo),
    path('delete_todo/<int:id>',delete_todo),
    path('edit_todo/<int:id>',edit_todo, name='edit_todo'),
    path('signout/',signout, name='signout'),
]   