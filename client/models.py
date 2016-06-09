from django.db import models
import uuid
import string
import random
import datetime
from django.template.defaultfilters import slugify

# Create your models here.

class Client(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=200, blank=False, editable=False)
    slug = models.SlugField(unique=True, blank=False, editable=False, help_text='This field is autofilled while saving.')
    company_name = models.CharField(max_length=100, blank=False)
    app_name = models.CharField(max_length=100, blank=False)
    package_name = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    readonly_fields = ('id', 'slug')

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return (self.id.__str__() + "<->" + self.app_name.__str__())

    def __unicode__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so adding slug
            self.id = uuid.uuid4()
            self.slug = slugify(self.app_name) + '-' + id_generator()
            self.created_at = datetime.datetime.utcnow()

        self.updated_at = datetime.datetime.utcnow()
        super(Client, self).save(*args, **kwargs)



def id_generator(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
