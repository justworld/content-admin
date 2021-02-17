from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf import settings

admin.autodiscover()
admin.site.site_title = '管理后台'
admin.site.site_header = '管理后台'

urlpatterns = [
    path('{}/'.format(settings.ADMIN_PATH), admin.site.urls)
]
