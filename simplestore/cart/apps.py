from django.apps import AppConfig
from django.db.models.signals import post_save, pre_save, post_delete

class CartConfig(AppConfig):
    name = 'simplestore.cart'

    def ready(self):
        from . import signals
        pre_save.connect(receiver=signals.cart_item_pre_save_receiver, sender='cart.CartItem')
        post_save.connect(receiver=signals.cart_item_post_save_receiver, sender='cart.CartItem')
        post_delete.connect(receiver=signals.cart_item_post_save_receiver, sender='cart.CartItem')