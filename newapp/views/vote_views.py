from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from newapp.models import Question, Answer

# 21/04/27 김인웅 - 추천 view 추가
@login_required(login_url='common:login')
def vote_question(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    if request.user == question.author:
        messages.error(request, '본인 글은 추천할 수 없습니다.')
    else:
        question.voter.add(request.user)
    return redirect('newapp:detail', question_id=question.id)


@login_required(login_url='common:login')
def vote_answer(request, answer_id):

    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user == answer.author:
        messages.error(request, '본인 답변은 추천할 수 없습니다.')
    else:
        answer.voter.add(request.user)
    return redirect('newapp:detail', question_id=answer.a_subject.id)