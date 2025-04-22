from django.urls import path
from .views import HomeView

urlpatterns = [
    path('anasayfa/', HomeView.as_view())
]
