from .models import UWResource, ResourceLink, IntendedAudience
from rest_framework import serializers


class ResourceLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceLink
        fields = ('link_type', 'url',)


class IntendedAudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntendedAudience
        fields = ('audience',)


class UWResourceSerializer(serializers.ModelSerializer):
    resource_links = ResourceLinkSerializer(many=True, read_only=True)
    intended_audiences = IntendedAudienceSerializer(many=True, read_only=True)

    class Meta:
        model = UWResource
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
