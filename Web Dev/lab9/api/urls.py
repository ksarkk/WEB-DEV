from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.get_companies),
    path('companies/<int:pk>/', views.get_company),
    path('companies/<int:pk>/vacancies/', views.get_vacancy_by_company),
    path('vacancies/', views.get_vacancies),
    path('vacancies/<int:pk>/', views.get_vacancy),
    path('vacancies/top_ten/', views.top_ten),
]