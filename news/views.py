import imp
from django.shortcuts import render, get_object_or_404, redirect
from catagory.models import Catagory
from news.models import News
from main.views import site_name, site_about, site_contact, site_facebook, site_email, site_twiter, site_youtube, site_address, site_icon, site_logo
import os
from django.contrib import messages
from subcatagory.models import Subcatagory
from bizzsupport import error
from contactform.models import Contacts
from usermanager.models import Usermanager

site_name = site_name + ' | News'
news = News.objects.all
subcatagory = Subcatagory.objects.all
catagory = Catagory.objects.all
unread_contacts = Contacts.objects.filter(readstatus=False).count()

# News Detail
def news_detail(request, pk):
    news_detail = News.objects.filter(pk = pk)
    popular_news = News.objects.all().order_by('-news_views')[:5]

    newstags = News.objects.get(pk = pk).news_tags
    tags = newstags.split(',')

    # Get Views
    try:
        views = News.objects.get(pk=pk)
        views.news_views = views.news_views + 1
        views.save()

    except:
        pass
    # End Get Views

    return render(request, 'news_detail.html', {
        'news':news,
        'news_detail':news_detail,
        'site_name':site_name,
        'site_about':site_about, 
        'site_facebook':site_facebook, 
        'site_twiter':site_twiter, 
        'site_youtube':site_youtube,
        'site_email':site_email,
        'site_contact':site_contact,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'user_name':request.user.username,
        'catagory':catagory,
        'subcatagory':subcatagory,
        'popular_news':popular_news,
        'tags':tags,
        'activeuser':Usermanager.objects.filter(username=request.user.username)
        })

# News List
def news_list(request):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    return render(request, 'news_list.html',{
        'site_name':site_name, 
        'news' : news, 
        'catagory':catagory, 
        'subcatagory':subcatagory,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'unread_contacts':unread_contacts,
        'user_name':request.user.username,
        'activeuser':Usermanager.objects.filter(username=request.user.username)
        })

# Add News
def add_news(request):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    if request.method == 'POST':
        save_news(request, 'new', 1)

        if error_message != '':
            return error(request, error_message)
        else:
            return redirect('news_list')
    
    return render(request, 'news_add.html',{
        'site_name':site_name, 
        'catagory':catagory, 
        'subcatagory':subcatagory,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'unread_contacts':unread_contacts,
        'user_name':request.user.username,
        'activeuser':Usermanager.objects.filter(username=request.user.username)
        })

# Delete News
def delete_news(request, pk):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    delete_data = News.objects.get(pk=pk)
    
    if len(delete_data.news_image) > 0:
        os.remove(delete_data.news_image.path)
    
    delete_data.delete()
    messages.success(request, 'News deleted successfully.')

    return redirect('news_list')

# Edit News
def edit_news(request, pk):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End
    
    global old_image
    news = News.objects.get(pk=pk)

    # Date Makeup
    if len(str(news.news_date.day)) == 1:
        news_day = '0' + str(news.news_date.day)
    else:
        news_day = str(news.news_date.day)

    if len(str(news.news_date.month)) == 1:
        news_month = '0' + str(news.news_date.month)
    else:
        news_month = str(news.news_date.month)

    news_date = str(news.news_date.year) + '-' + news_month + '-' + news_day

    catagory = Catagory.objects.all
    subcatagory = Subcatagory.objects.all

    if len(News.objects.filter(pk=pk)) == 0:
        return error(request,'Data not available')

    old_image = news.news_image

    if request.method == 'POST':
        save_news(request, 'edit', pk)

        if error_message != '':
            return error(request, error_message)
        else:
            return redirect('news_list')

    return render(request, 'news_edit.html', {
        'site_name':site_name, 
        'site_icon':site_icon,
        'site_logo':site_logo,
        'pk':pk, 
        'news':news, 
        'news_date':news_date, 
        'catagory':catagory, 
        'subcatagory':subcatagory,
        'unread_contacts':unread_contacts,
        'user_name':request.user.username,
        'activeuser':Usermanager.objects.filter(username=request.user.username)
        })

# Save News
def save_news(request, type='new' or 'edit', pk=None):
    global error_message
    error_message = ''

    news_title = request.POST.get('news_title')
    news_date = request.POST.get('news_date')
    news_writer = request.POST.get('news_writer')
    news_catagory = request.POST.get('news_catagory')
    news_summary = request.POST.get('news_summary')
    news_detail = request.POST.get('news_detail')
    news_image = request.FILES.get('news_image')
    news_tags = request.POST.get('news_tags')

    if news_title == '' or news_date == '' or news_writer == '' or news_catagory == '' or news_summary == ''  or news_detail == '' or news_image == '':
        error_message = 'You are missing some data. All fields are required.'
        return error_message

    else:
        if type == 'new':
            if str(news_image.content_type).startswith('image'):
                if news_image.size < 5000000:
                    write_data = News(
                        news_title = news_title, 
                        news_date = news_date,
                        news_writer = news_writer,
                        news_catagoryid = news_catagory,
                        news_summary = news_summary,
                        news_detail = news_detail,
                        news_image = news_image,
                        news_tags = news_tags)

                    write_data.save()
                    
                else:
                    error_message = 'Selected file size is not supported. You can only upload image less than 5 MB.'
                    return error_message

            else:
                error_message = 'Selected file format is not supported. You can only select image file to proceed.'
                return error_message

        elif type == 'edit':
                try:

                    if str(news_image.content_type).startswith('image'):
                        if news_image.size < 5000000:
                            write_data = News.objects.get(pk=pk)
                            write_data.news_title = news_title
                            write_data.news_date = news_date
                            write_data.news_writer = news_writer
                            write_data.news_catagoryid = news_catagory
                            write_data.news_summary = news_summary
                            write_data.news_detail = news_detail
                            write_data.news_image = news_image
                            write_data.news_tags = news_tags

                            write_data.save()
                            os.remove(old_image.path)
                            
                        else:
                            error_message = 'Selected file size is not supported. You can only upload image less than 5 MB.'
                            return error_message

                    else:
                        error_message = 'Selected file format is not supported. You can only select image file to proceed.'
                        return error_message

                except:
                    write_data = News.objects.get(pk=pk)
                    write_data.news_title = news_title
                    write_data.news_date = news_date
                    write_data.news_writer = news_writer
                    write_data.news_catagoryid = news_catagory
                    write_data.news_summary = news_summary
                    write_data.news_detail = news_detail
                    write_data.news_tags = news_tags

                    write_data.save()