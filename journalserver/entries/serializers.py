from rest_framework import serializers
from .models import User, Question, Choice, Entry, EntryText

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'join_date']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'metric_name', 'is_default', 'question_text', 'pub_date']

class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    question_id = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all(),
        source='question',
        write_only=True
    )
    class Meta: 
        model = Choice
        fields = ['id', 'question', 'question_id', 'choice_value']

#not yet used anywhere. 
class EntryTextSerializer(serializers.ModelSerializer): 
    class Meta:
        model = EntryText
        fields = ['id', 'text']

class EntrySerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta: 
        model = Entry
        fields = ['id', 'user', 'entry_date', 'choices']

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        entry = Entry.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(entry=entry, **choice_data)
        return entry