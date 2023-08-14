from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import upload_project
from django.contrib import messages

# Create your views here.


def index(request):
    data=upload_project.objects.all()[:6]
    
    return render(request,'index.html',{'box':data})


def all_projetcs(request):
    data=upload_project.objects.all()
    
    return render(request,'all_project.html',{'projects':data})


def up_project(request):  
    if request.method=='POST':
        pname=request.POST.get('pname')
        pdesc=request.POST.get('desc')
        technologies=request.POST.get('technologies')
        url=request.POST.get('url')
        picture=request.FILES.get('profile')

        print(picture)
        form=upload_project(pname=pname,pdesc=pdesc,technologies=technologies,url=url,profile_picture=picture)
        form.save()
        messages.success(request, "project uplaod successfully") 
        


    return render(request,'upload_project.html')




def search(request):
    query=request.GET['query'];
    data=upload_project.objects.filter(pname__icontains=query)
    return render(request,'search.html',{'searchdata':data})




def login_form(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        
        if User is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse('username and password incorrect')
    return render(request,'login.html')  