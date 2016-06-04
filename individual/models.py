from django.db import models
from client.models import Client
import uuid
import datetime

# Create your models here.
class Individual(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=200, blank=False, editable=False)
    external_id = models.CharField(max_length=100, blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="client")
    os = models.CharField(max_length=32, blank=False, default='')
    version = models.CharField(max_length=32, blank=False, default='')
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    readonly_fields = ('id')

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return (self.id.__str__() + "<->" + self.external_id.__str__())

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so smet slug
            self.id = uuid.uuid4()
            self.created_at = datetime.datetime.today()

        self.updated_at = datetime.datetime.today()
        super(Individual, self).save(*args, **kwargs)