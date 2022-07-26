from django.shortcuts import render, redirect
from .models import Main
from news.models import News
from catagory.models import Catagory
from subcatagory.models import Subcatagory
from django.contrib.auth import authenticate, login, models
import os
from contactform.models import Contacts
from usermanager.models import Usermanager
from bizzsole.siteinfo import site_name, site_about, site_facebook, site_twiter, site_youtube, site_contact, site_email, site_address, site_icon, site_logo


# News
news = News.objects.all().order_by('-news_date')
catagory = Catagory.objects.all()
subcatagory = Subcatagory.objects.all()
latest_news = News.objects.all().order_by('-news_date')[:3]
latest_news2 = News.objects.all().order_by('-news_date')[:6]
popular_news = News.objects.all().order_by('-news_views')[:5]
unread_contacts = Contacts.objects.filter(readstatus=False).count()

# Get Active Catagory IDs
news_subcatagoryid = []
i = 0
for n in News.objects.all().order_by('news_catagoryid'):
    if i != n.news_catagoryid:
        news_subcatagoryid.append(n.news_catagoryid)
        i = n.news_catagoryid

active_catid = []
i = 0
for scat in Subcatagory.objects.all().order_by('catagoryid'):
    for subcat in news_subcatagoryid:
        if subcat == scat.pk and i != scat.catagoryid:
            active_catid.append(scat.catagoryid)
            i = scat.catagoryid

# Home
def home(request):
    return render(request, 'home.html', {
        'site_name':site_name + ' | Home', 
        'site_about':site_about, 
        'site_facebook':site_facebook, 
        'site_twiter':site_twiter, 
        'site_youtube':site_youtube,
        'site_email':site_email,
        'site_contact':site_contact,
        'site_address':site_address,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'news':news,
        'catagory':catagory,
        'active_catid':active_catid,
        'subcatagory':subcatagory,
        'latest_news':latest_news,
        'latest_news2':latest_news2,
        'popular_news':popular_news,
        }
    )

# About
def about(request):
    return render(request, 'about.html', {
        'site_name':site_name + ' | About', 
        'site_about':site_about, 
        'site_facebook':site_facebook, 
        'site_twiter':site_twiter, 
        'site_youtube':site_youtube,
        'site_email':site_email,
        'site_contact':site_contact,
        'site_address':site_address,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'news':news,
        'catagory':catagory,
        'active_catid':active_catid,
        'subcatagory':subcatagory,
        'popular_news':popular_news,
        }
    )

# Panel
def panel(request):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    user_name = request.user.username
    user_first_name = request.user.first_name
    user_last_name = request.user.last_name
    user_email = request.user.email
    user_full_name = user_first_name + ' ' + user_last_name

    return render(request, 'panel.html',{
        'site_name':site_name + ' | Dashboard', 
        'site_about':site_about, 
        'site_facebook':site_facebook, 
        'site_twiter':site_twiter, 
        'site_youtube':site_youtube,
        'site_email':site_email,
        'site_contact':site_contact,  
        'site_address':site_address,
        'site_icon':site_icon,
        'site_logo':site_logo,  
        'user_name':user_name,
        'user_first_name':user_first_name,
        'user_last_name':user_last_name,
        'user_email':user_email,
        'user_full_name':user_full_name,
        'unread_contacts':unread_contacts,
        'activeuser':Usermanager.objects.filter(username=request.user.username)
        })

# Login
def mylogin(request):
    global error_message
    error_message = ''
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('user_password')

        if user_name != '' or password != '':
            user = authenticate(username = user_name, password = password)

            if user != None:
                login(request, user)
                return redirect('panel')

            else:
                error_message = 'Incorrect user name or password.'
                return error_page(request, error_message)

        else:
            error_message = 'Incorrect user name or password.'
            return error_page(request, error_message)

    return render(request, 'login.html', {'site_name':site_name + ' | Login', 'site_icon':site_icon})

# Site Settings
def site_settings(request):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    global old_icon
    global old_logo

    old_icon = site_icon
    old_logo = site_logo

    if request.method == 'POST':
        save_settings(request)

        if error_message != '':
            return render(request, 'error.html',{'site_name':site_name + ' | Error', 'error':error_message})
        else:
            return redirect('panel')

    return render(request, 'site_settings.html', {
        'site_name':site_name + ' | Settings',
        'sitename':site_name,
        'site_about':site_about, 
        'site_facebook':site_facebook, 
        'site_twiter':site_twiter, 
        'site_youtube':site_youtube,
        'site_email':site_email,
        'site_contact':site_contact,
        'site_address':site_address,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'unread_contacts':unread_contacts,
        'user_name':request.user.username,
        'activeuser':Usermanager.objects.filter(username=request.user.username)
        }
    )

