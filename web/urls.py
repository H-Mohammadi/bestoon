from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'submit/expense/$', views.submit_expense, name='submit_expense'),
    re_path(r'submit/income/$', views.submit_income, name='submit_income'),
    re_path(r'^register/$', views.register, name='register'),
]
