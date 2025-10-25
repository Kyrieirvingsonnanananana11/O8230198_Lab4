from django.db import models

# Create your models here.
from django.db import models

class LearningJourney(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)  # Automatically store when added

    def __str__(self):
        return self.title

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
