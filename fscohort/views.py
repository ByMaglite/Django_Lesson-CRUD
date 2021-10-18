from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.

def home(request):
    return render(request, "fscohort/home.html")


def student_list(request):
    
    students = Student.objects.all()
    
    context = {
        "students":students
    }
    
    return render(request, "fscohort/student_list.html", context)

def student_add(request):
    pass

def student_detail(request):
    pass

def student_update(request):
    pass

def student_delete(request):
    pass



