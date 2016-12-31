
from django.conf.urls import url
from django.contrib import admin
from app.views import IndexView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index_view"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
