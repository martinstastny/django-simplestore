from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^category/(?P<category_slug>[-\w\d]+)/$', views.CategoryDetailView.as_view(), name='category'),
    url(r'^(?P<slug>[-\w\d]+)/$', views.ProductDetailView.as_view(), name='detail'),
    url(r'^$', views.ProductsListView.as_view(), name='index')
]
