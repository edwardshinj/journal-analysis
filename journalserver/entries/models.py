from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Question(models.Model):
    # Represents each quantitative question/metric
    metric_name = models.CharField(max_length=50)
    is_default = models.BooleanField(default=True, verbose_name="Default Question")
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')
    entry_date = models.DateTimeField(auto_now_add=True)

class Choice(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='choices')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_value = models.SmallIntegerField(default = 0)

    def __str__(self):
        return str(self.choice_value)
    
class EntryText(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='entry_text')
    text = models.TextField()

    def __str__(self):
        return str('Journal text entry')

