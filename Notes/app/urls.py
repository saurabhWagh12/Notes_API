from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',registerUser,name='registerUser'),
    path('login/',loginFunction,name='loggingIn'),
    path('logout/',loggingOUT,name='logoutUser'),
    path('notes/',getNotesOfUser,name='getNotes'),
    path('addNote/',addNote,name='addingNote'),
    path('updateNote/',updateNote,name='updateNote'),
    path('deleteNote/',deleteNote,name='deleteNote'),
]