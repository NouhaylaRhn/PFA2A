from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Fiche_de_condidature

urlpatterns = [ 
                url(r'^$', ListView.as_view(
                                    queryset=Fiche_de_condidature.objects.all().order_by("-date")[:25],
                                    template_name="blog/blog.html")),
                 url(r'^(?P<pk>\d+)$', DetailView.as_view(
                                    model = Fiche_de_condidature,
                                    template_name="blog/post.html")),
            ]
