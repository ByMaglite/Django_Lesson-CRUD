from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    email = models.EmailField(max_length=154)
    phone = models.CharField(max_length=50)
    
    GENDER =(
        ("1", "Female"),
        ("2", "Male"),
        ("3", "Other"),
        ("4", "Prefer Not Say"),   
    )
    
    gender = models.CharField(max_length=50, choices=GENDER)
    number = models.CharField(max_length=50)
    image = models.ImageField(upload_to="student/", default="avatar.png")
    
    def __str__(self):
        return self.number + " " + self.first_name