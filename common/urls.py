# --------------------------------[edit 21/04/16 김인웅]--------------------------------- #
# 로그인 로그아웃 구현을 위한 url 참조 추가
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
]
# -------------------------------------------------------------------------------------- #