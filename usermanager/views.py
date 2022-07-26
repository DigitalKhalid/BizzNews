from django.shortcuts import render, redirect
from .models import Usermanager
from django.contrib.auth.models import User, Group, Permission
from bizzsole.siteinfo import site_logo, site_icon, site_name
from bizzsole.bizzfunc import error, access_permission
from django.contrib.contenttypes.models import ContentType

site_name = site_name + ' | Users'

# List of Users
def user_list(request):
    # Permission Check
    permission = access_permission(request)
    if permission == -1:
        return redirect('mylogin')

    if permission == 0:
        error_message = 'Access Denied. You have not enough permissions to visit this section. For more information, please contact administrator.'
        return error(request, error_message)
    # End Permission Check

    usermanager = Usermanager.objects.all()

    return render(request, 'user_list.html',{
        'usermanager':usermanager,
        'user_name':request.user.username,
        'site_name':site_name,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'activeuser':Usermanager.objects.filter(username=request.user.username)
    })


# Edit Users
def user_edit(request, pk):
    # Permission Check
    permission = access_permission(request)
    if permission == -1:
        return redirect('mylogin')

    if permission == 0:
        error_message = 'Access Denied. You have not enough permissions to visit this section. For more information, please contact administrator.'
        return error(request, error_message)
    # End Permission Check

    if request.method == 'POST':
        error_message = ''
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


# Save User Information
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

# Delete User
def user_delete(request, pk):
    # Permission Check
    permission = access_permission(request)
    if permission == -1:
        return redirect('mylogin')

    if permission == 0:
        error_message = 'Access Denied. You have not enough permissions to visit this section. For more information, please contact administrator.'
        return error(request, error_message)
    # End Permission Check

    usermanager = Usermanager.objects.get(pk=pk)
    user = User.objects.filter(username=usermanager.username)
    
    usermanager.delete()
    user.delete()

    return redirect('user_list')

# Groups
def user_group(request):
    # Permission Check
    permission = access_permission(request)
    if permission == -1:
        return redirect('mylogin')

    if permission == 0:
        error_message = 'Access Denied. You have not enough permissions to visit this section. For more information, please contact administrator.'
        return error(request, error_message)
    # End Permission Check

    group = Group.objects.all().exclude(pk=1)

    return render(request, 'user_group.html',{
        'group':group,
        'user_name':request.user.username,
        'site_name':site_name,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'activeuser':Usermanager.objects.filter(username=request.user.username),
    })

# Add Groups
def user_group_add(request):
    # Permission Check
    permission = access_permission(request)
    if permission == -1:
        return redirect('mylogin')

    if permission == 0:
        error_message = 'Access Denied. You have not enough permissions to visit this section. For more information, please contact administrator.'
        return error(request, error_message)
    # End Permission Check

    if request.method == 'POST':
        group_name = request.POST.get('group_name')

        if group_name != '':
            if len(Group.objects.filter(name=group_name)) == 0:
                write_data = Group(
                    name = group_name
                    )

                write_data.save()
            
            else:
                error_message = 'Group name already exist.'
                return error(request, error_message)

        else:
            error_message = 'You have not entered a group name.'
            return error(request, error_message)

    return redirect('user_group')


# Delete Group
def user_group_delete(request, pk):
    # Permission Check
    permission = access_permission(request)
    if permission == -1:
        return redirect('mylogin')

    if permission == 0:
        error_message = 'Access Denied. You have not enough permissions to visit this section. For more information, please contact administrator.'
        return error(request, error_message)
    # End Permission Check

    usergroup = Group.objects.get(pk=pk)
    usergroup.delete()

    return redirect('user_group')


