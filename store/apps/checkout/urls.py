from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.CheckoutView.as_view(), name='index'),
]
