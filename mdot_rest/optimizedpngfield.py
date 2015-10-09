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
            img = Image.open(content)
            w, h = img.size
            resizeFactor = 1
            if (min(w, h) > 350):
                resizeFactor = min(w/350, h/350)
            img = img.resize((w/resizeFactor, h/resizeFactor), Image.ANTIALIAS)
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
