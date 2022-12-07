from .serializers import IncomeSerializer, IncomeCategorySerializer, ExpensesSerializer, ExpensesCategorySerializer
from rest_framework import viewsets
from .models import Income, IncomeCategory, ExpensesCategory, Expenses

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class IncomeCategoryViewSet(viewsets.ModelViewSet):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer

class ExpensesViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer

class ExpensesCategoryViewSet(viewsets.ModelViewSet):
    queryset = ExpensesCategory.objects.all()
    serializer_class = ExpensesCategorySerializer