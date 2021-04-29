from django.db import models
# ----------------------------------[edit 21/04/20 김인웅]----------------------------------- #
from django.contrib.auth.models import User
# ------------------------------------------------------------------------------------------ #
# Create your models here.

class Question(models.Model):
# 질문의 속성(컬럼): 제목(q_subject), 내용(q_content), 생성시간(q_date), 글쓴이(author)
    q_subject = models.CharField(max_length=100)
    q_content = models.TextField()
    q_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='author_question')
    modify_date = models.DateTimeField(null=True, blank=True)
    # author 컬럼은 User 테이블의 외래 키로 적용시킴
    # on_delete=models.CASCADE: 계정이 삭제되면 계정과 연결된 Question 데이터 모두 삭제
# ----------------------------------[edit 21/04/26 김인웅]----------------------------------- #
# 추천 컬럼 추가
    voter = models.ManyToManyField(User, related_name='voter_question')
    # 컬럼 간 관계를 표현하기 위한 문법(속성)
    # 1:N 관계 한쪽이 관계를 맺은 다른 쪽의 여러 객체를 가지는 것
# ------------------------------------------------------------------------------------------ #
    def __str__(self):
        return self.q_subject

class Answer(models.Model):
# 답변의 속성(컬럼): 제목(a_subject), 내용(a_content), 생성시간(a_date), 글쓴이(author)
    a_subject = models.ForeignKey(Question, on_delete=models.CASCADE)
    a_content = models.TextField()
    a_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='author_answer')
    modify_date = models.DateTimeField(null=True, blank=True)
    # blank=True는 form.is_valid()에서 데이터 검사 시 값이 없어도 된다.
    voter = models.ManyToManyField(User, related_name='voter_answer') # edit 21/04/27 김인웅

    def __str__(self):
        return self.a_subject

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)