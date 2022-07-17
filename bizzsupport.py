from django.shortcuts import render
from main.views import site_name

def error(request, error):
    error_site_name = site_name + ' | Error'
    return render(request, 'error.html',{'site_name':error_site_name, 'error':error})