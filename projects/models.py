from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    url = models.URLField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
