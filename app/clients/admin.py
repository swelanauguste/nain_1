from django.contrib import admin

from .models import Client, Location, User

admin.site.register(Client)
admin.site.register(Location)
admin.site.register(User)
