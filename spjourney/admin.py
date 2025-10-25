from django.contrib import admin

# Register your models here.
from django.contrib import admin  # Import admin module
from .models import LearningJourney, AboutMe  # Import models from this app

# Register models so they appear in the Django admin site
admin.site.register(LearningJourney)
admin.site.register(AboutMe)

