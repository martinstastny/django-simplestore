from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', views.profile_index, name='index'),
    url(r'^register/', views.RegistrationForm.as_view(), name='register'),
    url(r'^(?P<pk>\d+)/update/$', views.UpdateProfileForm.as_view(), name='update'),
    url(r'^login/', views.AuthenticationForm.as_view(), name='login'),
    url(r'^logout/', views.logout_view , name='logout'),
    # url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^(?P<pk>\d+)/$', login_required(views.ProfileDetail.as_view()), name='detail'),
]
