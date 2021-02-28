from django.contrib import admin
from django.conf.urls import url
from django.http.response import JsonResponse

from core.database.models import FilteredMultiSelectField


class BaseModelAdmin(admin.ModelAdmin):
    # 分页显示，一页的数量
    list_per_page = 10
    actions_on_top = True
    soft_delete = True
    list_select_related = False
    sortable_by = ('id', 'update_time', 'create_time')
    exclude = ('enable', 'create_time', 'update_time')

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if isinstance(db_field, FilteredMultiSelectField):
            # 必须定义获取该字段数据的方法, 方法返回queryset对象, 格式get_+字段名
            queryset_call = getattr(self, 'get_select_{}'.format(db_field.name))
            kwargs['queryset'] = queryset_call(db_field, request, **kwargs)
            return db_field.formfield(**kwargs)
        else:
            form_field = super(BaseModelAdmin, self).formfield_for_dbfield(db_field, request, **kwargs)
            return form_field

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Get a form Field for a ForeignKey.
        """
        queryset_call = getattr(self, 'get_select_{}'.format(db_field.name), None)
        if queryset_call:
            kwargs['queryset'] = queryset_call(db_field, request, **kwargs)

        return super(BaseModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # ÌíŒÓÅúÁ¿ÔöŒÓ¡¢ÅúÁ¿±àŒ­µÈ¶îÍâµÄurl
    def get_urls(self):
        urls = super(BaseModelAdmin, self).get_urls()
        if hasattr(self, 'change_online'):
            urls = [url(r'^change_online/$', self.admin_site.admin_view(self.change_online),
                        name='change_online')] + urls
        if hasattr(self, 'change_offline'):
            urls = [url(r'^change_offline/$', self.admin_site.admin_view(self.change_offline),
                        name='change_offline')] + urls

        return urls

    def _change_online(self, request, online, attr_name='online'):
        """
        ÉÏÏßÏÂÏß
        :param request:
        :return:
        """
        if request.method == 'POST':
            selected_ids = request.POST.get('selected_ids')
            selected_ids = selected_ids.split(',')
            if selected_ids:
                self.model.objects.filter(id__in=selected_ids).update(**{attr_name: online})
                return JsonResponse({'msg': '更新成功'})

            return JsonResponse({'msg': '没有数据更新'})

    def _can_delete(self, request, obj):
        """
        ¶ÔÏóÊÇ·ñ¿ÉÉŸ³ý
        :param request:
        :param obj:
        :return:
        """
        return True

    def delete_model(self, request, obj):
        """
        Given a model instance delete it from the database.
        """
        if self._can_delete(request, obj):
            if self.soft_delete:
                obj.enable = False
                obj.save()
            else:
                obj.delete()

    def delete_queryset(self, request, queryset):
        """
        Given a queryset, delete it from the database.
        """
        if self.soft_delete:
            queryset.update(enable=False)
        else:
            queryset.delete()
