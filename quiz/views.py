
from .serializers import RandomQuestionSerializer,QuestionSerializer, QuizSerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import  Quizzes ,Question
from rest_framework.views import APIView



class Quiz(generics.ListAPIView):
    serializer_class=QuizSerializer
    queryset=Quizzes.objects.all()
   
class RandomQuestion(APIView):

    def get(self, request, format:None, **kwargs):
        Question= Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(Question, many=True)
        return  Response(serializer.data)
        
class QuizQuestion(APIView):
    
    def get(self, request, format:None, **kwargs):
        Question = Question.objects.filter(quiz_title=kwargs['topic'])
        serializer= QuestionSerializer( Question,many=True)
        return  Response(serializer.data)