from django.conf.urls import url
from . import views

urlpatterns = [
    url('^products/$', views.ProductListView.as_view(), name='products'),
    url('^cart/$', views.CartDetailView.as_view(), name='cart'),
    url(r'^cart/update/(?P<id>[0-9]+)/$', views.CartUpdateView.as_view(), name='update'),
]
