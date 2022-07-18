from django.shortcuts import render, get_object_or_404, redirect
from catagory.models import Catagory
from django.contrib import messages
from main.views import site_name
from bizzsupport import error
from news.models import News
from subcatagory.models import Subcatagory
from contactform.models import Contacts

site_name = site_name + ' | Catagories'
unread_contacts = Contacts.objects.filter(readstatus=False).count()

# Catagory List
def catagory_list(request):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End
    
    catagory = Catagory.objects.all
    return render(request, 'catagory_list.html', {'site_name':site_name, 'catagory' : catagory, 'unread_contacts':unread_contacts, 'user_name':request.user.username,})

# Catagory Add
def add_catagory(request):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    if request.method == 'POST':
        save_catagory(request, 'new')

        if error_message != '':
            return error(request, error_message)
        else:
            return redirect('catagory_list')

    return render(request, 'catagory_add.html',{'site_name':site_name, 'unread_contacts':unread_contacts,'user_name':request.user.username,})

# Catagory Delete
def delete_catagory(request, pk):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    delete_data = Catagory.objects.get(pk=pk)
    
    delete_data.delete()
    messages.success(request, 'News deleted successfully.')

    return redirect('catagory_list')

# Catagory Edit
def catagory_edit(request, pk):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    catagory = Catagory.objects.get(pk=pk)

    if request.method == 'POST':
        save_catagory(request, 'edit', pk)

        if error_message != '':
            return error(request, error_message)
        else:
            return redirect('catagory_list')

    return render(request, 'catagory_edit.html', {'site_name':site_name, 'catagory':catagory, 'unread_contacts':unread_contacts,'user_name':request.user.username,})

# Catagory Save
def save_catagory(request, type= 'new' or 'edit', pk=None):
        global error_message
        error_message = ''

        catagory_name = request.POST.get('catagory_name')

        if catagory_name == '':
            error_message = 'You are missing some data. All fields are required.'
            return error_message

        else:
            if type == 'new':
                write_data = Catagory(
                    catagory = catagory_name)
                    
                write_data.save()
            
            elif type == 'edit':
                write_data = Catagory.objects.get(pk=pk)
                write_data.catagory = catagory_name

                write_data.save()