from random import shuffle, sample

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from app.models import Answer, Question, Result, QuizModel
from .filters import ResultFilter

def index(request):
    return render(request, 'index.html')


def contents(request):
    return render(request, 'html/contents.html')


def video(request):
    return render(request, 'html/video.html')


def taqdimot(request):
    return render(request, 'html/taqdimot.html')


def exhibition(request):
    return render(request, 'html/korgazma_file.html')


def textbooks(request):
    return render(request, 'html/textbooks.html')


def handbook(request):
    return render(request, 'html/handbook.html')


def elec_textbook(request):
    return render(request, 'html/elec_textbook.html')

def course_book(request):
    return render(request, 'html/course_book.html')


def qiuz(request):
    quizs = QuizModel.objects.all()
    context = {
        'quizs': quizs
    }
    return render(request, 'quiz.html', context)

@login_required(login_url='login')
def quistion(request, pk):
    quistions = Question.objects.filter(quiz_id=pk)
    quistions = sample(list(quistions), 2)
    answers = Answer.objects.all()
    answers = list(answers)
    shuffle(answers)
    if request.method == "POST":
        correct = 0
        wrong = 0
        for q in quistions:
            if request.POST.get(q.name) == "True":
                correct += 1
            else:
                wrong += 1
            quiz = q.quiz
        Result.objects.create(
            user=User.objects.get(username=request.user.username),
            total_question=len(quistions),
            corrent_question=correct,
            quiz=quiz
        )
        context = {
            'correct': correct,
            'wrong': wrong,
            'total_question': len(quistions),
            'user': request.user.username,
            'total': round(correct * 100 / len(quistions), 2)
        }
        return render(request, 'html/result.html', context)
    context = {
        'quistions': quistions,
        'answers': answers,
    }

    return render(request, 'html/test.html', context)

def result_list(request):
    results = Result.objects.all()
    results_filter = ResultFilter(request.GET, queryset=results)
    context = {
        'results': results_filter
    }
    return render(request, 'html/result.html', context)