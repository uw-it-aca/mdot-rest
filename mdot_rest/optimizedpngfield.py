from django.core.files.base import ContentFile
from django.db.models import ImageField
from django.db.models.fields.files import ImageFieldFile
from PIL import Image
import cStringIO
import os


class OptimizedPNGImageFieldFile(ImageFieldFile):
    """ Saves an optimized PNG.
    """

    def save(self, name, content, save=True):
        if content:
            # convert to optimized PNG
            # the PNG size is 350 * 350px
            img = Image.open(content)
            w, h = img.size
            if w >= h:
                img = img.crop((w/2 - h/2, 0, w/2 + h/2, h))
            else:
                img = img.crop((0, h/2 - w/2, w, h/2 + w/2))
            if img.size[0] > 350:
                img = img.resize((350, 350), Image.ANTIALIAS)

            buf = cStringIO.StringIO()
            img.save(buf, format='PNG', optimized=True)
            new_content_str = buf.getvalue()
            content = ContentFile(new_content_str)

            # make sure it gets a .png extension
            (basename, ext) = os.path.splitext(name)
            name = "{0}{1}".format(basename, '.png')

        return super(OptimizedPNGImageFieldFile, self).save(
            name, content, save)


class OptimizedPNGImageField(ImageField):
    """ ImageField that converts all images to an optimized PNG on save.
    """
    attr_class = OptimizedPNGImageFieldFile
