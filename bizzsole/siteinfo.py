from django import template
from main.models import Main

class SiteInfo:
    def __init__(self):
        site_name = ''
        site_about = ''

    def get_siteinfo(self):
        site = Main.objects.get(pk=1)
        self.site_name = site.name
        self.site_about = site.about
        self.facebook = site.facebook
        self.twiter = site.twiter
        self.youtube = site.youtube
        self.email = site.email
        self.contact = site.contact
        self.address = site.address
        self.icon = site.icon
        self.logo = site.logo

site_info = SiteInfo()
site_info.get_siteinfo()

site_name = site_info.site_name
site_about = site_info.site_about
site_facebook = site_info.facebook
site_twiter = site_info.twiter
site_youtube = site_info.youtube
site_email = site_info.email
site_contact = site_info.contact
site_address = site_info.address
site_icon = site_info.icon
site_logo = site_info.logo