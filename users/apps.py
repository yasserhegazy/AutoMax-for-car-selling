from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    def ready(self):
        import users.signals
        # This method is called when the app is ready.
        # It imports the signals module to ensure that the signal handlers are connected.
        # This is necessary to ensure that the signal handlers are registered when the app is loaded.
        # Without this, the signal handlers would not be connected, and the Profile model would not
