from django.contrib import admin
from .models import Job, CustomUser, Application, JobAlert, Resume, CompanyReview, CompanyProfile

# Register your models here.

admin.site.register(Application)
admin.site.register(Job)
admin.site.register(CustomUser)
admin.site.register(JobAlert)
admin.site.register(Resume)
admin.site.register(CompanyReview)
admin.site.register(CompanyProfile)
