from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Prefetch
from rest_framework import permissions, viewsets
from .models import User, Question, Entry, Choice
from .serializers import UserSerializer, QuestionSerializer, EntrySerializer

#Class way of getting all entries? 
class EntryViewSet(viewsets.ModelViewSet):
    choices_queryset = Choice.objects.select_related('question')
    queryset = Entry.objects.prefetch_related(Prefetch('choices', queryset=choices_queryset)) #.filter(user=user)
    serializer_class = EntrySerializer
    #permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# Get all questions to show
def questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return JsonResponse(serializer.data, safe=False)
