from django import forms
from django.core.exceptions import ValidationError # см. D4.5
from .models import Post


class PostForm(forms.ModelForm):    # TODO D4.4
    #description = forms.CharField(min_length=20)
    class Meta:
        model = Post
        fields = [
            'category',
            'header',
            'text',
        ]

#Для проверки корректности форм надо переопределить метод clean в форме TODO 4.4
#https://docs.djangoproject.com/en/4.0/ref/forms/api/#django.forms.Form.clean
#    def clean(self):
#        cleaned_data = super().clean()
#        description = cleaned_data.get("description")
#        name = cleaned_data.get("name")
#
#        if name == description:
#            raise ValidationError(
#                "Описание не должно быть идентично названию."
#            )
#
#        return cleaned_data
