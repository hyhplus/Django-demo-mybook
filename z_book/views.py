from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from .models import BookInfo

# Create your views here.
def test(request):
    return HttpResponse("<h1>test page</h1>")

def detail(request, id):
    book = BookInfo.objects.get(pk=id)
    # template = loader.get_template('z_book/detail.html')
    # context = RequestContext(request, {'book' : book})
    # #return HttpResponse("detail %s" % id)
    # return HttpResponse(template, context)

    return render(request, 'z_book/detail.html', {'book':book})


def index(request):
    booklist = BookInfo.objects.all()
    # template = loader.get_template('z_book/index.html')
    # context = RequestContext(request, {'booklist' : booklist})
    # return HttpResponse(template, context)

    return render(request, 'z_book/index.html', {'booklist':booklist})
