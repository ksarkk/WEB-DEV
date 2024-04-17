from django.shortcuts import render, HttpResponse
from .models import Category, Product
from django.http.response import JsonResponse
# Create your views here.

def home(request) :
    return render(request, 'home.html')

def get_products(request) :
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]

    return JsonResponse(products_json, safe=False)

def get_product(request, pk = None) :
    try :
        product = Product.objects.get(id=pk)
        return JsonResponse(product.to_json())
    except Product.DoesNotExist as exception :
        return JsonResponse({
            'error' : str(exception)
        })

def get_categories(request) :
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]

    return JsonResponse(categories_json, safe=False)

def get_category(request, pk = None) :
    try :
        category = Category.objects.get(id=pk)
        return JsonResponse(category.to_json())
    except Category.DoesNotExist as exception :
        return JsonResponse({
            'error': str(exception)
        })
    
def get_products_by_category(request, pk = 0) :
    try :
        products = Product.objects.all()
        products_cleaned_json = [product.to_json() for product in products if product.category_id == pk]

        return JsonResponse(products_cleaned_json, safe=False)
    except Product.DoesNotExist as exception :
        return JsonResponse({
            'error' : str(exception)
        })