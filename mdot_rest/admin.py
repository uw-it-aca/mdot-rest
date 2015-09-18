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
    actions = ['make_published', 'make_unpublished']

    def make_published(self, request, queryset):
        rows_updated = queryset.update(published=True)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "{0} stories were".format(rows_updated)
        self.message_user(
            request, "{0} successfully marked as published.".format(
                message_bit))
    make_published.short_description = "Mark selected resources as published"

    def make_unpublished(self, request, queryset):
        rows_updated = queryset.update(published=False)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "{0} stories were".format(rows_updated)
        self.message_user(
            request, "{0} successfully marked as not published.".format(
                message_bit))
    make_unpublished.short_description = \
        "Mark selected resources as not published"
