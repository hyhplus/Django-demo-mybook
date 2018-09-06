from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
# Create your views here.
def test(request):
    return HttpResponse('<h1>test u</h1>')


def index(request):
    name = request.session.get('uname')
    return render(request, 'user/index.html', {'uname' : name})


def login(request):
    return render(request, 'user/login.html')


def login_handle(request):
    request.session['uname'] = request.POST['uname']
    return redirect('/user/index/')


def logout(request):
    request.session.flush()
    return redirect('/user/index/')