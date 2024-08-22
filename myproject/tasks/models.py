from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(default="Field for information about lesson")
    def __str__(self):
        return f"Subject name: {self.name}"


class Teacher(models.Model):
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
    speciality = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return f"Name: {self.name}\nLast_name: {self.surname}\nSpeciality: {self.speciality}"

class School_Class(models.Model):
    STATUS_CHOICES = (
        ('first','1th'),
        ('second', '2th'),
        ('third','3th'),
        ('fourth','4th'),
        ('fifth', '5th'),
        ('sixth','6th'),
        ('seventh','7th'),
        ('eighth', '8th'),
        ('ninth','9th'),
        ('tenth','10th'),
        ('eleventh', '11th')
        
    )
    letter = models.CharField(max_length=1)
    grade = models.CharField(max_length=4)
    def __str__(self):
        return f"{self.grade} Grade {self.letter}"
    

class Student(models.Model):
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
    grade = models.ForeignKey(School_Class, on_delete=models.CASCADE)
    def __str__(self):
        return f"Name: {self.name}\nLast_name: {self.surname}\nClass{self.grade.str()}"
