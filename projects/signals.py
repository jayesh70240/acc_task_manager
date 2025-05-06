from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Task

@receiver(pre_save, sender=Task)
def notify_on_status_change(sender, instance, **kwargs):
    if instance.pk:
        old = Task.objects.get(pk=instance.pk)
        if old.status != instance.status:
            print(f"Task '{instance.title}' status changed from {old.status} to {instance.status}")
