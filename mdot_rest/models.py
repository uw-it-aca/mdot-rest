from django.db import models

class ResourceLink(models.Model):
    """ Represents metadata about a resource we want to direct users to.
    """
    name = models.CharField(max_length=30)
    # app_type = ?? related model?
    short_desc = models.CharField(max_length=200) # can this be blank?
    feature_desc = models.TextField()
    # image = models.ImageField(upload_to=WHERE) # icon, instead? where to upload to?
    # screenshots = related model??
    # bundle = ?? # should this be a related model? tags?
    web_url = models.URLField(blank=True)
    iTunes_url = models.URLField(blank=True)
    Google_Play_url = models.URLField(blank=True)
    Windows_Store_url = models.URLField(blank=True)
    # role_focus = ?? should this be a related model?
    # school_focus = ?? related model?
    # major_focus = ?? related model?
    # class_standing_focus = ?? related model?
    support_url = models.URLField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
