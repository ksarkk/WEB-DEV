from django.shortcuts import render
import json
from .models import Vacancy, Company
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def get_companies(request) :
    if request.method == 'GET' :
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]

        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST' :
        return JsonResponse({
            'buba' : 'ok'
        })

def get_company(request, pk = None) :
    try :
        company = Company.objects.get(id = pk)
        return JsonResponse(company.to_json())
    except Company.DoesNotExist as exp :
        return JsonResponse({
            'ERROR' : str(exp)
        })

def get_vacancy_by_company(request, pk = None) :
    try :
        company = Company.objects.get(id = pk)
        vacancies = Vacancy.objects.filter(company = company)
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    except Company.DoesNotExist as exp :
        return JsonResponse({
            'ERROR' : str(exp)
        })
    
@csrf_exempt
def get_vacancies(request) :
    if request.method == 'GET' :
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]

        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST' :
        data = json.loads(request.body)
        company_id=data.get('company')

        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            return JsonResponse({'error': 'Company not found'})
    
        vacancy = Vacancy.objects.create(name=data.get('name'), 
                                         description=data.get('description'),
                                         salary=data.get('salary'), 
                                         company=company)
        return JsonResponse(vacancy.to_json())

    

def get_vacancy(request, pk = None) :
    try :
        vacancy = Vacancy.objects.get(id = pk)
        return JsonResponse(vacancy.to_json())
    except Vacancy.DoesNotExist as exp :
        return JsonResponse({
            'ERROR' : str(exp)
        })
    
def top_ten(request) :
    top_ten_vacancies = Vacancy.objects.order_by('-salary')[:10]

    top_ten_json = [vacancy.to_json() for vacancy in top_ten_vacancies]

    return JsonResponse(top_ten_json, safe=False)
