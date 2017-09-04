from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CartView.as_view(), name='index'),
    url(r'^add/(?P<product_id>[0-9]+)/$', views.AddToCartView.as_view(), name='add'),
    url(r'^remove/(?P<product_id>[0-9]+)/$', views.RemoveCartItemView.as_view(), name='remove'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.UpdateCartItemView.as_view(), name='update'),
]
