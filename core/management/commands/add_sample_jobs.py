from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Job

class Command(BaseCommand):
    help = 'Add sample jobs for testing filter functionality'

    def handle(self, *args, **options):
        # Get or create a user for job posting
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={'password': 'admin123'}
        )
        
        sample_jobs = [
            {
                'title': 'Registered Nurse',
                'description': 'Experienced nursing professional needed for hospital care',
                'company': 'City Hospital',
                'location': 'New York',
                'salary': 65000,
            },
            {
                'title': 'Software Developer',
                'description': 'Python developer for web applications',
                'company': 'Tech Corp',
                'location': 'San Francisco',
                'salary': 85000,
            },
            {
                'title': 'Nursing Assistant',
                'description': 'Support nursing staff in patient care',
                'company': 'Healthcare Plus',
                'location': 'Chicago',
                'salary': 35000,
            },
            {
                'title': 'Data Analyst',
                'description': 'Analyze data and create reports',
                'company': 'Google',
                'location': 'Mountain View',
                'salary': 75000,
            },
            {
                'title': 'Marketing Manager',
                'description': 'Lead marketing campaigns and strategies',
                'company': 'Microsoft',
                'location': 'Seattle',
                'salary': 90000,
            }
        ]
        
        for job_data in sample_jobs:
            job, created = Job.objects.get_or_create(
                title=job_data['title'],
                company=job_data['company'],
                defaults={
                    'description': job_data['description'],
                    'location': job_data['location'],
                    'salary': job_data['salary'],
                    'create_by': user
                }
            )
            if created:
                self.stdout.write(f'Created job: {job.title} at {job.company}')
            else:
                self.stdout.write(f'Job already exists: {job.title} at {job.company}')
        
        self.stdout.write(self.style.SUCCESS('Sample jobs added successfully!'))