from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from .models import BookInfo, AreaInfo

# Create your views here.
def test(request):
    return HttpResponse("<h1>test page</h1>")


''' 一个详情页 '''
def detail(request, id):
    book = BookInfo.books.get(pk=id)
    # template = loader.get_template('z_book/detail.html')
    # context = RequestContext(request, {'book' : book})
    # #return HttpResponse("detail %s" % id)
    # return HttpResponse(template, context)

    return render(request, 'z_book/detail.html', {'book':book})


''' 主页: 列表页 '''
def index(request):
    booklist = BookInfo.books.all()
    # template = loader.get_template('z_book/index.html')
    # context = RequestContext(request, {'booklist' : booklist})
    # return HttpResponse(template, context)

    return render(request, 'z_book/index.html', {'booklist':booklist})


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
    # name = request.POST.get('uname')
    # upwd = request.POST.get('upwd')
    # gender = request.POST.get('ugender')

    hobby = request.POST.getlist('uhobby')
    context = {'uname':name, 'upwd':upwd, 'ugender':gender, 'uhobby':hobby}
    return render(request,'z_book/postTest2.html', context)


def cookie(request):
    response = HttpResponse()
    if request.COOKIES.has_key('h1'):
        response.write('<h1>'+request.COOKIES['h1']+'</n1>')
    response.set_cookie('h1', '你好', 120)
    return response
