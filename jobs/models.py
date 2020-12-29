from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='images')
    summary = models.CharField(max_length=256)
    github = models.CharField(max_length=256)
    demo = models.CharField(max_length=256)

    def __str__(self):
        return self.name
