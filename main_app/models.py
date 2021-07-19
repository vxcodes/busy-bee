from django.db import models

# Create your models here.
class Comb(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    atchieve_by = models.DateField(auto_now_add=False, auto_now=False, null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, null=True)

    def __str__(self):
        return self.title