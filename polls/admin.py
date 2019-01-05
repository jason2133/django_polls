from django.contrib import admin
# admin 관리자 불러오기

from polls.models import Question, Choice
# Poll 투표모델 - Question과 Choice 불러오기

# Models.py에서 정의한 테이블인 Question과 Choice가 Admin에서도 보이도록 만듦
admin.site.register(Question)
admin.site.register(Choice)
# import한 클래스를 admin.site.regeister 함수를 사용하여 Admin 사이트에 등록




