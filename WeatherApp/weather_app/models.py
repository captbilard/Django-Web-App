from django.db import models

# Create your models here.
class City(models.Model):
    City = models.CharField(max_length= 40)
    class Meta:
        verbose_name_plural = "Cities"
    
    def __str__(self):
        return self.City

