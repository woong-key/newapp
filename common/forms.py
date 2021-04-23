# --------------------------------[edit 21/04/19 김인웅]--------------------------------- #
# 회원 가입 폼 작성

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    # UserCreationForm을 가용해서 회원 가입의 기본 속성을 받아올 수 있다.
    # 받아오는 기본 속성은 username, password1, password2
    # email 등 다른 속성들을 추가해서 회원 가입 시 입력하게 만들 수 있다.
    email = forms.EmailField(label='이메일')
    class Meta:
        model = User
        fields = ('username', 'email')

        # Meta 클래스: UserForm의 내부 클래스
        #