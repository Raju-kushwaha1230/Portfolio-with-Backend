from django.db import models

# Create your models here.
class contact(models.Model):
    Name=models.CharField(max_length=255)
    Email=models.EmailField()
    Subject=models.CharField(max_length=255)
    Massage=models.CharField(max_length=500)

    def __str__(self) :
        return self.Name