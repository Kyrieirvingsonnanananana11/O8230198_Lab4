from django.db import models

# Create your models here.
from django.db import models  # Import Django models

# Model for learning journey entries
class LearningJourney(models.Model):
    title = models.CharField(max_length=100)  # Title of the journey
    description = models.TextField()          # Description
    date = models.DateField(auto_now_add=True)  # Date added automatically

    def __str__(self):
        return self.title  # Display title in admin

# Model for personal details
class AboutMe(models.Model):
    name = models.CharField(max_length=100)  # Your name
    bio = models.TextField()                 # Short bio
    email = models.EmailField(blank=True)    # Email (optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Date created automatically

    def __str__(self):
        return self.name  # Display name in admin

