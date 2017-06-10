from django.conf.urls import url
from . import views

urlpatterns = [
    url('^products/$', views.ProductListView.as_view(), name='products'),
    url('^cart/$', views.CartDetailView.as_view(), name='cart'),
    url(r'^cart/(?P<id>[0-9]+)/$', views.CartUpdateDeleteView.as_view(), name='update'),
]
