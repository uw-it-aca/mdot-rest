from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework import status
import models as resource_models
import json
import datetime
from mock import patch


class ResourceTests(TestCase):
    def setUp(self):
        self.default_date = datetime.datetime(1945, 11, 03, 12, 03, 34)
        with patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = self.default_date

            self.resource1 = resource_models.Resource.objects.create(title='ITConnect', feature_desc='This is a test.', featured=True, accessible=True, responsive_web=True, campus_seattle=True, campus_tacoma=False, campus_bothell=False)
            self.intended_audience1 = resource_models.IntendedAudience.objects.create(audience='Students')
            self.intended_audience1.save()
            self.intended_audience1.resource.add(self.resource1)
            self.resource_link1 = resource_models.ResourceLink.objects.create(link_type='IOS', resource=self.resource1, url='uw.edu/itconnect')
            self.resource1.save()
            self.intended_audience1.save()
            self.resource_link1.save()

        self.client = Client()

    def test_simple_resource(self):
        """
        Get the first resource in the database.
        """
        response = self.client.get('/api/v1/resources/1/', format='json')
        expected_response = {
            u'accessible': True,
            u'campus_bothell': False,
            u'campus_seattle': True,
            u'campus_tacoma': False,
            u'created_date': u'1945-11-03T12:03:34Z',
            u'feature_desc': u'This is a test.',
            u'featured': True,
            u'id': 1,
            u'intended_audiences': [{u'audience': u'Students'}],
            u'last_modified': u'1945-11-03T12:03:34Z',
            u'resource_links': [{u'link_type': u'IOS', u'url': u'uw.edu/itconnect'}],
            u'responsive_web': True,
            u'title': u'ITConnect'}

        self.assertEqual(json.loads(response.content), expected_response)

    def test_get_accessible_resource(self):
        """
        Get resources that are accessible.
        """
        response = self.client.get('/api/v1/resources/?accessible=True', format='json')
        expected_response = [{
            u'accessible': True,
            u'campus_bothell': False,
            u'campus_seattle': True,
            u'campus_tacoma': False,
            u'created_date': u'1945-11-03T12:03:34Z',
            u'feature_desc': u'This is a test.',
            u'featured': True,
            u'id': 1,
            u'intended_audiences': [{u'audience': u'Students'}],
            u'last_modified': u'1945-11-03T12:03:34Z',
            u'resource_links': [{u'link_type': u'IOS', u'url': u'uw.edu/itconnect'}],
            u'responsive_web': True,
            u'title': u'ITConnect'}]

        self.assertEqual(json.loads(response.content), expected_response)

    def tearDown(self):
        """
        Destroys all the objects that were made for each test.
        """
        self.resource1.delete()
        self.intended_audience1.delete()
        self.resource_link1.delete()
