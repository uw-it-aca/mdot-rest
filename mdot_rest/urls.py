from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^resources/$', views.UWResourceList.as_view()),
    url(r'^resources/(?P<pk>[0-9]+)/$', views.UWResourceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
