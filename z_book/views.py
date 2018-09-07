from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import RequestContext, loader
from django.urls import reverse
import random
from .models import BookInfo, AreaInfo
from django.core.paginator import Paginator

# Create your views here.
def test(request):
    return HttpResponse("<h1>test page</h1>")


''' 一个详情页 '''
def detail(request, id):
    # book = BookInfo.books.get(pk=id)
            # template = loader.get_template('z_book/detail.html')
            # context = RequestContext(request, {'book' : book})
            # #return HttpResponse("detail %s" % id)
            # return HttpResponse(template, context)
    try:
        book = get_object_or_404(BookInfo, pk=id)
    except BookInfo.MultipleObjectsReturned:
        book = None

    return render(request, 'z_book/detail.html', {'book':book})


''' 主页: 列表页 '''
def index(request):
    #booklist = BookInfo.books.all()
    booklist = get_list_or_404(BookInfo, pk__lt=3)
    return render(request, 'z_book/index.html', {'booklist':booklist})


''' 分页测试 '''
def pagTest(request, pIndex):
    list = BookInfo.books.all()
    p = Paginator(list, 5)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)

    list2 = p.page(pIndex)
    plist = p.page_range
    return render(request, 'z_book/pageTest.html', {'list':list2,'plist':plist,'pIndex':pIndex})


''' 地址 '''
def area(request,id):
    area = AreaInfo.objects.get(pk=id)
    context = {'area' : area}
    return render(request, 'z_book/area.html', context)


''' GET请求方式test '''
def getTest1(request):
    return render(request, 'z_book/getTest1.html')

def getTest2(request):
    a = request.GET['a']
    b = request.GET['b']
    context = {'a':a, 'b':b}
    return render(request, 'z_book/getTest2.html', context)

def getTest3(request):
    a = request.GET.getlist('a')
    b = request.GET['b']
    context = {'a':a, 'b':b}
    return render(request, 'z_book/getTest3.html', context)


''' POST test '''
def postTest1(request):
    return render(request, 'z_book/postTest1.html')


def postTest2(request):
    name = request.POST['uname']
    upwd = request.POST['upwd']
    gender = request.POST['ugender']

    hobby = request.POST.getlist('uhobby')
    context = {'uname':name, 'upwd':upwd, 'ugender':gender, 'uhobby':hobby}
    return render(request,'z_book/postTest2.html', context)


# def cookie(request):
#     response = HttpResponse()
#     if request.COOKIES.has_key('h1'):
#         response.write('<h1>'+request.COOKIES['h1']+'</n1>')
#     response.set_cookie('h1', '你好', 120)
#     return response


def indexhttp(request):
    #request.session['user']= 'session'
    context = {'h1' : 'hello'}
    content = loader.render_to_string('polls/index.html', context, request)
    hp = HttpResponse(content)
    hp.set_cookie('user', 'cookie')

    hp.write('<h1>'+'write'+'</h1>')

    # hp.delete_cookie('user')   #删除cookie
    return hp

def jsonIndex(request):
    return JsonResponse({'list' : 'abc','set':'bbc'})

def reverse1(request):
    # return HttpResponseRedirect('12/')
    a=random.random() * 100
    a = int(a)

    return HttpResponseRedirect(reverse('reverse2', args=(a,)))

def reverse2(request, id):
    return HttpResponse(id)