from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Job, Apply
from django.db.models import Q

# Create your views here.


@login_required
def job_lists(request):
    job_posts = Job.objects.all()
    
    # Search by job title
    query = request.GET.get('q', '')
    if query:
        job_posts = job_posts.filter(title__icontains=query)
    
    # Filter by company
    company = request.GET.get('company', '')
    if company:
        job_posts = job_posts.filter(company__icontains=company)
    
    # Filter by salary (minimum salary)
    min_salary = request.GET.get('min_salary', '')
    if min_salary:
        try:
            job_posts = job_posts.filter(salary__gte=int(min_salary))
        except ValueError:
            pass
    
    # Filter by keyword (searches in title, description, location, company)
    keyword = request.GET.get('keyword', '')
    if keyword:
        job_posts = job_posts.filter(
            Q(title__icontains=keyword) | 
            Q(description__icontains=keyword) | 
            Q(location__icontains=keyword) |
            Q(company__icontains=keyword)
        )
    
    context = {
        'job_posts': job_posts,
        'query': query,
        'company': company,
        'min_salary': min_salary,
        'keyword': keyword
    }
    return render(request, 'job_lists.html', context)

@login_required
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'job_detail.html', {'job': job})

@login_required
def apply_job(request, job_id):
    if request.method == 'POST':
        job = get_object_or_404(Job, id=job_id)
        Apply.objects.get_or_create(user=request.user, job=job)
        return redirect('my_applications')
    return redirect('job_lists')

@login_required
def post_job(request):
    if request.method == 'POST':
        Job.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            company=request.POST['company'],
            location=request.POST['location'],
            salary=request.POST['salary'],
            create_by=request.user
        )
        return redirect('job_lists')
    return render(request, 'post_job.html')

@login_required
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    applications = Apply.objects.filter(user=user)
    posted_jobs = Job.objects.filter(create_by=user)
    return render(request, 'profile.html', {
        'user': user,
        'applications': applications,
        'posted_jobs': posted_jobs
    })


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

@login_required
def my_applications(request):

    applications = Apply.objects.filter(user=request.user)

    return render(request, 'my_applications.html',
                  {'applications': applications})