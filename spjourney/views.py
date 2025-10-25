from django.shortcuts import render
from .models import LearningJourney, AboutMe  # Import models

def index(request):
    journeys = LearningJourney.objects.all()  # Get all learning journey entries
    return render(request, 'index.html', {'journeys': journeys})  # Render home page

def about_me(request):
    about = AboutMe.objects.first()  # Get first AboutMe entry
    return render(request, 'aboutMe.html', {'about': about})  # Render About Me page

