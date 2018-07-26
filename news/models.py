from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Domaine(models.Model):
    title = models.CharField(max_length = 250)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Article(models.Model):
    LOC = (
            ('GN', 'Guinée'),
            ('AF', 'Afrique'),
            ('WD', 'Monde'),
        )
    pub_date = models.DateTimeField()
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    localisation = models.CharField(max_length=3, choices=LOC)
    title = models.CharField(max_length = 350)
    image = models.ImageField(upload_to='images', blank= True)
    content = models.TextField()
    redacteur = models.CharField(max_length = 250)
    # creted_by
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)