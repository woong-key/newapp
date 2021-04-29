from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from newapp.models import Question
from django.db.models import Q

# from ..(상위 폴더의 상위 폴더) models import Question 요렇게 쓸 수도 있어요.


def index(request):

    page = request.GET.get('page', '1')

# 2021/04/28 김인웅 - 검색 view 구현
    kw = request.GET.get('kw', '')
    question_list = Question.objects.order_by('-q_date')

    if kw:
        question_list = question_list.filter(
            Q(q_subject__icontains=kw) |
            Q(q_content__icontains=kw)
        ).distinct()
    # .filter: 조건에 맞는 여러 행을 출력할 때 사용
    # .filter와 연계해서 사용하는 키워드
    # __icontains: 해당 컬럼의 값이 지정한 문자열을 포함하는 항목을 검색
    # __istartswith: 해당 컬럼값이 지정한 문자열로 '시작'하는 항목을 검색
    # __endswith: 해당 컬럼값이 지정한 문자열로 '끝'나는 항목을 검색
    # __in: 주어진 값 안에 존재하는 항목을 검색 ex) id__in=[3,5,7] 그럼 id가 3, 5, 7인 항목 출력
    # __year: 해당 년도 검색 ex) create_date__year=2021
    # __month, __day도 가능
    # __isnull: null인 항목 검색

    pagenator = Paginator(question_list, 5)
    page1 = pagenator.get_page(page)
    context = {'question_list1': page1, 'page': page, 'kw': kw}
    return render(request, 'newapp/question_list.html', context)


def detail(request, question_id):

    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question1': question}
    return render(request, 'newapp/question_detail.html', context)
