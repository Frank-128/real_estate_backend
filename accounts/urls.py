from django.urls import path
from . import views

urlpatterns = [
    path('register',views.AccountAPIView.as_view())
]
