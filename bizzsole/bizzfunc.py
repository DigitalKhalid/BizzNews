from django.shortcuts import render
from contactform.models import Contacts
from usermanager.models import Usermanager
from bizzsole.siteinfo import site_name, site_icon, site_logo


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


# Get No. of Unread Messages Received from Contact Form
def unread_contacts(request):
    unread_contacts = Contacts.objects.filter(readstatus=False).count()
    return unread_contacts


def user_name(request):
    user_name = request.user.username
    return user_name


# Check Access Permission for Logged In User
def access_permission(request):
    permission = 0

    if not request.user.is_authenticated:
        permission = -1
        return permission

    for i in request.user.groups.all():
        if i.name == 'Super User' or i.pk == 1 : permission = 1
    
    return permission


