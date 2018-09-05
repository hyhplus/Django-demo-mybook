from django.db import models

# Create your models here.
class BookInfoManger(models.Manager):
    def get_queryset(self):
        return super(BookInfoManger, self).get_queryset().filter(isDelete=False)


class BookInfo(models.Model):
    b_title = models.CharField(max_length=20)
    b_pubdate = models.DateTimeField()
    bread = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    books = BookInfoManger()

    @classmethod
    def create(cls, title, pubdate):
        book = cls(b_title=title, b_pubdate=pubdate)
        book.bread = 0
        book.comment = 0
        book.isDelete = False
        return book

    def __str__(self):
        return "%d" % self.pk


class HeroInfo(models.Model):
    h_name = models.CharField(max_length=20)
    h_gender = models.BooleanField(default=True)
    h_content = models.CharField(max_length=100)
    h_book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)

    def gender(self):
        if self.h_gender:
            return '男'
        else:
            return '女'
    gender.short_description = '性别'

    def __str__(self):
        return "%d" % self.pk


class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title