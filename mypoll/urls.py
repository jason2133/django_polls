"""mypoll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from polls import views
# # Polls 투표를 Views로 해줘요


# # app_name = 'polls'

# urlpatterns = [ # URL / 뷰 매핑을 정의하는 방식은 항상 동일함
#     path('admin/', admin.site.urls), # Admin
#     path('polls/', views.index, name='index'), # 초기화면
#     path('polls/<int:question_id>/', views.detail, name='detail'), # 투표 질문거리 던져요
#     # 사용자가 질문 하나를 선택하면 detail() 뷰 함수가 호출되는 것임!
#     path('polls/<int:question_id>/results/', views.results, name='results'), # 투표 결과 보여줘요
#     path('polls/<int:question_id>/vote/', views.vote, name='vote'), # 투표하고 싶어요!
# ]

# path('polls/<int:question_id>/vote/', views.vote, name='vote')
#                  Routes                  Views      Name
# Routes : URL 패턴을 표현하는 문자열
# Views : URL 스트링이 매칭되면 호출되는 뷰 함수
# Kwargs
# Name : 각 URL 패턴별로 이름을 붙여줌. 여기서 정해진 이름은 Template 파일에서 많이 사용됨!


# URLS를 2개의 파일에 나누어서 정리해보자!

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]

