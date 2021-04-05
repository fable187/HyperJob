from django.shortcuts import render
from django.views import View
from .models import Vacancy
from django.contrib.auth.models import User
from django.db import connection

import pandas as pd


# Create your views here.
class VacancyView(View):

    def get(self, request, *args, **kwargs):
        sql = """SELECT user.id, user.username, vacancy.description
                FROM auth_user user
                ,    vacancy_vacancy vacancy 

                WHERE user.id = vacancy.id"""
        results = []
        with connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()

        # print(results)
        context = {
            'users': results
        }

        return render(request, 'vacancy.html', context=context)
