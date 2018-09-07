from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=64)

    class Meta:
        db_table = 'user'


class Area(models.Model):
    aid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    aPArea = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title