from . import views
from django.urls import path

urlpatterns = [
    path('polls/', views.ListPollView.as_view()),
    path('poll/<int:pk>/', views.DetailPollView.as_view()),
    path('poll/create/', views.CreatePollView.as_view()),
    path('poll/<int:pk>/update/', views.UpdatePollView.as_view()),
    path('poll/<int:pk>/delete/', views.DeletePollView.as_view()),
    path('poll/active_list/', views.ActivePollView.as_view()),
    path('question/create/', views.CreateQuestionView.as_view()),
    path('questions/', views.ListQuestionView.as_view()),
    path('question/<int:pk>/update/', views.UpdateQuestionView.as_view()),
    path('question/<int:pk>/delete/', views.DeleteQuestionView.as_view()),
    path('answer/<int:user_id>/', views.answer_view),
    path('answer/create/', views.CreateAnswerView.as_view()),

]