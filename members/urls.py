from django.urls import path
from . import views
urlpatterns=[
    path('members/',views.memberview,name='listOfMembers'),

]