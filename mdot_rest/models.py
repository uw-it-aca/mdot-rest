from django.db import models


class Resource(models.Model):
    """ Represents metadata about a resource we want to direct users to.
    """
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)
    feature_desc = models.CharField(max_length=120)
    featured = models.BooleanField(default=False)
    accessible = models.BooleanField(default=False)
    responsive_web = models.BooleanField(default=False)
    campus_seattle = models.BooleanField(default=False)
    campus_tacoma = models.BooleanField(default=False)
    campus_bothell = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class IntendedAudience(models.Model):
    """ Represents audiences we want to advertise the resource to. Examples
        include affiliation (student, staff, faculty) or class standing
        (freshman, sophomore, etc.)
    """
    resource = models.ManyToManyField('Resource')
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)

    def __unicode__(self):
        return self.name

    class Meta:
        default_related_name = 'intended_audiences'


class ResourceLink(models.Model):
    """ Represents a link to launch the resource, based on what sort of
        device the link is displayed on.
    """
    ANDROID = 'AND'
    IOS = 'IOS'
    WEB = 'WEB'
    WINDOWS_PHONE = 'WIP'
    LINK_TYPE_CHOICES = (
        (ANDROID, 'Android'),
        (IOS, 'iOS'),
        (WEB, 'Web'),
        (WINDOWS_PHONE, 'Windows Phone'),
    )
    link_type = models.CharField(max_length=3, choices=LINK_TYPE_CHOICES)
    resource = models.ForeignKey('Resource')
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)
    url = models.URLField()

    def __unicode__(self):
        return "{0}: {1}".format(self.resource, self.link_type)

    class Meta:
        default_related_name = 'resource_links'
