from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework import status
import mdot_rest.models as resource_models
import json
import datetime
from mock import patch


class ResourceTest(TestCase):

    def setUp(self):
        self.default_date = datetime.datetime(1945, 11, 3, 12, 3, 34)
        with patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = self.default_date

            self.resource1 = resource_models.UWResource.objects.create(
                title='ITConnect',
                feature_desc='This is a test.',
                featured=True,
                accessible=True,
                responsive_web=True,
                campus_seattle=True,
                campus_tacoma=False,
                campus_bothell=False,
                published=True)
            self.resource2 = resource_models.UWResource.objects.create(
                title='SpaceScout',
                feature_desc='This is another test.',
                featured=True,
                accessible=False,
                responsive_web=True,
                campus_seattle=True,
                campus_tacoma=True,
                campus_bothell=True,
                published=True)
            self.resource3 = resource_models.UWResource.objects.create(
                title='Unpublished',
                feature_desc='This is a resource that is not published.',
                featured=True,
                accessible=False,
                responsive_web=True,
                campus_seattle=True,
                campus_tacoma=True,
                campus_bothell=True,
                published=False)

            self.intended_audience1 = \
                resource_models.IntendedAudience.objects.create(
                    audience='Students')
            self.intended_audience2 = \
                resource_models.IntendedAudience.objects.create(
                    audience='Developers')

            self.intended_audience1.save()
            self.intended_audience2.save()

            self.intended_audience1.resource.add(self.resource1)
            self.intended_audience1.resource.add(self.resource2)
            self.intended_audience2.resource.add(self.resource2)
            self.intended_audience2.resource.add(self.resource3)

            self.resource_link1 = resource_models.ResourceLink.objects.create(
                link_type='IOS',
                resource=self.resource1,
                url='uw.edu/itconnect')
            self.resource_link2 = resource_models.ResourceLink.objects.create(
                link_type='WEB',
                resource=self.resource2,
                url='spacescout.uw.edu')
            self.resource_link3 = resource_models.ResourceLink.objects.create(
                link_type='IOS',
                resource=self.resource2,
                url='spacescout.ue.edu/ios')
            self.resource_link4 = resource_models.ResourceLink.objects.create(
                link_type='WEB',
                resource=self.resource3,
                url='washington.edu/notathing')

            self.resource1.save()
            self.resource2.save()
            self.resource3.save()

            self.intended_audience1.save()
            self.intended_audience2.save()

            self.resource_link1.save()
            self.resource_link2.save()
            self.resource_link3.save()
            self.resource_link4.save()

        self.client = Client()

    def test_resource_str(self):
        """
        Test that the __str__ method returns the resource name.
        Python 2 should still use unicode. Python 3 only uses str
        """
        self.assertEqual(self.resource1.__str__(), 'ITConnect')

    def test_intendedaudience_str(self):
        """
        Test that the __str__ method returns the audience name.
        """
        self.assertEqual(self.intended_audience1.__str__(), 'Students')

    def test_resource_linke_str(self):
        """
        Test that the __str__ method returns the resource link name.
        """
        self.assertEqual(self.resource_link1.__str__(), 'ITConnect: IOS')

    def test_simple_resource(self):
        """
        Get the first resource in the database.
        """
        path = "/api/v1/uwresources/{0}/".format(self.resource1.pk)
        response = self.client.get(path, format='json')
        expected_response = {u'accessible': True,
                             u'campus_bothell': False,
                             u'campus_seattle': True,
                             u'campus_tacoma': False,
                             u'created_date': u'1945-11-03T12:03:34-08:00',
                             u'feature_desc': u'This is a test.',
                             u'featured': True,
                             u'id': self.resource1.pk,
                             u'image': None,
                             u'intended_audiences': [{u'audience':
                                                      u'Students'}],
                             u'last_modified': u'1945-11-03T12:03:34-08:00',
                             u'resource_links': [{u'link_type': u'IOS',
                                                  u'url':
                                                  u'uw.edu/itconnect'}],
                             u'responsive_web': True,
                             u'title': u'ITConnect'
                             }

        self.assertTrue(json.loads(response.content) == expected_response)
        self.assertTrue(json.loads(response.content).__len__(),
                        expected_response.__len__())

    def test_get_published_resources(self):
        """
        Request all resources, but check that we only get published ones.
        """
        response = self.client.get('/api/v1/uwresources/')
        expected_response = [{u'accessible': True,
                              u'feature_desc': u'This is a test.',
                              u'title': u'ITConnect',
                              u'image': None,
                              u'created_date': u'1945-11-03T12:03:34-08:00',
                              u'campus_seattle': True,
                              u'campus_bothell': False,
                              u'responsive_web': True,
                              u'featured': True,
                              u'last_modified': u'1945-11-03T12:03:34-08:00',
                              u'intended_audiences': [{u'audience':
                                                       u'Students'}],
                              u'resource_links': [{u'url': u'uw.edu/itconnect',
                                                   u'link_type': u'IOS'}],
                              u'id': 1,
                              u'campus_tacoma': False
                              },
                             {u'accessible': False,
                              u'feature_desc': u'This is another test.',
                              u'title': u'SpaceScout',
                              u'image': None,
                              u'created_date': u'1945-11-03T12:03:34-08:00',
                              u'campus_seattle': True,
                              u'campus_bothell': True,
                              u'responsive_web': True,
                              u'featured': True,
                              u'last_modified': u'1945-11-03T12:03:34-08:00',
                              u'intended_audiences': [{u'audience':
                                                       u'Students'},
                                                      {u'audience':
                                                       u'Developers'}],
                              u'resource_links': [{u'url':
                                                   u'spacescout.uw.edu',
                                                   u'link_type': u'WEB'},
                                                  {u'url':
                                                   u'spacescout.ue.edu/ios',
                                                   u'link_type': u'IOS'}],
                              u'id': 2,
                              u'campus_tacoma': True
                              }]

        self.assertTrue(sorted(json.loads(response.content),
                        key=lambda i: i['id']) ==
                        sorted(expected_response, key=lambda i: i['id']))
        self.assertTrue(json.loads(response.content).__len__(),
                        expected_response.__len__())

    def test_get_accessible_resource(self):
        """
        Get resources that are accessible.
        """
        response = self.client.get('/api/v1/uwresources/?accessible=True',
                                   format='json')
        expected_response = [{u'accessible': True,
                              u'campus_bothell': False,
                              u'campus_seattle': True,
                              u'campus_tacoma': False,
                              u'created_date': u'1945-11-03T12:03:34-08:00',
                              u'feature_desc': u'This is a test.',
                              u'featured': True,
                              u'id': 1,
                              u'image': None,
                              u'intended_audiences': [{u'audience':
                                                       u'Students'}],
                              u'last_modified': u'1945-11-03T12:03:34-08:00',
                              u'resource_links': [{u'link_type': u'IOS',
                                                   u'url':
                                                   u'uw.edu/itconnect'}],
                              u'responsive_web': True,
                              u'title': u'ITConnect'
                              }]

        self.assertTrue(sorted(json.loads(response.content),
                               key=lambda i: i['id']) ==
                        sorted(expected_response, key=lambda i: i['id']))
        self.assertTrue(json.loads(response.content).__len__(),
                        expected_response.__len__())

    def test_get_responsive_resources(self):
        """
        Get resources that are responsive.
        """
        response = self.client.get('/api/v1/uwresources/?responsive_web=True')
        expected_response = [{u'accessible': True,
                              u'feature_desc': u'This is a test.',
                              u'title': u'ITConnect',
                              u'image': None,
                              u'created_date': u'1945-11-03T12:03:34-08:00',
                              u'campus_seattle': True,
                              u'campus_bothell': False,
                              u'responsive_web': True,
                              u'featured': True,
                              u'last_modified': u'1945-11-03T12:03:34-08:00',
                              u'intended_audiences': [{u'audience':
                                                       u'Students'}],
                              u'resource_links': [{u'url': u'uw.edu/itconnect',
                                                   u'link_type': u'IOS'}],
                              u'id': 1,
                              u'campus_tacoma': False
                              },
                             {u'accessible': False,
                              u'feature_desc': u'This is another test.',
                              u'title': u'SpaceScout',
                              u'image': None,
                              u'created_date': u'1945-11-03T12:03:34-08:00',
                              u'campus_seattle': True,
                              u'campus_bothell': True,
                              u'responsive_web': True,
                              u'featured': True,
                              u'last_modified': u'1945-11-03T12:03:34-08:00',
                              u'intended_audiences': [{u'audience':
                                                       u'Students'},
                                                      {u'audience':
                                                       u'Developers'}],
                              u'resource_links': [{u'url':
                                                   u'spacescout.uw.edu',
                                                   u'link_type': u'WEB'},
                                                  {u'url':
                                                   u'spacescout.ue.edu/ios',
                                                   u'link_type': u'IOS'}],
                              u'id': 2,
                              u'campus_tacoma': True
                              }]

        self.assertTrue(sorted(json.loads(response.content),
                               key=lambda i: i['id']) ==
                        sorted(expected_response, key=lambda i: i['id']))
        self.assertTrue(json.loads(response.content).__len__(),
                        expected_response.__len__())

    def test_get_seattle_resource(self):
        """
        Get all the resources that are for seattle campus.
        """
        response = self.client.get('/api/v1/uwresources/?campus_seattle=True')
        expected_response = [{u'accessible': True,
                              u'feature_desc': u'This is a test.',
                              u'title': u'ITConnect',
                              u'image': None,
                              u'created_date': u'1945-11-03T12:03:34-08:00',
                              u'campus_seattle': True,
                              u'campus_bothell': False,
                              u'responsive_web': True,
                              u'featured': True,
                              u'last_modified': u'1945-11-03T12:03:34-08:00',
                              u'intended_audiences': [{u'audience':
                                                       u'Students'}],
                              u'resource_links': [{u'url': u'uw.edu/itconnect',
                                                   u'link_type': u'IOS'}],
                              u'id': 1,
                              u'campus_tacoma': False
                              },
                             {u'accessible': False,
                              u'feature_desc': u'This is another test.',
                              u'title': u'SpaceScout',
                              u'image': None,
                              u'created_date': u'1945-11-03T12:03:34-08:00',
                              u'campus_seattle': True,
                              u'campus_bothell': True,
                              u'responsive_web': True,
                              u'featured': True,
                              u'last_modified': u'1945-11-03T12:03:34-08:00',
                              u'intended_audiences': [{u'audience':
                                                       u'Students'},
                                                      {u'audience':
                                                       u'Developers'}],
                              u'resource_links': [{u'url':
                                                   u'spacescout.uw.edu',
                                                   u'link_type': u'WEB'},
                                                  {u'url':
                                                   u'spacescout.ue.edu/ios',
                                                   u'link_type': u'IOS'}],
                              u'id': 2,
                              u'campus_tacoma': True
                              }]

        self.assertTrue(sorted(json.loads(response.content),
                               key=lambda i: i['id']) ==
                        sorted(expected_response, key=lambda i: i['id']))
        self.assertTrue(json.loads(response.content).__len__(),
                        expected_response.__len__())

    def test_get_featured_resource(self):
        """
        Get all the resources that are flagged as featured.
        """
        response = self.client.get('/api/v1/uwresources/?featured=True')
        expected_response = [{u'accessible': True,
                              u'feature_desc': u'This is a test.',
                              u'title': u'ITConnect',
                              u'image': None,
                              u'created_date': u'1945-11-03T12:03:34-08:00',
                              u'campus_seattle': True,
                              u'campus_bothell': False,
                              u'responsive_web': True,
                              u'featured': True,
                              u'last_modified': u'1945-11-03T12:03:34-08:00',
                              u'intended_audiences': [{u'audience':
                                                       u'Students'}],
                              u'resource_links': [{u'url':
                                                   u'uw.edu/itconnect',
                                                   u'link_type':
                                                   u'IOS'}],
                              u'id': 1,
                              u'campus_tacoma': False
                              },
                             {u'accessible': False,
                              u'feature_desc': u'This is another test.',
                              u'title': u'SpaceScout',
                              u'image': None,
                              u'created_date': u'1945-11-03T12:03:34-08:00',
                              u'campus_seattle': True,
                              u'campus_bothell': True,
                              u'responsive_web': True,
                              u'featured': True,
                              u'last_modified': u'1945-11-03T12:03:34-08:00',
                              u'intended_audiences': [{u'audience':
                                                       u'Students'},
                                                      {u'audience':
                                                       u'Developers'}],
                              u'resource_links': [{u'url':
                                                   u'spacescout.uw.edu',
                                                   u'link_type': u'WEB'},
                                                  {u'url':
                                                   u'spacescout.ue.edu/ios',
                                                   u'link_type': u'IOS'}],
                              u'id': 2,
                              u'campus_tacoma': True
                              }]

        self.assertTrue(sorted(json.loads(response.content),
                               key=lambda i: i['id']) ==
                        sorted(expected_response, key=lambda i: i['id']))
        self.assertTrue(json.loads(response.content).__len__(),
                        expected_response.__len__())

    def test_get_resource_by_title(self):
        """
        Get a resource by its title.
        """
        response = self.client.get('/api/v1/uwresources/?title=SpaceScout')
        expected_response = [{u'accessible': False,
                              u'feature_desc': u'This is another test.',
                              u'title': u'SpaceScout',
                              u'image': None,
                              u'created_date': u'1945-11-03T12:03:34-08:00',
                              u'campus_seattle': True,
                              u'campus_bothell': True,
                              u'responsive_web': True,
                              u'featured': True,
                              u'last_modified': u'1945-11-03T12:03:34-08:00',
                              u'intended_audiences': [{u'audience':
                                                       u'Students'},
                                                      {u'audience':
                                                       u'Developers'}],
                              u'resource_links': [{u'url':
                                                   u'spacescout.uw.edu',
                                                   u'link_type': u'WEB'},
                                                  {u'url':
                                                   u'spacescout.ue.edu/ios',
                                                   u'link_type': u'IOS'}],
                              u'id': 2,
                              u'campus_tacoma': True}]

        self.assertTrue(sorted(json.loads(response.content),
                               key=lambda i: i['id']) ==
                        sorted(expected_response, key=lambda i: i['id']))
        self.assertTrue(json.loads(response.content).__len__(),
                        expected_response.__len__())

    def test_get_resource_by_audience(self):
        """
        Get all the resources that are for an audience.
        """
        response = self.client.get('/api/v1/uwresources/?audience=Students')
        expected_response = [{u'accessible': True,
                              u'feature_desc': u'This is a test.',
                              u'title': u'ITConnect',
                              u'image': None,
                              u'created_date': u'1945-11-03T12:03:34-08:00',
                              u'campus_seattle': True,
                              u'campus_bothell': False,
                              u'responsive_web': True,
                              u'featured': True,
                              u'last_modified': u'1945-11-03T12:03:34-08:00',
                              u'intended_audiences': [{u'audience':
                                                       u'Students'}],
                              u'resource_links': [{u'url': u'uw.edu/itconnect',
                                                   u'link_type': u'IOS'}],
                              u'id': 1,
                              u'campus_tacoma': False
                              },
                             {u'accessible': False,
                              u'feature_desc': u'This is another test.',
                              u'title': u'SpaceScout',
                              u'image': None,
                              u'created_date': u'1945-11-03T12:03:34-08:00',
                              u'campus_seattle': True,
                              u'campus_bothell': True,
                              u'responsive_web': True,
                              u'featured': True,
                              u'last_modified': u'1945-11-03T12:03:34-08:00',
                              u'intended_audiences': [{u'audience':
                                                       u'Students'},
                                                      {u'audience':
                                                       u'Developers'}],
                              u'resource_links': [{u'url':
                                                   u'spacescout.uw.edu',
                                                   u'link_type': u'WEB'},
                                                  {u'url':
                                                   u'spacescout.ue.edu/ios',
                                                   u'link_type': u'IOS'}],
                              u'id': 2,
                              u'campus_tacoma': True
                              }]

        self.assertTrue(sorted(json.loads(response.content),
                               key=lambda i: i['id']) ==
                        sorted(expected_response, key=lambda i: i['id']))
        self.assertTrue(json.loads(response.content).__len__(),
                        expected_response.__len__())

    def test_complex_filter(self):
        """
        Get all the resources that satisfy a complex filter.
        """
        response = self.client.get(
            '/api/v1/uwresources/?accessible=True&campus_seattle=True&\
            responsive_web=True&featured=True&audience=Students')

        expected_response = [{u'accessible': True,
                              u'feature_desc': u'This is a test.',
                              u'title': u'ITConnect',
                              u'image': None,
                              u'created_date': u'1945-11-03T12:03:34-08:00',
                              u'campus_seattle': True,
                              u'campus_bothell': False,
                              u'responsive_web': True,
                              u'featured': True,
                              u'last_modified': u'1945-11-03T12:03:34-08:00',
                              u'intended_audiences': [{u'audience':
                                                       u'Students'}],
                              u'resource_links': [{u'url': u'uw.edu/itconnect',
                                                   u'link_type': u'IOS'}],
                              u'id': 1,
                              u'campus_tacoma': False
                              }]

        self.assertTrue(sorted(json.loads(response.content)) ==
                        sorted(expected_response))
        self.assertTrue(json.loads(response.content).__len__(),
                        expected_response.__len__())

    def test_put_to_api(self):
        """
        The rest API is readonly, so an attempt at a put should return a
        forbidden status code.
        """
        new_resource = {u'accessible': True,
                        u'feature_desc': u'This is a test.',
                        u'title': u'ITConnect',
                        u'created_date': u'1945-11-03T12:03:34-08:00',
                        u'campus_seattle': True,
                        u'campus_bothell': False,
                        u'responsive_web': True,
                        u'featured': True,
                        u'last_modified': u'1945-11-03T12:03:34-08:00',
                        u'intended_audiences': [{u'audience': u'Students'}],
                        u'resource_links': [{u'url': u'uw.edu/itconnect',
                                             u'link_type': u'IOS'}],
                        u'id': 1,
                        u'campus_tacoma': False
                        }

        response = self.client.put('/api/v1/uwresources/', new_resource)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_to_api(self):
        """
        The rest API is readonly, so an attempt at a post should return a
        forbidden status code.
        """
        new_resource = {u'accessible': True,
                        u'feature_desc': u'This is a test.',
                        u'title': u'ITConnect',
                        u'created_date': u'1945-11-03T12:03:34-08:00',
                        u'campus_seattle': True,
                        u'campus_bothell': False,
                        u'responsive_web': True,
                        u'featured': True,
                        u'last_modified': u'1945-11-03T12:03:34-08:00',
                        u'intended_audiences': [{u'audience': u'Students'}],
                        u'resource_links': [{u'url': u'uw.edu/itconnect',
                                             u'link_type': u'IOS'}],
                        u'id': 1,
                        u'campus_tacoma': False
                        }

        response = self.client.post('/api/v1/uwresources/', new_resource)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_from_api(self):
        """
        The rest API is readonly, so an attempt to delete a resource should
        return a forbidden status code.
        """
        response = self.client.delete('/api/v1/uwresources/?title=ITConnect')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_to_api(self):
        """
        The rest API is readonly, so an attempt to patch a resource should
        return a forbidden status code.
        """
        new_resource = {u'accessible': True,
                        u'feature_desc': u'This is a test.',
                        u'title': u'ITConnect',
                        u'created_date': u'1945-11-03T12:03:34-08:00',
                        u'campus_seattle': True,
                        u'campus_bothell': False,
                        u'responsive_web': True,
                        u'featured': True,
                        u'last_modified': u'1945-11-03T12:03:34-08:00',
                        u'intended_audiences': [{u'audience': u'Students'}],
                        u'resource_links': [{u'url': u'uw.edu/itconnect',
                                             u'link_type': u'IOS'}],
                        u'id': 1,
                        u'campus_tacoma': False
                        }

        response = self.client.patch('/api/v1/uwresources/', new_resource)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def tearDown(self):
        """
        Destroys all the objects that were made for each test.
        """
        self.resource1.delete()
        self.resource2.delete()

        self.intended_audience1.delete()
        self.intended_audience2.delete()

        self.resource_link1.delete()
        self.resource_link2.delete()
        self.resource_link3.delete()
