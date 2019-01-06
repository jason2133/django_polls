from django.db import models

# Create your models here.

# Polls 애플리케이션에서는 Question과 Choice 2개의 테이블이 필요함

class Question(models.Model): # 투표 질문
    question_text = models.CharField(max_length = 200) 
    # Question 문자열 length 최대 200자
    
    pub_date = models.DateTimeField('date published')
    # pub_date 생성시간 DateTime 형식으로 하고, date published 띄워라

    def __str__(self):
        # 객체를 문자열로 표현할 때 사용하는 함수
        return self.question_text
        # Question_text 문자열 리턴해라

# 각 필드를 분리해서 보여주기
# class QuestionAdmin(admin.ModelAdmin) :
#     fieldsets = [
#         ('Question Statement', {'fields' : ['question_text']}),
#         ('Date Information', {'fields' : ['pub_date']}),
#     ]

# 필드를 접어서 보여주기
# class QuestionAdmin(admin.ModelAdmin) :
#     fieldsets = [
#         ('Question Statement', {'fields' : ['question_text'], 'classes' : ['collapse']}),
#         ('Date Information', {'fields' : ['pub_date'], 'classes' : ['collapse']}),
#     ]

class Choice(models.Model): # 투표 항목 선택
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    # 질문
    
    choice_text = models.CharField(max_length = 200)
    # 투표 항목 선택 : 문자열 length 최대 200자
    
    votes = models.IntegerField(default = 0)
    # 투표
    # 기본값은 0이지 투표 값은

    def __str__(self):
        return self.choice_text



