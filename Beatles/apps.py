from django.apps import AppConfig

class BeatlesConfig(AppConfig):
    """
    Configuration class for the 'Beatles' Django app.

    This class specifies the default auto field for database models
    and the name of the app. It is automatically recognized by Django
    when the app is included in the INSTALLED_APPS setting.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Beatles'
