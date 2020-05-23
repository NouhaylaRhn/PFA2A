from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "personal"


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student/$', views.studentHome, name='studentHome'),
    url(r'^register/$', views.register, name='Register'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^fiches/$', views.ficheList, name='ficheList'),
    url(r'^fiches/upload/$', views.uploadFiche, name='uploadFiche'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
