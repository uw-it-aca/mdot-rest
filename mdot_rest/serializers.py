from .models import Resource, ResourceLink
from rest_framework import serializers


class ResourceLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceLink
        fields = ('link_type', 'title', 'url')


class ResourceSerializer(serializers.ModelSerializer):
    resourcelink_set = ResourceLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Resource
        fields = ('id', 'name', 'feature_desc', 'featured', 'accessible', 'responsive_web', 'resourcelink_set', 'created_date', 'last_modified')
