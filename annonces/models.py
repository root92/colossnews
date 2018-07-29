from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Entreprise(models.Model):
    ent_name = models.CharField(max_length = 250)
    adresse_1 = models.CharField(max_length = 250)
    adresse_2 = models.CharField(max_length = 250)
    telephone = models.IntegerField()
    mobile = models.IntegerField()
    email = models.EmailField()
    about = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ent_name

class Annonce(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    job_title = models.CharField(max_length = 250)
    description = models.TextField()
    limite_date = models.DateTimeField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title

class Apply(models.Model):
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 250)
    middle_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length = 250)
    telephone = models.IntegerField()
    email = models.EmailField()
    adresse_1 = models.CharField(max_length = 250)
    adresse_2 = models.CharField(max_length = 250)

    def __str__(self):
        return self.first_name

class Doc(models.Model):
    apply = models.ForeignKey(Apply, on_delete=models.CASCADE)
    doc = models.FileField() 

    