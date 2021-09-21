from django.shortcuts import render
from . models import Exam

# Create your views here.


def examonline(request):
    results = Exam.objects.all()

    return render(request, 'index.html', {"Exam":results})

def examonline2(request):
    results = Exam.objects.all()

    return render(request, 'quiz.html', {"Exam":results})