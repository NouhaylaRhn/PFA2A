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
    url(r'^recus/$', views.RecuList, name='RecuList'),
    url(r'^cartes/$', views.CarteList, name='CarteList'),
    url(r'^uploadfiche/$', views.uploadFiche, name='uploadFiche'),
    url(r'^uprecu/$', views.uploadRecu, name='uploadRecu'),
    url(r'^upcarte/$', views.uploadCarte, name='uploadCarte'),
    url(r'^logout/$', views.logout_request, name="logout"),
    url(r'^login/$', views.login_request, name="login_request"),
    url(r'^loginadmin/$', views.login_admin, name="login_admin"),
    url(r'^homee/$', views.panda, name="panda"),
    url(r'^homeerecu/$', views.pandarecu, name="pandarecu"),
    url(r'^homeecarte/$', views.pandacarte, name="pandacarte"),
    url(r'^export/$', views.export_excel, name="export_excel"),
    url(r'^exportrecu/$', views.export_recu, name="export_recu"),
    url(r'^exportcarte/$', views.export_carte, name="export_carte"),
    url(r'^adminprofile/$', views.adminprofile, name="adminprofile"),
    url(r'^tipe/$', views.tipe, name="tipe"),
    url(r'^resultat/$', views.resultat, name="resultat"),
    url(r'^recus/(?P<id>\d+)/$', views.delete_recus, name='delete_recus'),
    
    


    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
