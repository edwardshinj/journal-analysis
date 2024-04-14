import datetime
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Question(models.Model):
    # Represents each quantitative question/metric
    metric_name = models.CharField(max_length=50)
    default = models.BooleanField(default=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_date = models.DateTimeField(auto_now_add=True)

class Choice(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='choices')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_value = models.SmallIntegerField(default = 0)

    def __str__(self):
        return str(self.choice_value)

