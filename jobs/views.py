from django.shortcuts import render, get_object_or_404

from . import models


def home(request):
    jobs = models.Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})


def detail(request, id):
    job = get_object_or_404(models.Job, pk=id)
    return render(request, 'jobs/detail.html', {'job': job})