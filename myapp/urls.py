from django.urls import path
from . import views
urlpatterns = [
    path('Hello/', views.say_hello),
    path('home/', views.homepage),
    path('about/', views.about),
    path('contact/', views.contact),
    path('order/',views.order),
    path('experiment/',views.experiment),
    path('experiment/<person>',views.experiment)
]
