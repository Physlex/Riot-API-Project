""" This module implements the url paths associated with the Django-Cassiopeia API.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
