from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from newapp.forms import QuestionForm
# from 경로 잘 보셈, 위 아래 같은 경로
from ..models import Question
# 모듈 임포트 optimizing = ctrl + alt + o


@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.q_date = timezone.now()
            question.save()
            return redirect('index')
    else:
        form = QuestionForm()
    return render(request, 'newapp/question_form.html', {'form': form})


@login_required(login_url='common:login')
def question_modify(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    if request.user != question.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('newapp:detail', question_id=question.id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('newapp:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'newapp/question_form.html', {'form': form})


@login_required(login_url='common:login')
def question_delete(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    if request.user != question.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('newapp:detail', question_id=question.id)

    question.delete()
    return redirect('newapp:index')