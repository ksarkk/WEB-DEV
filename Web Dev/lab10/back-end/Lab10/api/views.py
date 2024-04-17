from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Company, Vacancy
from . import serializers


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer

    @action(detail=True, methods=['GET'])
    def vacancies(self, request, *args, **kwargs):
        company = self.get_object()
        vacancies = company.vacancy_set.all()
        serializer = serializers.VacancySerializer(vacancies, many=True)
        return Response(serializer.data)


class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = serializers.VacancySerializer

    @action(detail=False, methods=['GET'])
    def top_ten(self, request):
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = serializers.VacancySerializer(vacancies, many=True)
        return Response(serializer.data)


# def company_list(request):
#     companies = Company.objects.all()
#     try:
#         companies_json = [c.to_jsonCom() for c in companies]
#     except Company.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})
#     return JsonResponse(companies_json, safe=False)
#


