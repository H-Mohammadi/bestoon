from django.contrib import admin
from .models import Expense, Income, Token


# Register your models here.

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount')


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount')


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('user',)


