from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def htmlforms(request):
    if request.method=="POST":

        return HttpResponse('Data inserted')
    return render(request,'htmlforms.html')


def insert_topic(request):
    if request.method=="POST":
        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()

        QLTO=Topic.objects.all()
        d={'topic':QLTO}
                                       
        return render(request,'display_topic.html',d)
    return render(request,'insert_topic.html')

def insert_webpage(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}

    if request.method=="POST":
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']

        TO=Topic.objects.get(topic_name=tn)
        WO=WebPage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
        WO.save()

        QLWO=WebPage.objects.all()
        d1={'webpage':QLWO}
        return render(request,'display_webpage.html',d1)
    return render(request,'insert_webpage.html',d)
