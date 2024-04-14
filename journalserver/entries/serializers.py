from rest_framework import serializers
from .models import User, Question, Choice

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['username']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['metric_name', 'default', 'question_text', 'pub_date']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Choice
        fields = ['user', 'question', 'choice_value', 'choice_date']