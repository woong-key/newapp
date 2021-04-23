# from django.http import HttpResponse
# Create your views here.
# -------------------------------[edit 21/04/11 김인웅]---------------------------------- #
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer, Comment
# --------------------------------[edit 21/04/14 김인웅]--------------------------------- #
from .forms import QuestionForm, AnswerForm, CommentForm
from django.contrib.auth.decorators import login_required
# --------------------------------[edit 21/04/15 김인웅]--------------------------------- #
from django.core.paginator import Paginator
# --------------------------------[edit 21/04/21 김인웅]--------------------------------- #
from django.contrib import messages


# --------------------------------[edit 21/04/12 김인웅]--------------------------------- #
def index(request):

    page = request.GET.get('page', '1')
    # get('page', '1'): 페이지 파라미터가 없는 URL을 위해 기본값을 1로 지정
    # 조회
    question_list = Question.objects.order_by('-q_date')
    # print('question_list: ', question_list)

    # 페이징 처리
    pagenator = Paginator(question_list, 5)
    # 페이징을 할 목록과 페이지에 표시될 항목 수
    # Paginator 클래스는 question_list를 페이징 처리(인스턴스)로 변환
    # 변환한 내용을 pagenator 객체(인스턴스)에 저장
    # Paginator 클래스를 호출하면서 두 번째 인수에 페이지당 표시될 할목 수 입력
    page1 = pagenator.get_page(page)
    # Paginator 클래스를 사용해 객체에 쓸 수 있는 속성
    # .count: 게시물의 개수(전체)
    # .per_page: 페이지당 보여줄 게시물 개수
    # .page_range: 페이지의 범위
    # .number: 현재 페이지의 번호
    # .previous_page_number: 이전 페이지 번호
    # .next_page_number: 다음 페이지 번호
    # .start_index: 현재 페이지 시작 인덱스
    # .end_index: 현재 페이지 끝 인덱스
    # .has_previous: 이전 페이지 유무
    # .has_next: 다음 페이지 유무

    context = {'question_list1': page1}
    # print('question_list: ', context)
    return render(request, 'newapp/question_list.html', context)

def detail(request, question_id):

    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question1': question}
    return render(request, 'newapp/question_detail.html', context)

# 404 페이지
# 요청하는 페이지가 없거나 서버에서 오류가 발생하면 반환되는 응답 코드
# 기본적으로 정상 처리되면 200을 반환, 서버 오류는 500을 반환하기도 함

# 21/04/13 김인웅 답변 등록 페이지 함수
# @login_required(login_url='common:login')
# def answer_create(request, question_id):
#
#     question = get_object_or_404(Question, pk=question_id)
#     if request.method == 'POST':
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.author = request.user
#             answer.a_date = timezone.now()
#             answer.save()
#             return redirect('newapp:detail', question_id=question.id)
#     else:
#         form = AnswerForm()
#     return render(request, 'newapp/question_detail.html', {'question1': question, 'form': form})

@login_required(login_url='common:login')
def answer_create(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.a_date = timezone.now()
            answer.a_subject = question
            answer.save()
            return redirect('newapp:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question1': question, 'form': form}
    return render(request, 'newapp/question_detail.html', context)

# -------------------------------------------------------------------------------------- #

# --------------------------------[edit 21/04/14 김인웅]--------------------------------- #
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

    # 위에 작성한 코드는 아래 4월 14일에 작성한 코드를 다시 한 번 한 것임
    # if request.method == 'POST':
    #     form = QuestionForm(request.POST)
    #     if form.is_valid():
    #         question = form.save(commit=False)
    #         # 폼에 입력한 값을 임시 저장(실제 데이터는 아직 저장되지 않음)
    #         # commit=False이 없으면 q_date가 없다고 에러 뜸
    #         question.author = request.user
    #         question.q_date = timezone.now()
    #         # 아직 q_date가 없으므로 이를 받아서
    #         question.save()
    #         # 저장
    #         return redirect('newapp:index')
    # else:
    #     form = QuestionForm()
    # return render(request, 'newapp/question_form.html', {'form': form})
# -------------------------------------------------------------------------------------- #

# --------------------------------[edit 21/04/21 김인웅]--------------------------------- #
@login_required(login_url='common:login')
def question_modify(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)

    if request.user != question.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('newapp:detail', question_id=question.id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        # form에서 받아온 내용의 내부 구조를 정의할 때 사용
        # 기존의 데이터를 받아와서 내용을 수정하기 위해 선언
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

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user != answer.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('newapp:detail', question_id=answer.a_subject.id)

    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('newapp:detail', question_id=answer.a_subject.id)
    else:
        form = AnswerForm(instance=answer)

    return render(request, 'newapp/answer_form.html', {'answer': answer, 'form': form})

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user != answer.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('newapp:detail', question_id=answer.a_subject.id)
    else:
        answer.delete()
    return redirect('newapp:detail', question_id=answer.a_subject.id)
# -------------------------------------------------------------------------------------- #

# --------------------------------[edit 21/04/22 김인웅]--------------------------------- #
# 댓글 달기 기능 구현
@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            return redirect('newapp:detail', question_id=question_id)
    else:
        form = CommentForm()
    return render(request, 'newapp/comment_form.html', {'form': form})

@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('newapp:detail', question_id=comment.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('newapp:detail', question_id=comment.question.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'newapp/comment_form.html', {'form': form})

@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('newapp:detail', question_id=comment.question.id)
    else:
        comment.delete()
    return redirect('newapp:detail', question_id=comment.question.id)

@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('newapp:detail', question_id=comment.answer.a_subject.id)
    else:
        form = CommentForm()
    return render(request, 'newapp/comment_form.html', {'form': form})

@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('newapp:detail', question_id=comment.answer.a_subject.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('newapp:detail', question_id=comment.answer.a_subject.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'newapp/comment_form.html', {'form': form})

@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('newapp:detail', question_id=comment.answer.a_subject.id)
    else:
        comment.delete()
    return redirect('newapp:detail', question_id=comment.answer.a_subject.id)
# -------------------------------------------------------------------------------------- #