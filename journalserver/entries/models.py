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
    RESPONSE_TYPES = (
        ('LS', 'Likert Scale'),
        ('MC', 'Multiple Choice'),
        ('NV', 'Numerical Value'),
    )

    metric_name = models.CharField(max_length=50)
    is_default = models.BooleanField(default=False)
    question_text = models.CharField(max_length=200)
    response_type = models.CharField(
        max_length=2,
        choices=RESPONSE_TYPES,
        default='LS',
    )
    ls_scale = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),  # Minimum value
            MaxValueValidator(100)  # Maximum value you want to set
        ],
        null=True,
        default=None,
        help_text='How many points should this likert scale have?')
    mc_choices = models.CharField(
        max_length=200,
        null=True,
        default=None,
        help_text='The multiple choice options, comma separated'
    )
    nv_max = models.IntegerField(
        null=True,
        default=None,
        help_text='The maximum value for these numerical responses'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.metric_name
    

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')
    entry_date = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name_plural = "Entries"

    def __str__(self):
        return f'Entry by {self.user} on {self.entry_date}' 

def validate_response_value(value):
    max_value = value.question.response_schema.scale
    if not 1 <= value <= max_value:
        raise ValidationError(f"Response value must be between 1 and {max_value} inclusive")


class Response(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='responses')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='responses')
    #
    response_value = models.SmallIntegerField(
        validators=[validate_response_value]
    )

    def __str__(self):
        return f'{self.question}: {self.response_value}'
    
    
class EntryText(models.Model):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE, related_name='entry_text')
    text = models.TextField()

    def __str__(self):
        return 'Journal text entry. Do you really want the full text?'

