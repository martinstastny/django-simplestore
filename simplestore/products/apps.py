from django import apps


class AppConfig(apps.AppConfig):
    name = "simplestore.products"

    def ready(self):
        # noinspection PyUnresolvedReferences
        from . import signals
