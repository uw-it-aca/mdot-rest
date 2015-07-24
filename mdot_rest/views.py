from django.shortcuts import render
from .models import Resource
from .serializers import ResourceSerializer
from rest_framework import generics, permissions
import django_filters


class ResourceFilter(django_filters.FilterSet):
    class Meta:
        model = Resource
        fields = ('name', 'featured', 'accessible', 'responsive_web',)


class ResourceList(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_class = ResourceFilter


class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
