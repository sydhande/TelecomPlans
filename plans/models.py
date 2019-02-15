from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Landline(models.Model):
    planname = models.CharField(max_length=100)
    applicability = models.CharField(max_length=100)
    fmc = models.CharField(max_length=50)
    talkvalue = models.CharField(max_length=100)
    callcharges = models.CharField(max_length=100)
    remark = models.TextField()
    dateposted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.planname

    def get_absolute_url(self):
        return reverse('landline-detail', kwargs={'pk': self.pk})


class Broadband(models.Model):
    planname = models.CharField(max_length=100)
    speed = models.CharField(max_length=100)
    fmc = models.CharField(max_length=50)
    freedata = models.CharField(max_length=100)
    freeCalls = models.CharField(max_length=150)
    callcharges = models.CharField(max_length=100)
    securitydeosit = models.CharField(max_length=100)
    addfac = models.TextField()
    remark = models.TextField()
    dateposted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.planname

    def get_absolute_url(self):
        return reverse('broadband-detail', kwargs={'pk': self.pk})
