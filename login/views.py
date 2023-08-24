from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from login.models import table_user
def loginpage(request):
    return render(request,'loginpage.html')
def userform(request):
    return render(request,'userfrom.html')
def  userform1(request):
     a=User()
     u=table_user()
     u.first_name=request.POST.get('fname')
     u.email=request.POST.get('email')
     u.username=request.POST.get('username')
     u.phone=request.POST.get('num')
     u.gender=request.POST.get('gender')
     u.address=request.POST.get('adrs')
     u.age=request.POST.get('age')
     a.first_name=request.POST.get('fname')
     a.last_name=request.POST.get('lname')
     a.email=request.POST.get('email')
     a.username=request.POST.get('username')
     p=request.POST.get('pswrd')
     a.set_password(p)
     a.save()
     u.save()
     return redirect('/')

def login1(request):
    a=request.POST.get('pswrd')
    b=request.POST.get('username')
    o=authenticate(username=b,password=a)
    request.session['username']=b

    if o is not None and o.is_superuser==1:
        return redirect('/adminpage/')
    elif o is not None and o.is_superuser==0:
        return redirect('/userpage/')
    else:
        return HttpResponse('invalid_respond')
def adminpage(request):
    return render(request,'admin.html')
def userpage(request):
    s=request.session['username']
    e=table_user.objects.get(username=s)
    f=User.objects.get(username=s)
    return render(request,'user.html',{'x':s,'y':e,'z':f})


    
    

# Create your views here.
