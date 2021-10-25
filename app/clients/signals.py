from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .models import Client, User



@receiver(post_save, sender=User)
def create_client_profile(sender, instance, created, **kwargs):
    if created:
        Client.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_client_profile(sender, instance, **kwargs):
    instance.client.save()
