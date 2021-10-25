from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Location(models.Model):
    name = models.CharField(max_length=50)

    # class Meta:
    #     verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class Client(models.Model):
    """
    Client model.
    """

    user = models.OneToOneField("User", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=254, blank=True)
    last_name = models.CharField(max_length=254, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.ForeignKey(
        "Location", on_delete=models.SET_NULL, null=True, related_name="cities"
    )
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f"/client/{self.id}"

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.user.username


    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.user.username
