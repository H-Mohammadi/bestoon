from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import User, Token, Income, Expense
from datetime import datetime


# Create your views here.
# #csrf_cancel
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
