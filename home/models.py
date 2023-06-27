from django.db import models
from django.utils import timezone

# Create your models here.


class Contact(models.Model):
    """
    Contact Form model for posting to the admin panel
    """

    email = models.EmailField(blank=False)
    name = models.CharField(max_length=50, blank=False)
    message = models.TextField(blank=False)
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name}, {self.email}"

    class Meta:
        # Name for admin panel
        verbose_name = "Contact Form Submission"
