import django_filters as filters
from .models import Resource, IntendedAudience
from .serializers import ResourceSerializer
from rest_framework import generics, permissions


class ResourceFilter(filters.FilterSet):
    audience = filters.CharFilter(name='intendedaudience__audience')

    class Meta:
        model = Resource
        fields = ('title', 'featured', 'accessible', 'responsive_web', 'audience',)


class ResourceList(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_class = ResourceFilter


class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
