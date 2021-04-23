"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# ---------------------------------[edit]---------------------------------- #
from newapp.views import base_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # admin 페이지는 dJango에서 기본으로 세팅해준다.
    # path('newapp/', views.index)
    path('newapp/', include('newapp.urls')),
    # 모두 newapp/urls.py 파일에 있는 매핑을 참고 하여 처리하라는 의미
    # 이러한 선언으로 요청은 앞으로 newapp/urls.py에서 관리하는 것으로 인식
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),
]
# -------------------------------------------------------------------------- #