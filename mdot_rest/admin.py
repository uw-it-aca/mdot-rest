from django.conf import settings
from django.contrib import admin
from .models import *

from uw_saml.utils import is_member_of_group


admin_group = settings.ADMIN_AUTHZ_GROUP


class SAMLAdminSite(admin.AdminSite):
    def has_permission(self, request):
        if is_member_of_group(request, admin_group) and request.user.is_active:
            request.user.is_staff = True
            request.user.is_superuser = True
            request.user.save()
            return True
        return False

    def __init__(self, *args, **kwargs):
        super(SAMLAdminSite, self).__init__(*args, **kwargs)
        self._registry.update(admin.site._registry)


admin_site = SAMLAdminSite(name="SAMLAdmin")


@admin.register(IntendedAudience, site=admin_site)
class IntendedAudienceAdmin(admin.ModelAdmin):
    pass


class IntendedAudienceInline(admin.TabularInline):
    model = IntendedAudience.resource.through
    extra = 0


@admin.register(ResourceLink, site=admin_site)
class ResourceLinkAdmin(admin.ModelAdmin):
    model = ResourceLink


class ResourceLinkInLine(admin.TabularInline):
    model = ResourceLink
    extra = 0
    max_num = 4


@admin.register(UWResource, site=admin_site)
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
