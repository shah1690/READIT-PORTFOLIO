from django.urls import path

from team.views import team_view

urlpatterns = [
    path('', team_view, name='team'),
]
