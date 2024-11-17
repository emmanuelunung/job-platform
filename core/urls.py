from django.urls import path

app_name = 'core'

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('jobs/', views.job_list, name='job_list'),
    path('apply/<int:job_id>/', views.apply, name='apply'),
    path('applications/', views.application_list, name='application_list'),
    path('alerts/', views.alert_list, name='alert_list'),
    path('alerts/create/', views.create_alert, name='create_alert'),
    path('upload_resume/', views.upload_resume, name='upload_resume'),
    path('company_profile/', views.company_profile, name='company_profile'),
    path('company_profile/create/', views.create_company_profile, name='create_company_profile'),
    path('about-us/', views.about_us, name='about'),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

]



