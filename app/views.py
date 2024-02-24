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

def insert_accessrecord(request):
    QLWO=WebPage.objects.all()
    d={'webpage':QLWO}

    if request.method=="POST":
        pk=request.POST['pk']
        n=request.POST['n']
        d=request.POST['d']
        au=request.POST['au']

        WO=WebPage.objects.get(pk=pk)
        AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=au)[0]
        AO.save()

        QLAO=AccessRecord.objects.all()
        d1={'accessrecord':QLAO}
        return render(request,'display_accessrecord.html',d1)
    return render(request,'insert_accessrecord.html',d)



def select_multiple_webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    if request.method=='POST':
        topiclist=request.POST.getlist('tn')#['C','FB','VB']
        #print(tn)
        QLWO=WebPage.objects.none()
        for i in topiclist:
            QLWO=QLWO|WebPage.objects.filter(topic_name=i)
            
        d1={'webpage':QLWO}
        return render(request,'display_webpage.html',d1) 
    return render(request,'select_multiple_webpage.html',d)


def checkbox(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    return render(request,'checkbox.html',d)
    
