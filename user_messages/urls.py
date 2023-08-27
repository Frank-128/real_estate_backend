"""
user_messages api
"""

from django.urls import path

from user_messages import views



urlpatterns = [
    path("chating", views.UserMessageAPIView.as_view())
]