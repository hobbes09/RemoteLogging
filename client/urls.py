from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = [
    url(r'^clients/$', views.ClientList.as_view()),
    url(r'^clients/(?P<slug>[\w\-]+)/$', views.ClientDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

