from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, JsonResponse
from user.models import Area

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


# ----------------  Ajax异步实现下拉框多级联动  -----------------------

def ajaxIndex(request):
    return render(request, 'user/ajaxIndex.html')


def getArea1(request):
    list = Area.objects.filter(aPArea__isnull=True)
    list2 = []
    for a in list:
        list2.append([a.aid, a.title])
    return JsonResponse({'data' : list2})


def getArea2(request, pid):
    list = Area.objects.filter(aPArea_id=pid)
    list2 = []
    for a in list:
        list2.append({'id':a.aid, 'title':a.title})
    return JsonResponse({'data': list2})



#----------------- 缓存 F12-->network-->header ----------------
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)   # Cache-Control: max-age=300
def cacheIndex(request):
    return HttpResponse('hello1')