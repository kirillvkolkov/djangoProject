from django.db import models

# Create your models here.
class Post(models.Model):
    unique_id = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=30)
    body = models.CharField(max_length=300)
    date = models.CharField(max_length=30)

class User(models.Model):
    unique_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()

class Passwords(models.Model):
    unique_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()


#u = User(unique_id='ewr23472323', name='Vasya', surname='Petrov', age=33)
#u.save()

#p = Post(unique_id='777545126hdf', title='432423435', subtitle='3455345fg', body='777fs345443fsd', date='26-Aug-2021 11:11')
#p.save()

