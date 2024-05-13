from django.shortcuts import render
from .models import Category
from subjects.models import Subject
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='accounts:login')
def exam(request):
    grades=Category.objects.all()      
    context={'grades':grades,}
    return render(request,'exam/Exam.html',context)

def grade_exams(request,category_slug):
    grade=Category.objects.get(slug=category_slug) 
    subjects=Subject.objects.filter(category=grade)     
    context={'subjects':subjects,}
    return render(request,'subjects/subjects.html',context)

def exam_detail(request,category_slug,subject_slug):
    grade=Category.objects.get(slug=category_slug)
    subject=Subject.objects.get(category=grade,slugy=subject_slug) 
    context={'subject':subject,}
    return render(request,'subjects/exam_setion.html',context)