from django.shortcuts import render
from contactform.models import Contacts
from usermanager.models import Usermanager
from bizzsole.siteinfo import site_name, site_icon, site_logo
from django.contrib.auth.models import User, Group, Permission


def error(request, message='custom message' or 'access_denied' or 'required_all' or 'data_na' or 'image_file' or 'image_5mb', title=None):
    if message == 'access_denied': message = 'You have not enough permissions to access. For more information, please contact administrator.'
    if message == 'required_all': message = 'You are missing some data. Please fill out all fields.'
    if message == 'data_na': message = 'Data not available. We are unable to complete your request.'
    if message == 'image_file': message = 'Selected file format is not supported. You can only select image file to proceed.'
    if message == 'image_5mb': message = 'Selected file size is not supported. You can only upload image less than 5 MB.'

    if title == '' or title == None:
        title = 'Error'

    error_site_name = site_name + ' | Error'

    return render(request, 'error.html',{
        'site_name':error_site_name, 
        'title':title,
        'message':message,
        'site_icon':site_icon,
        'user_name':request.user.username,
        'activeuser':Usermanager.objects.filter(username=request.user.username,
        )})


def error_front(request, message, title=None):
    error_site_name = site_name + ' | Error'

    if title == '' or title == None:
        title = 'Error'

    return render(request, 'error_front.html',{
        'site_name':error_site_name,
        'title':title,
        'error_message':message,
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
def access_permission(request, code_name=None, user_only_data=False):
    permission = 0

    if not request.user.is_authenticated:
        permission = -1
        return permission

    for i in request.user.groups.all():
        if i.name == 'Super User' or i.pk == 1 : permission = 1

    if permission == 0:
        perm = request.user.get_all_permissions()
        for i in perm:
            if i == code_name: permission = 1
            if i == code_name + '_user_only': permission = 2
 
    return permission


