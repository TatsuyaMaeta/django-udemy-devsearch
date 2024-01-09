from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    # signalをアプリにキャッチさせたいのであればappsのところに書く必要がある
    def ready(self):
        import users.signals
