from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from users.models import User


class ResponseSchema(models.Model):
    scale = models.SmallIntegerField(
        validators=[MinValueValidator(2), MaxValueValidator(7)],
        default = 5
    )
    lowerLabel = models.CharField(max_length=20)
    upperLabel = models.CharField(max_length=20)

    # e.g. '1 to 5' or '1 (disagree) to 5 (agree)'
    def __str__(self):
        return f'1{' (' + self.lowerLabel + ') ' if self.lowerLabel else ''} to {self.scale}{
            ' (' + self.upperLabel + ')' if self.upperLabel else ''}'
    

# Represents each quantitative question/metric
class Question(models.Model):
    metric_name = models.CharField(max_length=50)
    is_default = models.BooleanField(default=False)
    question_text = models.CharField(max_length=200)
    response_schema = models.ForeignKey(ResponseSchema, on_delete=models.PROTECT)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.metric_name
    

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')
    entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Entry by {self.user} on {self.entry_date}' 

def validate_choice_value(value):
    max_value = value.question.response_schema.scale
    if not 1 <= value <= max_value:
        raise ValidationError(f"Choice value must be between 1 and {max_value} inclusive")


class Choice(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='choices')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    #
    choice_value = models.SmallIntegerField(
        validators=[validate_choice_value]
    )

    def __str__(self):
        return f'{self.question}: {self.choice_value}'
    
    
class EntryText(models.Model):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE, related_name='entry_text')
    text = models.TextField()

    def __str__(self):
        return 'Journal text entry. Do you really want the full text?'

