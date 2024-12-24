from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    fathername = models.CharField(max_length=25)
    mothername = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    jee_marks = models.IntegerField()
    country = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)

class Student(models.Model):
    name = models.CharField(max_length=50, null=False)
    fathername = models.CharField(max_length=25, null=False)
    mothername = models.CharField(max_length=25, null=False)
    email = models.EmailField()
    number = models.CharField(max_length=10, null=False)
    jee_marks = models.IntegerField()
    country = models.CharField(max_length=25, null=False)
    city = models.CharField(max_length=25, null=False)
    state = models.CharField(max_length=25, null=False)
    class Meta:
        db_table = "admission_student"

    def __str__(self):
        return self.name

class user(models.Model):
    name = models.CharField(max_length=50, null=False)
    fathername = models.CharField(max_length=25, null=False)
    mothername = models.CharField(max_length=25, null=False)
    email = models.EmailField()
    number = models.CharField(max_length=10, null=False)
    jee_marks = models.IntegerField()
    country = models.CharField(max_length=25, null=False)
    city = models.CharField(max_length=25, null=False)
    state = models.CharField(max_length=25, null=False)
    class Meta:
        db_table = "user"

    def __str__(self):
        return self.name


'''class location(models.Model):''
    state = models.CharField(max_length=10)
    city'''


    
