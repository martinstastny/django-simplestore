from django.conf.urls import url
from .views import ProductListView, CartView

urlpatterns = [
    url('^products/', ProductListView.as_view(), name='products'),
    url('^cart/', CartView.as_view(), name='cart'),
]