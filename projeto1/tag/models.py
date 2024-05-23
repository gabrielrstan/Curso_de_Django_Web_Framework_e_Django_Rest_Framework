from random import SystemRandom
from string import ascii_letters, digits

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    # Here the fields for the generic relationship begin

    # Represents the model we want to fit here
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # Represents the line id of the model described above
    object_id = models.CharField(max_length=255)
    # A field that represents the generic relationship that knows the above
    # fields (content_type and object_id)
    content_object = GenericForeignKey('content_type', 'object_id')

    def save(self, *args, **kwargs):
        if not self.slug:
            rand_letters = ''.join(
                SystemRandom().choices(ascii_letters + digits, k=5))

            self.slug = slugify(f'{self.name}-{rand_letters}')

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
