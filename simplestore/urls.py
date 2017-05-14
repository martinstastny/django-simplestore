from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^api/v1/', include('simplestore.api.urls', namespace='api')),
    url(r'^profiles/', include('simplestore.profiles.urls', namespace='profiles')),
    url(r'^cart/', include('simplestore.cart.urls', namespace='cart')),
    url(r'^checkout/', include('simplestore.checkout.urls', namespace='checkout')),
    url(r'^', include('simplestore.products.urls', namespace='products')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
