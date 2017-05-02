from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profiles/', include('store.profiles.urls', namespace='profiles')),
    url(r'^cart/', include('store.cart.urls', namespace='cart')),
    url(r'^checkout/', include('store.checkout.urls', namespace='checkout')),
    url(r'^', include('store.products.urls', namespace='products')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
