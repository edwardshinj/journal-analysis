from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Prefetch
from .models import User, Question, Entry, Choice
from .serializers import UserSerializer, QuestionSerializer, ChoiceSerializer


# Create your views here.
def questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return JsonResponse(serializer.data, safe=False)



def allUserEntries(reques, username):
    #username = request.GET.get('username')
    try:
        user = User.objects.get(username=username) 
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    
    results = []
    
    choices_queryset = Choice.objects.select_related('question')
    entries = Entry.objects.filter(user=user).prefetch_related(Prefetch('choices', queryset=choices_queryset))

    #for each entry, get all the answers
    for entry in entries: 
        entry_info = {
            'entry_id': entry.id,
            'entry_date': entry.entry_date,
            'questions' : []
        }

        for choice in entry.choices.all():
            question = choice.question
            entry_info['questions'].append({
                'question_text': question.question_text,
                'choice_value': choice.choice_value
            })

        results.append(entry_info)

    return JsonResponse(results, safe=False)




    #return entries > list of questions and answers