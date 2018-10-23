from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

from general.views import custom404View

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include(('general.urls', 'general'), namespace='general')),
	path('login/', include(('login.urls', 'login'), namespace='login')),
	path('articles/', include(('articles.urls', 'articles'), namespace='articles')),
	path('shop/', include(('shop.urls', 'shop'), namespace='shop')),
	path('', include('pwa.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
	re_path(r'(?P<path>.*)', custom404View, name='custom404')
]
