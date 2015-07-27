from .models import Resource, ResourceLink, IntendedAudience
from rest_framework import serializers


class ResourceLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceLink
        fields = ('link_type', 'url',)


class IntendedAudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntendedAudience
        fields = ('audience',)


class ResourceSerializer(serializers.ModelSerializer):
    resource_links = ResourceLinkSerializer(many=True, read_only=True)
    intended_audiences = IntendedAudienceSerializer(many=True, read_only=True)

    class Meta:
        model = Resource
        fields = (
            'id',
            'title',
            'feature_desc',
            'featured',
            'accessible',
            'responsive_web',
            'resource_links',
            'intended_audiences',
            'campus_bothell',
            'campus_tacoma',
            'campus_seattle',
            'created_date',
            'last_modified',
        )
