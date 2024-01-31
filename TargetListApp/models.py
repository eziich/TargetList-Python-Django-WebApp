from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    low = 'Nizak'
    medium = 'Srednji'
    high = 'Visok'

    Priority_choice = [
        (low, 'Nizak'),
        (medium, 'Srednji'),
        (high, 'Visok')
    ]

    not_started = 'Zadatak nije započet'
    in_progress = 'Zadatak se izvršava'
    done = 'Zadatak je završen'

    Status_choice = [
        (not_started, 'Zadatak nije započet'),
        (in_progress, 'Zadatak se izvršava'),
        (done, 'Zadatak je završen'),
    ]

    task_name = models.CharField(max_length=20, blank=False, null=False)
    task_description = models.CharField(max_length=256)
    task_priority = models.CharField(max_length=20, choices=Priority_choice, default=medium)
    task_status = models.CharField(max_length=20, choices=Status_choice, default=not_started)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


