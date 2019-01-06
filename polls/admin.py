from django.contrib import admin
# admin 관리자 불러오기

from polls.models import Question, Choice
# Poll 투표모델 - Question과 Choice 불러오기

# class ChoiceInline(admin.StackedInline) # Question 및 Choice를 한 화면에서 변경하기
class ChoiceInline(admin.TabularInline): # 테이블 형식으로 보여주기
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text'] # 필드 순서 변경
    fieldsets = [ # 각 필드를 분리해서 보여주기
        ('Question Statement', {'fields': ['question_text']}),
        # ('Date Information', {'fileds' : ['pub_date']}),
        ('Date Information', {'fileds' : ['pub_date'], 'classes' : ['collapse']}), # collapse : 필드 접기
    ]
    inlines = [ChoiceInline] # Choice 모델 클래스 같이 보기
    list_display = ('question_text', 'pub_date') # 레코드 리스트 칼럼 항목 지정
    list_filter = ['pub_date'] # list_filter 필터 필터 사이드 바 추가
    search_fields = ['question_text'] # search_fields 검색 기능 추가

# Models.py에서 정의한 테이블인 Question과 Choice가 Admin에서도 보이도록 만듦
admin.site.register(Question)
admin.site.register(Choice)
# import한 클래스를 admin.site.regeister 함수를 사용하여 Admin 사이트에 등록




