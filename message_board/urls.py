from django.urls import path
from .views import ListView

urlpatterns = [
    path('<int:pk>/', ListView.as_view()),
]
