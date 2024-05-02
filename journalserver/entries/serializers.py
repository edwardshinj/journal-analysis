from rest_framework import serializers
from .models import User, Question, Response, Entry, EntryText

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'join_date']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'metric_name', 'is_default', 'question_text', 'pub_date']

class ResponseSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    question_id = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all(),
        source='question',
        write_only=True
    )
    class Meta: 
        model = Response
        fields = ['id', 'question', 'question_id', 'response_value']

#not yet used anywhere. 
class EntryTextSerializer(serializers.ModelSerializer): 
    class Meta:
        model = EntryText
        fields = ['id', 'text']

class EntrySerializer(serializers.ModelSerializer):
    response = ResponseSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta: 
        model = Entry
        fields = ['id', 'user', 'entry_date', 'responses']

    def create(self, validated_data):
        responses_data = validated_data.pop('responses')
        entry = Entry.objects.create(**validated_data)
        for response_data in responses_data:
            Response.objects.create(entry=entry, **response_data)
        return entry