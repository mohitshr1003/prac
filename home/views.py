from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from .models import *

# Create your views here.
def index(request):

    if(request.method=='POST'):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('umail')
        pswd = request.POST.get('upswd')
        
        user = User.objects.create_user(fname, email, pswd)
        user.save()
    return render(request, "index.html")

def user_login(request):
    
    if(request.method == 'POST'):
        user_id = request.POST.get('chk_mail')
        user_pswd = request.POST.get('chk_pswd')

        user = authenticate(request, username=user_id, password=user_pswd)
        if user != None:
            login(request, user)
            return HttpResponse("Hello")
        else:
            return HttpResponse("Bye")
    
    return render(request, "login.html")