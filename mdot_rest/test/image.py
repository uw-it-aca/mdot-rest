from django.test import TestCase
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from mdot_rest.models import *
from PIL import Image
import os
import random

ALPHA = "abcdefghijklmnopqrstuvwxyz "
TESTROOT = os.path.abspath(os.path.dirname(__file__))
#import pdb; pdb.set_trace()

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
        dest = "{0}uploads/test.jpg".format(settings.MEDIA_ROOT)
        self.uwr1.image = SimpleUploadedFile(dest, fhandle.read())
        self.uwr1.save()
        fhandle.close()

        # assert that image type is now PNG
        img = Image.open(self.uwr1.image)
        self.assertEqual('PNG', img.format)
        # and it has a .png extension
        (basename, ext) = os.path.splitext(self.uwr1.image.name)
        self.assertEqual('.png', ext)

    def test_resize_img(self):
        """ Tests that a image is properly resized to 350 by 350px
        """
        # save a large landscape/portrait/square JPEG as the image
        fhandle = open("{0}/files/large.png".format(TESTROOT))
        dest = "{0}uploads/test.jpg".format(settings.MEDIA_ROOT)
        self.uwr1.image = SimpleUploadedFile(dest, fhandle.read())
        self.uwr1.save()
        fhandle.close()
        # assert that landscape image size is now 350 by 350px
        img = Image.open(self.uwr1.image)
        self.assertEqual(img.size, (350, 350))

        # save a medium landscape/portrait JPEG as the image
        fhandle = open("{0}/files/medium.png".format(TESTROOT))
        dest = "{0}uploads/test.jpg".format(settings.MEDIA_ROOT)
        origImg = Image.open("{0}/files/medium.png".format(TESTROOT))
        self.uwr1.image = SimpleUploadedFile(dest, fhandle.read())
        self.uwr1.save()
        fhandle.close()
        # assert that both sizes of image are equal to the smaller size
        # of the original img
        img = Image.open(self.uwr1.image)
        self.assertEqual(img.size, (min(origImg.size[0], origImg.size[1]), min(origImg.size[0], origImg.size[1])))

        # save a small landscape/portrait/square JPEG as the image
        fhandle = open("{0}/files/small.png".format(TESTROOT))
        dest = "{0}uploads/test.jpg".format(settings.MEDIA_ROOT)
        origImg = Image.open("{0}/files/small.png".format(TESTROOT))
        self.uwr1.image = SimpleUploadedFile(dest, fhandle.read())
        self.uwr1.save()
        fhandle.close()
        # assert that both sizes of image are equal to the smaller size
        # of the original img
        img = Image.open(self.uwr1.image)
        self.assertEqual(img.size, (min(origImg.size[0], origImg.size[1]), min(origImg.size[0], origImg.size[1])))
        pass

    def tearDown(self):
        # destroy the UWResource
        self.uwr1.delete()
