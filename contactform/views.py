from django.shortcuts import redirect, render
from .models import Contacts
from main.views import site_name, site_icon, site_logo
from usermanager.models import Usermanager

# Submit Contact Form
def contactform_submit(request):
    send_confirmation = ''

    if request.method == 'POST':
        contact_name = request.POST.get('name')
        contact_email = request.POST.get('email')
        contact_message = request.POST.get('msg')

        if contact_name != '' or contact_email != '' or contact_message != '':
            write_data = Contacts(
                name = contact_name,
                email = contact_email,
                message = contact_message,
            )

            write_data.save()
            send_confirmation = 'Your message has been received. Thank you for contact us.'

        else:
            send_confirmation = 'All fields are required.'

    return redirect('contact')

# Contact Form List
def contactform_list(request):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    contacts = Contacts.objects.all().order_by('readstatus', '-date')
    unread_contacts = Contacts.objects.filter(readstatus=False).count()

    return render(request, 'contactform_list.html', {
        'site_name':site_name + ' | Contacts',
        'user_name':request.user.username,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'contacts':contacts,
        'unread_contacts':unread_contacts,
        'activeuser':Usermanager.objects.filter(username=request.user.username)
        })


# Change Read Status
def change_readstatus(request, pk):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    read_status = Contacts.objects.get(pk=pk).readstatus
    write_data = Contacts.objects.get(pk=pk)

    if read_status == False:
        write_data.readstatus = True

        write_data.save()

    else:
        write_data.readstatus = False

        write_data.save()

    return redirect('contactform_list')


# Delete Contact Form
def contactform_delete(request, pk):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    delete_data = Contacts.objects.get(pk=pk)
    delete_data.delete()

    return redirect('contactform_list')