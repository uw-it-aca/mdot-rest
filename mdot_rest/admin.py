from django.contrib import admin
from .models import *


@admin.register(IntendedAudience)
class IntendedAudienceAdmin(admin.ModelAdmin):
    pass


class IntendedAudienceInline(admin.TabularInline):
    model = IntendedAudience.resource.through
    extra = 0


@admin.register(ResourceLink)
class ResourceLinkAdmin(admin.ModelAdmin):
    model = ResourceLink


class ResourceLinkInLine(admin.TabularInline):
    model = ResourceLink
    extra = 0
    max_num = 4


@admin.register(UWResource)
class UWResourceAdmin(admin.ModelAdmin):
    inlines = [ResourceLinkInLine, IntendedAudienceInline]
