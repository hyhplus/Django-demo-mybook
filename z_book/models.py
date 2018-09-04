from django.db import models

# Create your models here.
class BookInfo(models.Model):
    b_title = models.CharField(max_length=20)
    b_pubdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%d" % self.pk


class HeroInfo(models.Model):
    h_name = models.CharField(max_length=20)
    h_gender = models.BooleanField()
    h_content = models.CharField(max_length=100)
    h_book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def gender(self):
        if self.h_gender:
            return '男'
        else:
            return '女'
    gender.short_description = '性别'

    def __str__(self):
        return "%d" % self.pk
