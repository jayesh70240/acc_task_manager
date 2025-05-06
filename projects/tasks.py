from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Task

@shared_task
def send_deadline_reminders():
    now = timezone.now()
    upcoming = Task.objects.filter(deadline__lte=now + timedelta(hours=1), status__in=['pending', 'ongoing'])
    for task in upcoming:
        print(f"Reminder: Task '{task.title}' is due soon!")
