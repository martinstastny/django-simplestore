from django import apps


class AppConfig(apps.AppConfig):
    name = "simplestore.checkout"

    def ready(self):
        # noinspection PyUnresolvedReferences
        from . import signals
