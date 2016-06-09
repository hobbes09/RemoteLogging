from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = [
    url(r'^sessions/$', views.SessionList.as_view()),
    url(r'^sessions/(?P<pk>[\w\-]+)/$', views.SessionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

