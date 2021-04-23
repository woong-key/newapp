# -----------------------------[edit 21/04/14 김인웅]----------------------------- #
from .models import Question, Answer, Comment
from django import forms


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['q_subject', 'q_content']
        # widget = {
        #     'q_subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'q_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10})
        # }
        labels = {
            'q_subject': '글 제목',
            'q_content': '글 내용',
        }

# -----------------------------[edit 21/04/20 김인웅]----------------------------- #
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['a_content']
        # widget = {
        #     'a_subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'a_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10})
        # }
        labels = {
           #'a_subject': '답변 제목',
            'a_content': '답변 내용',
        }
# ------------------------------------------------------------------------------- #

# -----------------------------[edit 21/04/21 김인웅]----------------------------- #
# Comment 클래스 추가
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글 내용',
        }
