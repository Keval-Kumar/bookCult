from django.urls import path
from . import views
urlpatterns=[
    path('firstpage/',views.index,name='firstpage'),
]