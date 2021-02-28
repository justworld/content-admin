from django.db import models

from core.database.models import FilteredMultiSelectField, BaseModel


class Tag(BaseModel):
    _database = 'content'

    name = models.CharField('标签名', max_length=20)
    online = models.BooleanField('是否上线', default=False)

    class Meta:
        db_table = 'tag'
        verbose_name = "Tag"
        verbose_name_plural = "标签管理"
        app_label = 'content'

    def __str__(self):
        return self.name


class Article(BaseModel):
    _database = 'content'

    title = models.CharField('标题', max_length=50)
    desc = models.CharField('描述', max_length=100)
    html_content = models.TextField('内容')
    cover = models.CharField('封面', max_length=255)
    tags = FilteredMultiSelectField('所属标签', max_length=100)
    ads = FilteredMultiSelectField('所属广告', max_length=100)
    top = models.BooleanField('是否置顶', default=False)
    online = models.BooleanField('是否上线', default=False)
    read_num = models.IntegerField('阅读数', default=0)
    like_num = models.IntegerField('点赞数', default=0)

    class Meta:
        db_table = 'article'
        verbose_name = "article"
        verbose_name_plural = "文章管理"
        app_label = 'content'

    def __str__(self):
        return self.title


class Ad(BaseModel):
    _database = 'content'

    name = models.CharField('标题', max_length=20)
    cover = models.CharField('封面', max_length=255)
    link = models.CharField('地址', max_length=255)
    online = models.BooleanField('是否上线', default=False)

    class Meta:
        db_table = 'ad'
        verbose_name = "ad"
        verbose_name_plural = "广告管理"
        app_label = 'content'

    def __str__(self):
        return self.name