# Edit Groups
def user_group_edit(request, pk):
    # Permission Check
    permission = access_permission(request)
    if permission == -1:
        return redirect('mylogin')

    if permission == 0:
        error_message = 'Access Denied. You have not enough permissions to visit this section. For more information, please contact administrator.'
        return error(request, error_message)
    # End Permission Check

    group = Group.objects.get(pk=pk)

    if request.method == 'POST':
        groupname = request.POST.get('group_name')
        write_data = Group.objects.get(pk=pk)
        write_data.name = groupname

        write_data.save()

        return redirect('user_group')

    return render(request, 'user_groupedit.html',{
        'user_name':request.user.username,
        'site_name':site_name,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'activeuser':Usermanager.objects.filter(username=request.user.username),
        'group':group,
    })


# Assign groups to users
def user_addgroup(request, pk):
    # Permission Check
    permission = access_permission(request)
    if permission == -1:
        return redirect('mylogin')

    if permission == 0:
        error_message = 'Access Denied. You have not enough permissions to visit this section. For more information, please contact administrator.'
        return error(request, error_message)
    # End Permission Check

    if request.method == 'POST':
        groupname = request.POST.get('group_name')

        usermanager = Usermanager.objects.get(pk=pk)
        users = User.objects.get(username=usermanager.username)
        group = Group.objects.get(name=groupname)

        users.groups.add(group)

    usermanager = Usermanager.objects.get(pk=pk)
    users = User.objects.get(username=usermanager.username)

    group = []
    for i in users.groups.all().order_by('name') :
        group.append(i.name)


    grouplist = Group.objects.all().order_by('name')
    
    groupl = []
    for i in grouplist:
        groupl.append(i.name)

    grouplist = list(set(groupl).symmetric_difference(set(group)))

    return render(request, 'user_addgroup.html',{
        'user_name':request.user.username,
        'site_name':site_name,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'activeuser':Usermanager.objects.filter(username=request.user.username),
        'group':group,
        'grouplist':grouplist,
        'usermanager':usermanager,
    })

# Remove Groups from Users
def user_deletegroup(request, pk, groupname):
    # Permission Check
    permission = access_permission(request)
    if permission == -1:
        return redirect('mylogin')

    if permission == 0:
        error_message = 'Access Denied. You have not enough permissions to visit this section. For more information, please contact administrator.'
        return error(request, error_message)
    # End Permission Check

    usermanager = Usermanager.objects.get(pk=pk)
    users = User.objects.get(username=usermanager.username)
    group = Group.objects.get(name=groupname)

    users.groups.remove(group)
    return redirect('user_addgroup', pk=pk)



# Permissions
# Permission List
def permissions_list(request):
    # Permission Check
    permission = access_permission(request)
    if permission == -1:
        return redirect('mylogin')

    if permission == 0:
        error_message = 'Access Denied. You have not enough permissions to visit this section. For more information, please contact administrator.'
        return error(request, error_message)
    # End Permission Check

    permissions = Permission.objects.all()

    return render(request, 'permissions_list.html',{
        'permissions':permissions,
        'user_name':request.user.username,
        'site_name':site_name,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'activeuser':Usermanager.objects.filter(username=request.user.username),
    })


# Add Permissions
def permissions_add(request):
    # Permission Check
    permission = access_permission(request)
    if permission == -1:
        return redirect('mylogin')

    if permission == 0:
        error_message = 'Access Denied. You have not enough permissions to visit this section. For more information, please contact administrator.'
        return error(request, error_message)
    # End Permission Check

    if request.method == 'POST':
        permission_name = request.POST.get('permission_name')
        permission_codename = request.POST.get('permission_codename')

        if permission_name != '' and permission_codename != '':
            if len(Permission.objects.filter(name=permission_name)) == 0 and len(Permission.objects.filter(codename=permission_codename)) == 0:
                content_type = ContentType.objects.get(app_label='main', model='main')
                write_permission = Permission.objects.create(
                    name = permission_name,
                    content_type = content_type,
                    codename = permission_codename
                    )
            
                write_permission.save()

            else:
                error_message = 'Permission name already exist.'
                return error(request, error_message)

        else:
            error_message = 'You are missing some data. Please fill out all fields.'
            return error(request, error_message)

    return redirect('permission_list')


