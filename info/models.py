from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class InfoBlog(models.Model):
    """"""

    name = models.CharField(max_length=30, null=False)
    text = models.TextField()
    rating = models.FloatField(validators=[MinValueValidator(1.), MaxValueValidator(10.)])
    price = models.FloatField(null=False)
    is_deleted = models.BooleanField(null=False, default=False)
    access_date = models.DateField(null=False, blank=False, default=timezone.now)

    def __str__(self):
        return self.name