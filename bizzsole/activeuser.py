from django.contrib.auth.models import User, Group, Permission
from usermanager.models import Usermanager

class ActiveUser:
    def __init__(self):
        username = ''

    def get_userinfo(self, request):
        user = User.objects.get(username=request.user.username)
        usermanager = Usermanager.objects.get(username=user.username)

        self.username = user.username
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.user_email = user.email
        self.user_contact = usermanager.user_contact
        self.user_biography = usermanager.user_biography
        self.user_address = usermanager.user_address
        self.user_doj = usermanager.user_doj
        self.user_image = usermanager.user_image
        self.user_status = usermanager.user_status
        self.user_post = usermanager.user_posts

        self.group = []
        for i in user.groups.all():
            self.group.append(i.name)

# active_user = ActiveUser()
# active_user.get_userinfo()

# username = active_user.username
# user_firstname = active_user.first_name
# user_lastname = active_user.last_name
# user_email = active_user.user_email
# user_contact = active_user.user_contact
# user_biography = active_user.user_biography
# user_address = active_user.user_address
# user_doj = active_user.user_doj
# user_image = active_user.user_image
# user_status = active_user.user_status
# user_post = active_user.user_post
# user_group = active_user.group