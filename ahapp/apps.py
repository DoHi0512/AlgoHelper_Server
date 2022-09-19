from django.apps import AppConfig

class AhappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ahapp'
    def ready(self):
        from .views import main
        main()
    