# save settings
def save_settings(request):
    global error_message
    error_message = ''

    sitename = request.POST.get('site_name')
    siteabout = request.POST.get('site_about')
    sitefacebook = request.POST.get('site_facebook')
    sitetwiter = request.POST.get('site_twiter')
    siteyoutube = request.POST.get('site_youtube')
    siteemail = request.POST.get('site_email')
    sitecontact = request.POST.get('site_contact')
    siteaddress = request.POST.get('site_address')
    siteicon = request.FILES.get('site_icon')
    sitelogo = request.FILES.get('site_logo')

    if sitename == '':
        error_message = 'Site name is required.'
        return error_message
    
    if sitefacebook == '':
        sitefacebook = '#'
    if sitetwiter == '':
        sitetwiter = '#'
    if siteyoutube == '':
        siteyoutube = '#'

    write_data =  Main.objects.get(pk=1)
    write_data.name = sitename
    write_data.about = siteabout
    write_data.facebook = sitefacebook
    write_data.twiter = sitetwiter
    write_data.youtube = siteyoutube
    write_data.email = siteemail
    write_data.contact = sitecontact
    write_data.address = siteaddress

    try:
        if str(siteicon.content_type).startswith('image'):
            if siteicon.size < 5000000:
                write_data.icon = siteicon
                os.remove(old_icon.path)
            else:
                error_message = 'Selected file size is not supported. You can only upload image less than 5 MB.'
                return error_message

        else:
            error_message = 'Selected file format is not supported. You can only select image file to proceed.'
            return error_message
    
    except:
        pass

    try:
        if str(sitelogo.content_type).startswith('image'):
            if sitelogo.size < 5000000:
                write_data.logo = sitelogo
                os.remove(old_logo.path)

            else:
                error_message = 'Selected file size is not supported. You can only upload image less than 5 MB.'
                return error_message

        else:
            error_message = 'Selected file format is not supported. You can only select image file to proceed.'
            return error_message
            
    except:
        pass

    write_data.save()

# Update User Settings & Password
def user_settings(request, username):
    if request.method == 'POST':
        useremail = request.POST.get('user_email')
        userfirstname = request.POST.get('user_first_name')
        userlastname = request.POST.get('user_last_name')
        userpassword = request.POST.get('user_password')
        userrepassword = request.POST.get('user_repassword')

        write_data = models.User.objects.get(username=username)
        write_data.email = useremail
        write_data.first_name = userfirstname 
        write_data.last_name = userlastname

        if userpassword != '':
            if userpassword == userrepassword:

                for i in userpassword:
                    strength = 0
                    if i > '0' and i < '9':
                        strength =+ 1
                    if i > 'A' and i < 'Z':
                        strength =+ 1
                    if i > 'a' and i < 'z':
                        strength =+ 1
                    if i > '!' and i < '(':
                        strength =+ 1

                if strength == 4:
                    print('Strong Password')
                elif strength == 3:
                    print('Moderate Password')
                else:
                    print('Week Password')

                write_data.set_password(userpassword)
            else:
                print('password does not match')
        
        write_data.save()

        return redirect('panel')
    
    return redirect('panel')

# Register New User
def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        useremail = request.POST.get('user_email')
        userfirstname = request.POST.get('user_firstname')
        userlastname = request.POST.get('user_lastname')
        userpassword = request.POST.get('user_password')
        userrepassword = request.POST.get('user_repassword')
        userterms = request.POST.get('user_terms')

        if userterms == 'on':
            if userpassword != '':
                if userpassword == userrepassword:
                    for i in userpassword:
                        strength = 0
                        if i > '0' and i < '9':
                            strength =+ 1
                        if i > 'A' and i < 'Z':
                            strength =+ 1
                        if i > 'a' and i < 'z':
                            strength =+ 1
                        if i > '!' and i < '(':
                            strength =+ 1

                    if strength == 4:
                        print('Strong Password')
                    elif strength == 3:
                        print('Moderate Password')
                    else:
                        print('Week Password')

                        available_users = models.User.objects.filter(username = username).count()
                        
                        if available_users > 0:
                            error_message = 'User name not available'
                            return error_page(request, error_message)
                        
                        else:
                            write_data = models.User.objects.create_user(
                                username = username,
                                email = useremail,
                                password = userpassword,
                                first_name = userfirstname,
                                last_name = userlastname,
                                )
                            
                            write_data.save()

                            write_Usermanager = Usermanager(
                                username = username,
                                user_firstname = userfirstname,
                                user_lastname = userlastname,
                                user_email = useremail,
                                )

                            write_Usermanager.save()
                            
                            return redirect('mylogin')

                else:
                    error_message = 'Password does not match. Please enter same password in both fields.'
                    return error_page(request, error_message)
        else:
            error_message = 'Please accept the terms.'
            return error_page(request, error_message)
                        
    
    return redirect('mylogin')

# Contact Form
def contact(request):
    return render(request, 'contact.html', {
        'site_name':site_name + ' | Contact', 
        'site_about':site_about, 
        'site_facebook':site_facebook, 
        'site_twiter':site_twiter, 
        'site_youtube':site_youtube,
        'site_email':site_email,
        'site_contact':site_contact,
        'site_address':site_address,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'news':news,
        'catagory':catagory,
        'active_catid':active_catid,
        'subcatagory':subcatagory,
        'popular_news':popular_news,
        })


def error_page(request, error_message):
        return render(request, 'error_front.html', {
        'site_name':site_name + ' | error', 
        'site_about':site_about, 
        'site_facebook':site_facebook, 
        'site_twiter':site_twiter, 
        'site_youtube':site_youtube,
        'site_email':site_email,
        'site_contact':site_contact,
        'site_address':site_address,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'news':news,
        'catagory':catagory,
        'active_catid':active_catid,
        'subcatagory':subcatagory,
        'latest_news':latest_news,
        'latest_news2':latest_news2,
        'popular_news':popular_news,
        'error_message':error_message,
        }
    )