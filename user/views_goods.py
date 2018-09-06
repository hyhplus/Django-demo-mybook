from django.shortcuts import render


logo = 'welcome to itcast'

def index(request):
    return render(request, 'temtest/index.html', {'logo': logo})


def goods_list(request):
    return render(request, 'temtest/goodslist.html',{'logo': logo})


def user_pwd(request):
    return render(request, 'temtest/userpwd.html', {'logo': logo})