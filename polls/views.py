# index() 함수 작성

from django.shortcuts import render
from django.shortcuts import get_object_or_404
# get object or 404 함수를 임포트함

from django.http import HttpResponseRedirect
from django.urls import reverse

from polls.models import Question # 질문
from polls.models import Choice # 선택거리

def index(request): # 초기 화면
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    # -pub_date의 정렬 (역순으로 정렬)해서 최근 5개의 질문을 갖고 온다
    # 잘보면 앞에 - 마이너스가 있다는 사실을 알 수 있다 -> 역순으로 정렬한다

    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)
    # HTML Template와 연결

def detail(request, question_id): # 디테일 - 질문 이름이랑 내용 불러오기
    question = get_object_or_404(Question, pk=question_id)
    # 조건에 맞는 객체 object가 없다면 HTTP 404 익셉션을 발생시킴
    return render(request, 'polls/detail.html', {'question' : question})
    # HTML Template와 연결

def vote(request, question_id): # 투표하기
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 설문 투표 폼을 다시 보여준다
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice.", 
        })
    else:
        selected_choice.votes += 1
        # 정상적으로 처리되면 투표수를 올려요
        selected_choice.save()
        # 그리고 저장시켜요

        # POST 데이터를 정상적으로 처리하였으면
        # 항상 HttpResponseRedirect를 반환하여 Redirection을 처리함
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        # reverse 함수를 사용하여 URL 추출
        # URL 패턴명으로부터 URL 스트링을 구함

def results(request, question_id):
    # 결과 보여주기
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question' : question})
    # HTML Template와 연결




