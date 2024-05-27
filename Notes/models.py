from django.db import models

# Create your models here.


class DropDown(models.Model):
    drop_down = models.CharField(blank=True, max_length= 50)

    def __str__(self):
        return self.drop_down

class Notes(models.Model):

    title = models.CharField(max_length=100,unique=True)
    description =  models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    drop_down = models.ForeignKey(DropDown, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    