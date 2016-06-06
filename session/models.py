from django.db import models
from individual.models import Individual
import uuid
import datetime

SESSION_STATUS = (
    ('ACTIVE', 'SESSION_ON'),
    ('INACTIVE', 'SESSION_OFF')
)

SESSION_TYPES = (
    ('A', 'ASSERT'),
    ('D', 'DEBUG'),
    ('E', 'ERROR'),
    ('I', 'INFO'),
    ('V', 'VERBOSE'),
    ('W', 'WARN'),
    ('ALL', 'ALL_LOGS')
)

class Session(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=200, blank=False, editable=False)
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE, verbose_name="individual")
    context = models.TextField()
    status = models.CharField(choices=SESSION_STATUS, default='INACTIVE', max_length=64, blank=False, null=False)
    type = models.CharField(choices=SESSION_TYPES, default='V', max_length=64, blank=False, null=False)
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)
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

        #TODO: Establish relation and validations between started_at, ended_at and status
        self.updated_at = datetime.datetime.utcnow()
        super(Session, self).save(*args, **kwargs)
