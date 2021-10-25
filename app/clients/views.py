from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Client, Location


class LocationListView(LoginRequiredMixin, ListView):
    model = Location


class LocationDetailView(LoginRequiredMixin, DetailView):
    model = Location


class LocationCreateView(LoginRequiredMixin, CreateView):
    model = Location
    fields = "__all__"


class LocationUpdateView(LoginRequiredMixin, UpdateView):
    model = Location
    fields = "__all__"


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = "__all__"
