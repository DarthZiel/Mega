from rest_framework import serializers
from .models import Income, Expenses, IncomeCategory, ExpensesCategory
class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        exclude = ['id']

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        exclude = ['id']


class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        exclude = ['id']


class ExpensesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpensesCategory
        exclude = ['id']