from django.shortcuts import render

from . import models


def hassan(request):
    jobs = models.Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})
