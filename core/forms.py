from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
from .models import CompanyReview
from .models import CompanyProfile



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'company', 'is_employer', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
            "placeholder": "Enter Username",
            "class": "form-control"
        }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
            "placeholder": "Enter Email",
            "class": "form-control"
        }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            "placeholder": "Enter Password",
            "class": "form-control"
        }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            "placeholder": "Repeat Password",
            "class": "form-control"
     }))



class JobAlertForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100, required=True)
    email = forms.EmailField(label='Email Address', required=True)


    job_title = forms.CharField(label='Preferred Job Title', max_length=100, required=False)
    location = forms.CharField(label='Preferred Location', max_length=100, required=False)
    job_type_choices = [
        ('full-time', 'Full-Time'),
        ('part-time', 'Part-Time'),
        ('contract', 'Contract'),
        ('remote', 'Remote')
    ]
    job_type = forms.ChoiceField(label='Job Type', choices=job_type_choices, required=False)
    salary_range = forms.IntegerField(label='Expected Salary Range', required=False, min_value=0)
    experience_level_choices = [
        ('entry-level', 'Entry Level'),
        ('mid-level', 'Mid Level'),
        ('senior-level', 'Senior Level'),
        ('executive', 'Executive')
    ]
    experience_level = forms.ChoiceField(label='Experience Level', choices=experience_level_choices, required=False)

    alert_frequency_choices = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly')
    ]
    alert_frequency = forms.ChoiceField(label='How often do you want to receive job alerts?', choices=alert_frequency_choices)
    job_categories = forms.CharField(label='Preferred Job Categories', max_length=200, required=False)
    opt_in = forms.BooleanField(label='Receive Job Alerts', initial=True, required=False)

    success_message = forms.CharField(widget=forms.HiddenInput(), required=False)


class ResumeUploadForm(forms.Form):

    full_name = forms.CharField(label='Full Name', max_length=100, required=True)
    email = forms.EmailField(label='Email Address', required=True)

    resume = forms.FileField(label='Upload Your Resume', required=True)

    cover_letter = forms.FileField(label='Upload Cover Letter', required=False)

    instructions = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}),
                                   initial="Please upload your resume in PDF, DOCX, or TXT format.", required=False)


class CompanyReviewForm(forms.ModelForm):
    class Meta:
        model = CompanyReview
        fields = ['company', 'user', 'reviewer_email', 'rating', 'review_text']


    review_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=True)

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['name', 'industry', 'company_size', 'location', 'description', 'logo', 'website']


    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=True)
