
from django.urls import path
# ---------------------------------[edit]---------------------------------- #
from .views import base_views, question_views, answer_views, comment_views
# ------------------------------------------------------------------------- #
# -----------------------------[edit 21/04/12]----------------------------- #
app_name = 'newapp'
# url에 별칭 부여하기
# url에 별칭을 부여하는 것은 실제 주소인 /newapp/이 index라는 별칭으로 변경됨
# 앱(newapp 같은 것)을 추가할 때 다른 앱과 url 별칭이 중복되면 안 된다.
# url 설정할 때 네임스페이스를 이용해서 독립된 이름 공간을 생성해야 한다.
# 네임스페이스: 각각의 앱이 관리하는 공간
# 네임스페이스 변수를 만들면 저장되는 문자열 값은 앱 이름과 동일하게 하는 것이 좋다.
# ------------------------------------------------------------------------- #

urlpatterns = [
    path('', base_views.index, name='index'),
# ---------------------------------[edit]---------------------------------- #
# 2021.04.12 김인웅
# 게시글 클릭 시 들어갈 페이지 추가
# 게시글 답변 작성 페이지 추가
    path('<int:question_id>/', base_views.detail, name='detail'),
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question, name='comment_delete_question'),
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),
]