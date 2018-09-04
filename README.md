# mybook
django demo

数据库mysql

1.简单使用{% for book in booklist %}遍历数据

2.关联表遍历{% for hero in book.heroinfo_set.all %}

3.布尔值设置

4.关联表在admin关联注册

5.url跳转<a href="{% url "detail" book.id %}"><br>
即跳转到views.detail的页面