from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Portfolio(models.Model):
    photo = models. ImageField(null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg',"jpge','png'])])#(quepuedeserunaURL)"])])
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    tags = models.CharField(max_length=100)
    url = models.CharField(max_length=200)