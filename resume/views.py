from django.shortcuts import render
from django.views import View
from .models import Resume
from django.contrib.auth.models import User
from django.db import connection

# Create your views here.
class HomeView(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'home.html')

class LoginView(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'login.html')

class SignupView(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'signup.html')


class ResumeView(View):

    def get(self, request, *args, **kwargs):
        # first need to get resume list
        user_list = User.objects.all()
        sql = """SELECT user.id, user.username, resume.description
        FROM auth_user user
        ,    resume_resume resume 
        
        WHERE user.id = resume.id"""
        results = []
        with connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()

        # print(results)
        context = {
            'users': results
        }

        return render(request, 'resume.html', context=context)


