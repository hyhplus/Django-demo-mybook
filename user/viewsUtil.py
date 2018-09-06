from django.http import HttpResponse

# 验证码                  http://localhost:8000/goods/getcode/
# 对应的urls: urls_goods  http://localhost:8000/goods/#
# 前端页面: temtest/index.html

def verifycode(request):
    from PIL import Image, ImageFont, ImageDraw
    import random

    # 定义变量,用于画面的背景色,宽和高
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 205)
    width = 100
    height = 32

    img = Image.new('RGB', (width,height), bgcolor)
    draw = ImageDraw.Draw(img)

    # 调用画笔的point()函数绘制噪点
    for i in range(0, 10):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)

    for i in range(0, 5):
        xy = (random.randrange(0, width), random.randrange(0, height),
              random.randrange(0, width), random.randrange(0, height))
        fill = (255, random.randrange(0, 255), random.randrange(0, 255))
        draw.line(xy, fill=fill)

    # 定义验证码的备选值
    str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123546789'
    rand_str = ''

    for i in range(0, 4):
        rand_str += str[random.randrange(0, len(str))]

    # 构造字体对象
    font = ImageFont.truetype('fonts-japanese-gothic.ttf', 23)

    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))

    # 绘制4个字
    draw.text((5, random.randrange(0,15)), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, random.randrange(0,15)), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, random.randrange(0,15)), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, random.randrange(0,15)), rand_str[3], font=font, fill=fontcolor)

    # 释放画笔
    # del draw

    # 存入session, 用于进一步验证
    request.session['verifycode'] = rand_str

    # import cStringIO
    # buf = cStringIO.StringIO()

    from io import BytesIO
    buff = BytesIO()

    img.save(buff, 'png')

    return HttpResponse(buff.getvalue(), 'image/png')



def verifycodeVaild(request):
    vc = request.POST['vc']
    if vc.upper() == request.session['verifycode']:
        return HttpResponse('<h1>'+'ok'+'</h1>')
    else:
        return HttpResponse('<h1>no</h1>')




def getcode(request):
    code = request.session['verifycode']
    return HttpResponse(code)