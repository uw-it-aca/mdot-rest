# Copyright 2022 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('uwresources/', views.UWResourceList.as_view()),
    path('uwresources/<int:pk>/', views.UWResourceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
