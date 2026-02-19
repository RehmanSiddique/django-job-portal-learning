from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.


def job_lists(request):
    job_posts = Job.objects.all()
    return render(request, 'job_lists.html', {'job_posts': job_posts})

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'job_detail.html', {'job': job})