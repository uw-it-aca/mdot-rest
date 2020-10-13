from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('uwresources/', views.UWResourceList.as_view()),
    path('uwresources/<int:pk>/', views.UWResourceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