# Delete Permission
def permissions_delete(request, pk):
    # Permission Check
    permission = access_permission(request)
    if permission == -1:
        return redirect('mylogin')

    if permission == 0:
        error_message = 'Access Denied. You have not enough permissions to visit this section. For more information, please contact administrator.'
        return error(request, error_message)
    # End Permission Check

    permissions = Permission.objects.get(pk=pk)
    permissions.delete()

    return redirect('permissions_list')


# Edit Permissions
def permissions_edit(request, pk):
    # Permission Check
    permission = access_permission(request)
    if permission == -1:
        return redirect('mylogin')

    if permission == 0:
        error_message = 'Access Denied. You have not enough permissions to visit this section. For more information, please contact administrator.'
        return error(request, error_message)
    # End Permission Check

    permissions = Permission.objects.get(pk=pk)

    if request.method == 'POST':
        permission_name = request.POST.get('permission_name')
        permission_codename = request.POST.get('permission_codename')

        if permission_name != '' and permission_codename != '':
            if len(Permission.objects.filter(name=permission_name)) == 0 and len(Permission.objects.filter(codename=permission_codename)) == 0:
                write_data = Permission.objects.get(pk=pk)
                write_data.name = permission_name
                write_data.codename = permission_codename

                write_data.save()
                return redirect('permissions_list')

            else:
                error_message = 'Permission name already exist.'
                return error(request, error_message)

        else:
            error_message = 'You are missing some data. Please fill out all fields.'
            return error(request, error_message)

    return render(request, 'permissions_edit.html',{
        'user_name':request.user.username,
        'site_name':site_name,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'activeuser':Usermanager.objects.filter(username=request.user.username),
        'permissions':permissions,
    })


# Assign permissions to users
def user_addpermission(request, pk):
    # Permission Check
    permission = access_permission(request)
    if permission == -1:
        return redirect('mylogin')

    if permission == 0:
        error_message = 'Access Denied. You have not enough permissions to visit this section. For more information, please contact administrator.'
        return error(request, error_message)
    # End Permission Check

    if request.method == 'POST':
        permission_name = request.POST.get('permission_name')

        usermanager = Usermanager.objects.get(pk=pk)
        users = User.objects.get(username=usermanager.username)
        print(users)
        permission = Permission.objects.get(name=permission_name)

        users.user_permissions.add(permission)

    usermanager = Usermanager.objects.get(pk=pk)
    users = User.objects.get(username=usermanager.username)
    permissions = Permission.objects.filter(user=users)

    user_permissions = []
    for i in permissions :
        user_permissions.append(i.name)

    permissionlist = Permission.objects.all().order_by('content_type')
    
    permissionl = []
    for i in permissionlist:
        permissionl.append(i.name)

    permissionlist = list(set(permissionl).symmetric_difference(set(user_permissions)))

    return render(request, 'user_addpermissions.html',{
        'user_name':request.user.username,
        'site_name':site_name,
        'site_icon':site_icon,
        'site_logo':site_logo,
        'activeuser':Usermanager.objects.filter(username=request.user.username),
        'user_permissions':user_permissions,
        'permissionlist':permissionlist,
        'usermanager':usermanager,
    })

# Remove Permission from Users
def user_deletepermission(request, pk, permissionname):
    # Permission Check
    permission = access_permission(request)
    if permission == -1:
        return redirect('mylogin')

    if permission == 0:
        error_message = 'Access Denied. You have not enough permissions to visit this section. For more information, please contact administrator.'
        return error(request, error_message)
    # End Permission Check

    usermanager = Usermanager.objects.get(pk=pk)
    users = User.objects.get(username=usermanager.username)
    permission = Permission.objects.get(name=permissionname)

    users.user_permissions.remove(permission)
    return redirect('user_addpermission', pk=pk)