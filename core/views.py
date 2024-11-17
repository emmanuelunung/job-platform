from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from .models import Application, Job, CustomUser
from django.db.models import Q
from .models import JobAlert
from .forms import JobAlertForm
from .forms import ResumeUploadForm
from .forms import CompanyProfileForm
from .models import CompanyProfile
from .forms import CompanyReviewForm
from .models import CompanyReview


# Create your views here.

def home(request):
    applications = Application.objects.all()

    context = {"applications": applications}
    return render(request, 'core/home.html', context)


def detail(request, pk):
    application = get_object_or_404(Application, pk=pk)

    related_application = Application.objects.filter(applicant=application.applicant)

    context = {
        "application": application,
        "related_application": related_application
    }
    return render(request, "core/detail.html", context)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


def apply(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        resume = request.FILES['resume']
        application = Application(job=job, applicant=request.user, resume=resume)
        application.save()
        return redirect('job_list')
    return render(request, 'apply.html', {'job': job})


def application_list(request):
    applications = Application.objects.filter(applicant=request.user)
    return render(request, 'application_list.html', {'applications': applications})


def job_list(request):
    query = request.GET.get('q')
    if query:
        jobs = Job.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(company__icontains=query) |
            Q(location__icontains=query)
        )
    else:
        jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})


def create_alert(request):
    if request.method == 'POST':
        form = JobAlertForm(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.user = request.user
            alert.save()
            return redirect('alert_list')
    else:
        form = JobAlertForm()
    return render(request, 'create_alert.html', {'form': form})

def alert_list(request):
    alerts = JobAlert.objects.filter(user=request.user)
    return render(request, 'alert_list.html', {'alerts': alerts})


def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('profile')
    else:
        form = ResumeUploadForm()
    return render(request, 'upload_resume.html', {'form': form})


def create_company_profile(request):
    if request.method == 'POST':
        form = CompanyProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = CompanyProfileForm()
    return render(request, 'create_company_profile.html', {'form': form})

def company_profile(request):
    profile = CompanyProfile.objects.get(user=request.user)
    return render(request, 'company_profile.html', {'profile': profile})


def add_review(request, company_id):
    company = get_object_or_404(CompanyProfile, id=company_id)
    if request.method == 'POST':
        form = CompanyReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.company = company
            review.user = request.user
            review.save()
            return redirect('company_profile', company_id=company.id)
    else:
        form = CompanyReviewForm()
    return render(request, 'add_review.html', {'form': form, 'company': company})

def company_reviews(request, company_id):
    company = get_object_or_404(CompanyProfile, id=company_id)
    reviews = CompanyReview.objects.filter(company=company)
    return render(request, 'company_reviews.html', {'company'})


def search_jobs(request):
    query = request.GET.get('q')
    jobs = Job.objects.filter(title__icontains=query)
    return render(request, 'jobs/job_list.html', {'jobs': jobs})



def about_us(request):
    return render(request, 'about_us.html')



def signup(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:home")

    else:
        form = RegisterForm()

    context = {"form": form}
    return render(request, "core/signup.html", context)

def login_view(request):

    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("core:home")

    else:
        form = UserLoginForm()

    context = {"form": form}
    return render(request, "core/login.html", context)

def logout_view(request):
    logout(request)
    return redirect("coreApp:login")







