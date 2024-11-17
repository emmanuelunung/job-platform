from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    company = models.CharField(max_length=100, blank=True, null=True)
    is_employer = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name_plural = "Custom User"

    def __str__(self):
        return self.company


class Job(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return str(self.applicant.company)



class JobAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    frequency = models.CharField(max_length=50, choices=[('daily', 'Daily'), ('weekly', 'Weekly')])


class Resume(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')




class CompanyReview(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    reviewer_email = models.EmailField()




class CompanyProfile(models.Model):
    INDUSTRY_CHOICES = [
        ('tech', 'Technology'),
        ('finance', 'Finance'),
        ('healthcare', 'Healthcare'),
        ('education', 'Education'),
        ('manufacturing', 'Manufacturing'),
        ('retail', 'Retail'),
        ('other', 'Other'),
    ]

    SIZE_CHOICES = [
        ('small', 'Small (1-50 employees)'),
        ('medium', 'Medium (51-200 employees)'),
        ('large', 'Large (200+ employees)'),
    ]

    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES)
    company_size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    location = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
