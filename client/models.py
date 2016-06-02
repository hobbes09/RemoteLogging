from django.db import models
import uuid
import string
import random
from django.template.defaultfilters import slugify

# Create your models here.

class Client(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=False, help_text='This field is autofilled while saving.')
    company_name = models.CharField(max_length=100, blank=False)
    app_name = models.CharField(max_length=100, blank=False)
    package_name = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.app_name) + '-' + id_generator()
        super(Client, self).save(*args, **kwargs)



def id_generator(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
