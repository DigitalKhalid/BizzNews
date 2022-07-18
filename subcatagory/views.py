from sre_constants import SUCCESS
from django.shortcuts import render, get_object_or_404, redirect
from subcatagory.models import Subcatagory
from django.contrib import messages
from catagory.models import Catagory
from main.views import site_name
from bizzsupport import error
from contactform.models import Contacts

site_name = site_name + ' | Sub-Catagories'
unread_contacts = Contacts.objects.filter(readstatus=False).count()

# Subcatagory List
def subcatagory_list(request):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    subcatagory = Subcatagory.objects.all
    catagory = Catagory.objects.all
    return render(request, 'subcatagory_list.html', {'site_name':site_name, 'user_name':request.user.username,'subcatagory' : subcatagory, 'catagory':catagory, 'unread_contacts':unread_contacts,})

# Subcatagory Add
def add_subcatagory(request):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    catagory = Catagory.objects.all

    if request.method == 'POST':
        save_subcatagory(request, 'new')

        if error_message != '':
            return error(request, error_message)
        else:
            return redirect('subcatagory_list')

    return render(request, 'subcatagory_add.html', {'site_name':site_name, 'user_name':request.user.username,'catagory' : catagory, 'unread_contacts':unread_contacts,})

# Subcatagory Delete
def delete_subcatagory(request, pk):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    delete_data = Subcatagory.objects.get(pk=pk)
    
    delete_data.delete()
    messages.success(request, 'Sub catagory deleted successfully.')

    return redirect('subcatagory_list')

# Subcatagory Edit
def subcatagory_edit(request, pk):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End
    
    global old_subcatagory

    subcatagory = Subcatagory.objects.get(pk=pk)
    catagory = Catagory.objects.all

    old_subcatagory = subcatagory.subcatagory

    if request.method == 'POST':
        save_subcatagory(request, 'edit', pk)
        
        if error_message != '':
            return error(request, error_message)
        else:
            return redirect('subcatagory_list')

    return render(request, 'subcatagory_edit.html', {'site_name':site_name, 'user_name':request.user.username,'pk':pk, 'subcatagory':subcatagory, 'catagory':catagory, 'unread_contacts':unread_contacts,})

# Subcatagory Save
def save_subcatagory(request, type = 'new' or 'edit', pk=None):
    global error_message
    error_message = ''

    subcatagory_name = request.POST.get('subcatagory_name')
    maincatagory_id = request.POST.get('maincatagory_id')

    if subcatagory_name == '' or maincatagory_id == '0':
        error_message = 'You are missing some data. All fields are required.'
        return error_message

    elif len(Subcatagory.objects.filter(subcatagory=subcatagory_name)) != 0 and subcatagory_name != old_subcatagory:
        error_message = 'This sub-catagory is already exits. Duplicate names are not allowed.'
        return error_message

    else:
        if type == 'new':
            write_data = Subcatagory(
                subcatagory = subcatagory_name,
                catagoryid = maincatagory_id)

            write_data.save()

        elif type == 'edit':
            write_data = Subcatagory.objects.get(pk=pk)
            write_data.subcatagory = subcatagory_name
            write_data.catagoryid = maincatagory_id

            write_data.save()