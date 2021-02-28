from django.forms import models

from core.server.forms import FormNameMixin

class TagForm(FormNameMixin, models.ModelForm):
    pass


class ArticleForm(FormNameMixin, models.ModelForm):
    def clean_tags(self):
        """
        标签
        :return:
        """
        tags = self.data.getlist('tags')
        return tags

    def clean_ads(self):
        """
        广告
        :return:
        """
        ads = self.data.getlist('ads')
        return ads


class AdForm(FormNameMixin, models.ModelForm):
    pass
