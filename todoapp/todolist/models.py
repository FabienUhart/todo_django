from django.db import models
from django.utils import timezone

# Create your models here.
STATE_CHOICES = [
    ('RUN', 'Running'),
    ('DONE', 'Done'),
    ('INTER', 'Interrupted'),
]


class Todo(models.Model):
    """  BASE Model todolist"""
    title = models.CharField(max_length=250)
    details = models.TextField(default=None, null=True)
    state = models.CharField(
        max_length=5,
        choices=STATE_CHOICES,
        default=STATE_CHOICES[0],
    )
    state_order = models.IntegerField(default=0)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)
