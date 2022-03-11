# from django.urls import path
# from rest_framework import routers
# from .views import QuizRead, QuizListView, QuestionRead
# urlpatterns = [
#     path("", QuizListView.as_view(), name='quiz'),
#     path("<category>/", QuizRead.as_view(), name='quiz_read'),
#     path("<category>/<quiz>/", QuestionRead.as_view(), name="question_read")
# ]
from django.urls import path
from.views import Quiz,RandomQuestion,QuizQuestion
app_name='quiz'
urlpatterns=[
    path('', Quiz.as_view(), name='quiz'),
    path('r/<str>/',RandomQuestion.as_view(), name='random'),
    path('q/<str:topic>/',QuizQuestion.as_view(),name='questions'),
]
