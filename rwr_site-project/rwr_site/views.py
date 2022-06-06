from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse('My Home Page')

def my_custom_page_not_found_view(request,exception):
    return render(request, 'error_view.html', status=404)
