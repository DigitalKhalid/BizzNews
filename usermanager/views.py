from django.shortcuts import render, redirect
from .models import Usermanager
from django.contrib.auth.models import User
from main.views import site_logo, site_icon, site_name

site_name = site_name + ' | Users'

def user_list(request):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    usermanager = Usermanager.objects.all()

    return render(request, 'user_list.html',{
        'usermanager':usermanager,
        'user_name':request.user.username,
        'site_name':site_name,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'activeuser':Usermanager.objects.filter(username=request.user.username)
    })


def user_edit(request, pk):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    if request.method == 'POST':
        save_user(request, pk)

        if error_message == '':
            return redirect('user_list')
        else:
            return render(request, 'error.html', {
                'error_message':error_message,
                'user_name':request.user.username,
                'site_name':site_name,
                'site_icon':site_icon,
                'site_logo':site_logo,
                'activeuser':Usermanager.objects.filter(username=request.user.username)
                })

    usermanager = Usermanager.objects.get(pk=pk)

    return render(request, 'user_edit.html',{
        'usermanager':usermanager,
        'user_name':request.user.username,
        'site_name':site_name,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'activeuser':Usermanager.objects.filter(username=request.user.username)
    })

def save_user(request, pk=None):
    global error_message
    error_message = ''

    userfirstname = request.POST.get('user_firstname')
    userlastname = request.POST.get('user_lastname')
    useremail = request.POST.get('user_email')
    usercontact = request.POST.get('user_contact')
    userbiography = request.POST.get('user_biography')
    useraddress = request.POST.get('user_address')
    userstatus = request.POST.get('user_status')
    userimage = request.FILES.get('user_image')

    write_data = Usermanager.objects.get(pk=pk)

    write_data.user_firstname = userfirstname
    write_data.user_lastname = userlastname
    write_data.user_email = useremail
    write_data.user_contact = usercontact
    write_data.user_biography = userbiography
    write_data.user_address = useraddress
    write_data.user_status = userstatus

    try:
        if str(userimage.content_type).startswith('image'):
            if userimage.size < 5000000:
                write_data.user_image = userimage
                write_data.save()

            else:
                error_message = 'Selected file size is not supported. You can only upload image less than 5 MB.'
                return error_message

        else:
            error_message = 'Selected file format is not supported. You can only select image file to proceed.'
            return error_message

    except:
        write_data.save()