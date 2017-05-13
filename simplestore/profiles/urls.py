from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/', views.RegistrationFormView.as_view(), name='register'),
    url(r'^orders/$', views.ProfileOrdersView.as_view(), name='orders'),
    url(r'^orders/(?P<pk>\d+)/$', views.ProfileOrderDetailView.as_view(), name='order_detail'),
    url(r'^login/', views.AuthenticationForm.as_view(), name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^profile/$', views.ProfileDetail.as_view(), name='detail'),
    url(r'^profile/update/$', views.UpdateProfileForm.as_view(), name='update'),
]
