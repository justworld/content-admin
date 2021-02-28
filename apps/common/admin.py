from django.contrib import admin

from core.server.admins import BaseModelAdmin
from .models import Config
from .forms import ConfigForm


@admin.register(Config)
class ConfigAdmin(BaseModelAdmin):
    list_display = ('id', 'code', 'data', 'create_time', 'update_time')
    search_fields = ('code',)
    form = ConfigForm
