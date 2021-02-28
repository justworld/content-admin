from django.db import models
from django import forms
from django.core import validators
from django.forms import ValidationError
from django.utils.translation import ugettext_lazy as _

class FormNameMixin:
    def clean_name(self):
        """
        校验名称
        :return:
        """
        name = self.cleaned_data['name']
        id = self.instance.id
        queryset = self.Meta.model.objects.filter(name=name)
        if id:
            queryset = queryset.exclude(id=id)
        if queryset.exists():
            raise ValidationError('名称重复')

        return name


class FormCodeMixin:
    def clean_code(self):
        """
        校验标识
        :return:
        """
        code = self.cleaned_data['code']
        id = self.instance.id
        queryset = self.Meta.model.objects.filter(code=code)
        if id:
            queryset = queryset.exclude(id=id)
        if queryset.exists():
            raise ValidationError('标识重复')

        return code