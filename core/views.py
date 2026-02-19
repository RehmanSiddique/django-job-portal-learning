from django.shortcuts import render
from .models import Job

# Create your views here.


def job_lists(request):
    job_posts = Job.objects.all()
    return render(request, 'job_lists.html', {'job_posts': job_posts})