from django.shortcuts import render
from main.views import site_name, site_icon, site_logo
from contactform.models import Contacts
from usermanager.models import Usermanager

def error(request, error):
    error_site_name = site_name + ' | Error'
    return render(request, 'error.html',{
        'site_name':error_site_name, 
        'error':error,
        'site_icon':site_icon,
        'user_name':request.user.username,
        'activeuser':Usermanager.objects.filter(username=request.user.username,
        )})

def error_front(request, error):
    error_site_name = site_name + ' | Error'
    return render(request, 'error_front.html',{
        'site_name':error_site_name,
        'error':error,
        'site_icon':site_icon,
        'site_logo':site_logo,
        })

def unread_contacts(request):
    unread_contacts = Contacts.objects.filter(readstatus=False).count()
    return unread_contacts

def user_name(request):
    user_name = request.user.username
    return user_name
