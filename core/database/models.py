import json

from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.models import ModelMultipleChoiceField


class FilteredMultiSelectField(models.CharField):
    """
    过滤多选字段
    """

    def get_db_prep_save(self, value, connection):
        value = super(FilteredMultiSelectField, self).get_db_prep_save(value, connection)
        if isinstance(value, set):
            value = list(value)
        if value:
            return ','.join(str(x) for x in value)
        return ''

    def from_db_value(self, value, expression, connection, context):
        if value:
            return value.split(',')
        return []

    def to_python(self, value):
        if isinstance(value, list):
            return value
        return []

    def formfield(self, **kwargs):
        defaults = {'required': not self.blank,
                    'label': self.verbose_name,
                    'help_text': self.help_text,
                    'widget': FilteredSelectMultiple(self.verbose_name, False)}
        defaults.update(kwargs)
        return ModelMultipleChoiceField(**defaults)


class JsonTextField(models.TextField):
    """
    json字段
    还不是很完善, 慎用
    """

    def get_db_prep_save(self, value, connection):
        value = super(JsonTextField, self).get_db_prep_save(value, connection)
        if value:
            return json.dumps(value)
        return ''

    def to_python(self, value):
        return value

    def from_db_value(self, value, expression, connection, context):
        if value:
            return json.loads(value)
        return {}


##################    model_manager    ##################
class EnableManager(models.Manager):
    def get_queryset(self):
        return super(EnableManager, self).get_queryset().filter(enable=True)


##################    model    ##################
class BaseModel(models.Model):
    objects = EnableManager()

    enable = models.BooleanField('是否有效', default=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super(BaseModel, self).save(*args, **kwargs)
