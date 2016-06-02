from django.db import models
import uuid

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
    id = models.CharField(max_length=100, primary_key=True, unique=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    type = models.CharField(choices=LOG_TYPES, default='V', max_length=100)

    class Meta:
        ordering = ('created',)


