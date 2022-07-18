from django.shortcuts import render
from main.views import site_name
from contactform.models import Contacts

def error(request, error):
    error_site_name = site_name + ' | Error'
    return render(request, 'error.html',{'site_name':error_site_name, 'error':error})

def unread_contacts(request):
    unread_contacts = Contacts.objects.filter(readstatus=False).count()
    return unread_contacts

def user_name(request):
    user_name = request.user.username
    return user_name
