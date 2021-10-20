# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

import django_filters as filters
from .models import UWResource, IntendedAudience
from .serializers import UWResourceSerializer
from rest_framework import generics, permissions


class UWResourceFilter(filters.FilterSet):
    audience = filters.CharFilter(field_name='intended_audiences__audience')

    class Meta:
        model = UWResource
        fields = (
            'title',
            'featured',
            'accessible',
            'responsive_web',
            'audience',
            'campus_bothell',
            'campus_seattle',
            'campus_tacoma',
        )


class UWResourceList(generics.ListCreateAPIView):
    queryset = UWResource.objects.filter(published=True)
    serializer_class = UWResourceSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    filter_class = UWResourceFilter


class UWResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UWResource.objects.filter(published=True)
    serializer_class = UWResourceSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
