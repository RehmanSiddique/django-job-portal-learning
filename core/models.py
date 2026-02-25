from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Apply(models.Model):
    Status_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=Status_CHOICES, default='applied')
    applied_date = models.DateTimeField(auto_now_add=True, editable=False)
    
    class Meta:
        unique_together = ('user', 'job')
        ordering = ['-applied_date']
    
    def __str__(self):
        return f"{self.user.username} applied for {self.job.title}"
    
    