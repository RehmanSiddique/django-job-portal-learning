from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Job, Apply
from django.db.models import Q

# Create your views here.


@login_required
def job_lists(request):
    query = request.GET.get('q', '')
    if query:
        job_posts = Job.objects.filter(
            Q(title__icontains=query) | 
            Q(company__icontains=query) | 
            Q(location__icontains=query)
        )
    else:
        job_posts = Job.objects.all()
    return render(request, 'job_lists.html', {'job_posts': job_posts, 'query': query})

@login_required
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'job_detail.html', {'job': job})

@login_required
def apply_job(request, job_id):
    if request.method == 'POST':
        job = get_object_or_404(Job, id=job_id)
        user_id = request.POST.get('user_id')
        Apply.objects.create(user_id=user_id, job=job)
        return redirect('job_detail', job_id=job_id)
    return redirect('job_lists')

def post_job(request):
    if request.method == 'POST':
        Job.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            company=request.POST['company'],
            location=request.POST['location'],
            salary=request.POST['salary'],
            create_by_id=request.POST['user_id']
        )
        return redirect('job_lists')
    return render(request, 'post_job.html')

def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    applications = Apply.objects.filter(user=user)
    posted_jobs = Job.objects.filter(create_by=user)
    return render(request, 'profile.html', {
        'user': user,
        'applications': applications,
        'posted_jobs': posted_jobs
    })

def create_profile(request):
    if request.method == 'POST':
        User.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password'],
            city=request.POST['city']
        )
        return redirect('job_lists')
    return render(request, 'create_profile.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('job_lists')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('job_lists')
    
    return render(request, 'login.html')


def register(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('login')

    return render(request, 'register.html')


def user_logout(request):
    logout(request)
    return redirect('login')