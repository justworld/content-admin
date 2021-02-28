from django.contrib import admin

from core.server.admins import BaseModelAdmin
from .models import Tag, Article, Ad

from .forms import TagForm, ArticleForm, AdForm


@admin.register(Tag)
class TagAdmin(BaseModelAdmin):
    list_display = ('id', 'name', 'online', 'create_time', 'update_time')
    exclude = BaseModelAdmin.exclude + ('online',)
    search_fields = ('name',)
    # 增加自定义按钮
    actions = ['change_online', 'change_offline']
    form = TagForm

    def change_online(self, request):
        return self._change_online(request, True)

    change_online.url = '/admin/content/tag/change_online/'

    def change_offline(self, request):
        return self._change_online(request, False)

    change_offline.url = '/admin/content/tag/change_offline/'


@admin.register(Article)
class ArticleAdmin(BaseModelAdmin):
    list_display = (
    'id', 'title', 'desc', 'cover', 'online', 'top', 'read_num', 'like_num', 'create_time', 'update_time')
    exclude = BaseModelAdmin.exclude + ('online', 'read_num', 'like_num')
    search_fields = ('title',)
    form = ArticleForm

    def get_select_tags(self, *args, **kwargs):
        """
        获取可选的标签数据
        :return queryset
        """
        return Tag.objects.all()

    def get_select_ads(self, *args, **kwargs):
        """
        获取可选的广告数据
        :return queryset
        """
        return Ad.objects.all()

    def change_online(self, request):
        return self._change_online(request, True)

    change_online.url = '/admin/content/article/change_online/'

    def change_offline(self, request):
        return self._change_online(request, False)

    change_offline.url = '/admin/content/article/change_offline/'


@admin.register(Ad)
class AdAdmin(BaseModelAdmin):
    list_display = ('id', 'name', 'cover', 'link', 'create_time', 'update_time')
    exclude = BaseModelAdmin.exclude + ('online',)
    search_fields = ('name',)
    form = AdForm

    def change_online(self, request):
        return self._change_online(request, True)

    change_online.url = '/admin/content/ad/change_online/'

    def change_offline(self, request):
        return self._change_online(request, False)

    change_offline.url = '/admin/content/ad/change_offline/'
