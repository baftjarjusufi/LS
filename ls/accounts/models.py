from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    phone =models.CharField(max_length=100, null=True)
    email =models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    phone =models.CharField(max_length=100, null=True)
    email =models.CharField(max_length=100, null=True)
    department =models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    
    STATUS = (
            ('Active', 'Active'),
            ('Not Active','Not Active'),
            ('Finished','Finished'),
            ('Not Finished','Not Finished'),
    )


    name = models.CharField(max_length=100, null=True)
    code = models.FloatField(null=True)
    students =models.ForeignKey(Student, null=True, on_delete= models.SET_NULL)
    teachers = models.ForeignKey(Teacher, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return self.name


class Academicyear(models.Model):
    
    STATUS = (
            ('Active', 'Active'),
            ('Not Active','Not Active'),
            ('Finished','Finished'),
            ('Not Finished','Not Finished'),
    )


    year = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return self.year
    

    