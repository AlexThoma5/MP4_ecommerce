from django.db import models


SUBJECT_CHOICES = [
    (1, 'General Enquiry'),
    (2, 'Treatment Information'),
    (3, 'Pricing Question'),
    (4, 'Existing Client Query'),
    (5, 'Other'),
]


class ContactMessage(models.Model):
    """
    Stores a single contact messsage.
    """
    full_name = models.CharField(max_length=64)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    subject = models.PositiveSmallIntegerField(
        choices=SUBJECT_CHOICES)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f'Contact message from {self.full_name}'
