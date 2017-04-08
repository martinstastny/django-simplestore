from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<slug>[-\w\d]+)/$', views.ProductDetailView.as_view(), name='detail'),
    url(r'^$', views.ProductsListView.as_view(), name='index')
]
