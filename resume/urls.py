from django.urls import path
from .views import HomeView, LoginView, SignupView, ResumeView

urlpatterns = [
    path('', HomeView.as_view(), name='resume-home'),
    path('login/', LoginView.as_view(), name='resume-login'),
    path('signup/', SignupView.as_view(), name='resume-signup'),
    path('resumes/', ResumeView.as_view(), name='resume-res-list'),
]