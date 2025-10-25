from django.urls import path  # Import path for URL routing
from . import views  # Import views from this app

urlpatterns = [
    path('', views.index, name='index'),  # Home page which is the index view
    path('about/', views.about_me, name='about'),  # About Me page which is the about_me view
]