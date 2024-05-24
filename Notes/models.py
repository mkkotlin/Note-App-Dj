from django.db import models

# Create your models here.

class Notes(models.Model):

    title = models.CharField(max_length=100)
    description =  models.TextField(max_length=500)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title