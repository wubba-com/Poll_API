from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Polls, Questions, Answer, Choice
from .serializer import (
    PollListSerializer,
    PollSerializer,
    QuestionSerializer,
    PollDetailSerializer,
    AnswerSerializer,
    ChoiceSerializer
)
from rest_framework import generics
from rest_framework import permissions
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes


class ListPollView(APIView):
    """Список всех опросов"""

    def get(self, request):
        polls = Polls.objects.all()
        serializer = PollListSerializer(polls, many=True)
        return Response(serializer.data)


class DetailPollView(APIView):
    """Подробный вывод опроса"""

    def get(self, request, pk):
        poll = Polls.objects.get(id=pk)
        serializer = PollDetailSerializer(poll)
        return Response(serializer.data)


class CreatePollView(generics.CreateAPIView):
    """Создание опроса"""
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Polls.objects.all()


class UpdatePollView(generics.UpdateAPIView):
    """Изменение опроса"""
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        poll = Polls.objects.all()
        return poll


class DeletePollView(generics.DestroyAPIView):
    """Удаление опроса"""
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Polls.objects.all()


class ActivePollView(APIView):
    """Список всех активных опросов"""
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        polls = Polls.objects.filter(date_start__lte=timezone.now(), date_finish__gte=timezone.now())
        serializer = PollListSerializer(polls, many=True)
        return Response(serializer.data, status=200)


class ListQuestionView(APIView):
    """Список всех вопросов"""

    def get(self, request):
        questions = Questions.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class CreateQuestionView(generics.CreateAPIView):
    """Создание вопроса"""
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UpdateQuestionView(generics.UpdateAPIView):
    """Обновление вопроса"""
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        questions = Questions.objects.all()
        return questions


class DeleteQuestionView(generics.DestroyAPIView):
    """Удаление опроса"""
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def answer_view(request, user_id):
    """Просмотр ответов от пользователей"""
    answers = Answer.objects.filter(user_id=user_id)
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)


class CreateAnswerView(generics.CreateAPIView):
    """Создание ответа на опрос"""
    serializer_class = AnswerSerializer
    permission_classes = (permissions.IsAuthenticated,)


