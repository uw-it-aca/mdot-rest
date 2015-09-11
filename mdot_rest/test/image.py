from django.test import TestCase
from django.core.files import File
from mdot_rest.models import *
from PIL import Image
import os
import random

ALPHA = "abcdefghijklmnopqrstuvwxyz "
TESTROOT = os.path.abspath(os.path.dirname(__file__))


class ImageTest(TestCase):
    """ Tests image functions.
    """
    def setUp(self):
        # create a UWResource with a JPEG
        self.uwr1 = UWResource.objects.create(
            title="".join(random.choice(ALPHA) for i in range(10)),
            feature_desc="".join(random.choice(ALPHA) for i in range(50)),
        )

    def test_convert_to_png(self):
        """ Tests that a non-PNG image is converted to PNG upon save.
        """
        # save a JPEG as the image
        fhandle = open("{0}/files/campusmap.jpg".format(TESTROOT))
        self.uwr1.image = File(fhandle)
        self.uwr1.save()
        fhandle.close()

        # assert that image type is now PNG
        img = Image.open(self.uwr1.image)
        self.assertEqual('PNG', img.format)

    def tearDown(self):
        # destroy the UWResource
        self.uwr1.delete()
