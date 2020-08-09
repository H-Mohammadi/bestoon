# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import User, Token, Income, Expense
from datetime import datetime
from django.http.response import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# random_str = lambda N: ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)


def register(request):
    return render(request, 'web/register.html')
    # if request.POST.has_key('requestcode'):
    #     if not grecaptcha_verify(request):
    #         context = {'massage': "plz checked I`m not robot"}
    #         return render(request, 'register.html', context)
    #     if User.objects.filter(email=request.POST['email']).exists():
    #         context = {'massage': 'email existed!'}
    #         return render(request, 'register.html', context)
    #     if not User.objects.filter(username=request.POST['username']).exists():
    #         code = random_str(28)
    #         now = datetime.now()
    #         email = request.POST['email']
    #         temporarycode = Passwordresetcodes(email=email, time=now, code=code, username=username, password=pass)
    #         temporarycode.save()
    #         message = PMMail(api_key=settings.POSTMARK_API_TOKEN,
    #                          subject = "active account",
    #                          sender= "mohammadih120@gmail",
    #                          to= email,
    #                          text_body = "for active your account click this link")


# csrf_cancel
@csrf_exempt
def submit_expense(request):
    """user submit request"""

    # TODO; validate data. user might be fake. token might be fake, amount might be fake
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    Expense.objects.create(user=this_user,
                           amount=request.POST['amount'],
                           text=request.POST['text'],
                           date=date)

    return JsonResponse({
        'status': 'ok'
    }, encoder=json.JSONEncoder)


@csrf_exempt
def submit_income(request):
    """user submit an income"""

    # TODO; validate data. user might be fake. token might be fake, amount might be fake
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    Income.objects.create(user=this_user,
                          amount=request.POST['amount'],
                          text=request.POST['text'],
                          date=date)

    return JsonResponse({
        'status': 'ok'
    }, encoder=json.JSONEncoder)
