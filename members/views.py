from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Members
# Create your views here.
def memberview(request):
    if request.method == GET:
        members=Members.objects.all()
        data=[{
            'id':member.id,
            'name':members.name,
            'usn':members.usn,
            'year':members.year,
            'branch':members.branch
        }
            for member in members
        ]
        return JsonResponse(data,safe=False)  #safe=false so list can be sent

