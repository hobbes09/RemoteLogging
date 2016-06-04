from django.db import models
import uuid
from individual.models import Individual

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
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    type = models.CharField(choices=LOG_TYPES, default='V', max_length=100)
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE, verbose_name="individual", )

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return (self.id.__str__() + "<->" + self.body.__str__())

