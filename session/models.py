from django.db import models
from individual.models import Individual
import uuid
import datetime

class Session(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=200, blank=False, editable=False)
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE, verbose_name="individual")
    context = models.TextField()
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    class Meta:
        ordering = ('updated_at',)

    def __str__(self):
        return self.id.__str__()

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so adding slug
            self.id = uuid.uuid4()
            self.created_at = datetime.datetime.utcnow()

        self.updated_at = datetime.datetime.utcnow()
        super(Session, self).save(*args, **kwargs)