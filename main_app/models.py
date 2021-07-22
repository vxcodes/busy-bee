from django.db import models
from django.urls import reverse
# Create your models here.
class Comb(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    atchieve_by = models.DateField(auto_now_add=False, auto_now=False, null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'comb_id': self.id })

class Goal(models.Model):
    goal_title = models.CharField(max_length=100)
    goal_description = models.TextField(max_length=1000)
    goal_atchieve_by = models.DateField(auto_now_add=False, auto_now=False, null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, null=True)

    def __str__(self):
        return self.goal_title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

class Charm(models.Model):
    CHARMS = (
        ('S', 'Started'),
        ('H', 'Halfway'),
        ('D', 'Done'),
    )

    date = models.DateField('Complete by')
    charm = models.CharField(
        max_length=1,
        choices=CHARMS,
        default=CHARMS[0][0]
    )
    comb = models.ForeignKey(Comb, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_charm_display()} on {self.date}"