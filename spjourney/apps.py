from django.apps import AppConfig  # Import AppConfig to configure app settings

# Configuration for the spjourney app
class SpjourneyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Default type for primary keys
    name = 'spjourney'  # Name of the app
