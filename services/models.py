from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

SERVICE_TYPE_CHOICES = [
    (1, 'Initial Appointment'),
    (2, 'Follow-up Appointment'),
    (3, 'Package Deal'),
    (4, 'Treatment'),
]


class Service(models.Model):
    """
    Stores a single service.
    """
    service_type = models.PositiveSmallIntegerField(
        choices=SERVICE_TYPE_CHOICES)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.PositiveIntegerField()
    session_count = models.PositiveIntegerField(default=1)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['service_type', 'name']

    def __str__(self):
        return self.name
