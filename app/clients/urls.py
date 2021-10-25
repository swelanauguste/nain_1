from django.urls import path

from . import views

app_name = "clients"


urlpatterns = [
    path("", views.ClientListView.as_view(), name="client-list"),
    path("client/<int:pk>/", views.ClientDetailView.as_view(), name="client-detail"),
    path(
        "client/update/<int:pk>/",
        views.ClientUpdateView.as_view(),
        name="client-update",
    ),
    path("locations/", views.LocationListView.as_view(), name="location-list"),
    path(
        "location/<int:pk>/", views.LocationDetailView.as_view(), name="location-detail"
    ),
    path(
        "location/update/<int:pk>/",
        views.LocationUpdateView.as_view(),
        name="location-update",
    ),
    path(
        "location/create/",
        views.LocationCreateView.as_view(),
        name="location-create",
    ),
]
