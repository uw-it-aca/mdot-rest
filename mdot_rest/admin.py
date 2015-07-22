from django.contrib import admin
from .models import *


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    pass


@admin.register(IntendedAudience)
class IntendedAudienceAdmin(admin.ModelAdmin):
    pass


@admin.register(ResourceLink)
class ResourceLinkAdmin(admin.ModelAdmin):
    pass
