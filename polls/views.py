from django.shortcuts import render, HttpResponse
from django.http import Http404

from .models import Question


def home(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'questions': latest_question_list}
    return render(request, 'home.html', context)


def detail(request, question_id):
    q = Question.objects.get(id=question_id)
    return HttpResponse(f"You're looking at question: {q.question_text}")


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
