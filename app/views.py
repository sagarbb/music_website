from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def home(request):
    musics = Music.objects.all()
    d={'musics':musics}
    if request.session.get('username'):
        
        username=request.session.get('username')
        uo = User.objects.get(username = username)
        d={'username':uo,'musics':musics}
        return render(request,'home.html',d)
    return render(request,'home.html', d)
    

def register_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request,'Account is Created')
            return redirect('login_user')
        else:
            context = {'form':form}
            messages.info(request, 'Invalid Credentials')
            return render(request, 'register_page.html', context)

    context = {'form':form}
    return render(request, 'register_page.html', context)

def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user and user.is_active:
            login(request, user)
            request.session['username']=username
            messages.info(request, f'{username}, you are logged in.')
            return HttpResponseRedirect(reverse('home'))
            
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login_user')

    return render(request, 'login_page.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def folder(request):
    if request.session.get('username'):
        
        username=request.session.get('username')
        uo = User.objects.get(username = username)
        folders = Folder.objects.all()
        d={'username':uo,'folders':folders}
        return render(request,'folder.html',d)
    return redirect('login_user')