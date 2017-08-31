from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CheckoutOrderCreateView.as_view(), name='index'),
    url(r'confirmation/(?P<slug>[\w\d\-]+)/$',
        views.OrderConfirmationView.as_view(),
        name='order-confirmation'
    )
]