import django_filters as filters
from .models import UWResource, IntendedAudience
from .serializers import UWResourceSerializer
from rest_framework import generics, permissions


class UWResourceFilter(filters.FilterSet):
    audience = filters.CharFilter(name='intendedaudience__audience')

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
    queryset = UWResource.objects.all()
    serializer_class = UWResourceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_class = UWResourceFilter


class UWResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UWResource.objects.all()
    serializer_class = UWResourceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
