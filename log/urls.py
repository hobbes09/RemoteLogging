from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = [
    url(r'^logs/$', views.LogList.as_view()),
    url(r'^logs/(?P<pk>[\w\-]+)/$', views.LogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

