from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from newapp.models import Question
# from ..(상위 폴더의 상위 폴더) models import Question 요렇게 쓸 수도 있어요.


def index(request):

    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-q_date')
    pagenator = Paginator(question_list, 5)
    page1 = pagenator.get_page(page)
    context = {'question_list1': page1}
    return render(request, 'newapp/question_list.html', context)


def detail(request, question_id):

    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question1': question}
    return render(request, 'newapp/question_detail.html', context)
