from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images')
    summary = models.CharField(max_length=256)

    def __str__(self):
        return self.summary[0:100]
