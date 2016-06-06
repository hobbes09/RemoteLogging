from django.db import models
import uuid
import datetime
from individual.models import Individual
from session.models import Session

# Create your models here.

LOG_TYPES = (
    ('A', 'ASSERT'),
    ('D', 'DEBUG'),
    ('E', 'ERROR'),
    ('I', 'INFO'),
    ('V', 'VERBOSE'),
    ('W', 'WARN')
)

class Log(models.Model):
    id = models.CharField(max_length=100, primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    created = models.DateTimeField(editable=False)
    body = models.TextField()
    type = models.CharField(choices=LOG_TYPES, default='V', max_length=100)
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE, verbose_name="individual")
    session = models.ForeignKey(Session, on_delete=models.CASCADE, verbose_name="session", null=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return (self.id.__str__() + "<->" + self.body.__str__())

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so adding slug
            self.id = uuid.uuid4()
            self.created = datetime.datetime.utcnow()

        super(Log, self).save(*args, **kwargs)