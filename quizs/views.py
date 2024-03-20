from django.shortcuts import render
from .models import Quiz
import random

def index(request):
    quizs = Quiz.objects.all()
    random_index = random.randint(0, len(quizs) - 1)
    quiz = quizs[random_index]
    context = {
        "quiz": quiz,
    }
    return render(request, "quizs/index.html", context)
