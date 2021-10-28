from django.db import models
from datetime import timezone, datetime, timedelta

# Create your models here.
STATE_CHOICES = [
    ('RUN', 'Running'),
    ('DONE', 'Done'),
    ('INTER', 'Interrupted'),
]


class Todo(models.Model):
    """  BASE Model todolist"""
    title = models.CharField(max_length=250)
    details = models.TextField()
    state = models.CharField(
        max_length=5,
        choices=STATE_CHOICES,
        default=STATE_CHOICES[0],
    )
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
