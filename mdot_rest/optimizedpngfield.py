from django.core.files.base import ContentFile
from django.db.models import ImageField
from django.db.models.fields.files import ImageFieldFile
from PIL import Image
import cStringIO


class OptimizedPNGImageFieldFile(ImageFieldFile):
    """ Saves an optimized PNG.
    """
    def save(self, name, content, save=True):
        if content:
            img = Image.open(content)
            buf = cStringIO.StringIO()
            img.save(buf, format='PNG', optimized=True)
            new_content_str = buf.getvalue()
            content = ContentFile(new_content_str)

        return super(OptimizedPNGImageFieldFile, self).save(name, content, save)


class OptimizedPNGImageField(ImageField):
    """ ImageField that converts all images to an optimized PNG on save.
    """
    attr_class = OptimizedPNGImageFieldFile
