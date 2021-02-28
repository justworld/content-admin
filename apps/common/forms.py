import json

from django.forms import ValidationError, models

from core.server.forms import FormCodeMixin


class ConfigForm(FormCodeMixin, models.ModelForm):
    def clean_data(self):
        """
        校验data
        :return:
        """
        data = self.cleaned_data['data']
        if data:
            try:
                data = json.loads(data.replace('\'', '"'))
            except Exception:
                raise ValidationError('不是正确的json格式')

        return data
