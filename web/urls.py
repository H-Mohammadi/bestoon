from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'submit/expense/$', views.submit_expense, name='submit_expense')
]
