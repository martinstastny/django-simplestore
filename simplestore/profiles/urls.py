from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.UpdateProfileForm.as_view(), name='index'),
    url(r'^register/', views.RegistrationFormView.as_view(), name='register'),
    url(r'^login/', views.AuthenticationForm.as_view(), name='login'),
    url(r'^orders/$', views.ProfileOrdersView.as_view(), name='orders'),
    url(r'^orders/(?P<pk>\d+)/$', views.ProfileOrderDetailView.as_view(), name='order_detail'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^(?P<pk>\d+)/$', login_required(views.ProfileDetail.as_view()), name='detail'),
]
