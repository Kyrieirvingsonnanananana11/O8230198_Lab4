from django.shortcuts import render
from .models import LearningJourney, AboutMe

# Home page view
def index(request):
    journeys = LearningJourney.objects.all()  # get all records
    return render(request, 'index.html', {'journeys': journeys})

# About Me page view
def about_me(request):
    about = AboutMe.objects.first()  # get the first record
    return render(request, 'aboutMe.html', {'about': about})
