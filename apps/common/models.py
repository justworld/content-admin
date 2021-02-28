from django.db import models

from core.database.models import JsonTextField, BaseModel


class Config(BaseModel):
    _database = 'content'

    code = models.CharField('标识', max_length=20)
    data = JsonTextField('配置')

    class Meta:
        db_table = 'config'
        verbose_name = "config"
        verbose_name_plural = "配置管理"
        app_label = 'common'

    def __str__(self):
        return self.code
