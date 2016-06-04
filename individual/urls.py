from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = [
    url(r'^individuals/$', views.IndividualList.as_view()),
    url(r'^individuals/(?P<ext_id>[\w\-]+)/$', views.IndividualDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

