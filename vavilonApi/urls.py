from django.urls import path, include
from rest_framework import routers
from .views import IncomeViewSet, IncomeCategoryViewSet, ExpensesCategoryViewSet, ExpensesViewSet
income_router = routers.SimpleRouter()
income_router.register(r'income', IncomeViewSet)
income_category_router = routers.SimpleRouter()
income_category_router.register(r'incomeCategory', IncomeCategoryViewSet)
expenses_router = routers.SimpleRouter()
expenses_router.register(r'expenses', ExpensesViewSet)
expenses_category_router = routers.SimpleRouter()
expenses_category_router.register(r'expensesCategory', ExpensesCategoryViewSet)

urlpatterns = [
    path('api/v1/', include(income_router.urls)),   # http://127.0.0.1:8000/vavilonApi/api/v1/income/
    path('api/v1/', include(expenses_router.urls)),
    path('api/v1/', include(income_category_router.urls)),
    path('api/v1/', include(expenses_category_router.urls)),
]
