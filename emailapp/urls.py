from django.urls import path
from . import views
urlpatterns = [
    path('showmail/', views.getmail)
]
