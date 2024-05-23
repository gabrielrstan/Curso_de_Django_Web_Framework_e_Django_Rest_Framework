from random import SystemRandom
from string import ascii_letters, digits

from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            rand_letters = ''.join(
                SystemRandom().choices(ascii_letters + digits, k=5))

            self.slug = slugify(f'{self.name}-{rand_letters}')

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
