from django import forms
from django.core.exceptions import ValidationError # см. D4.5
from .models import Post, Author, Category


class PostForm(forms.ModelForm):    # forms.ModelForm для быстрой генерации форм из моделей, см. D4.3, D4.4
# Для сокрытия форм, и передачи данных: https://stackoverflow.com/questions/15795869/django-modelform-to-have-a-hidden-input

#    type = forms.ChoiceField(label='hidden', initial='NS') # Форма создаётся, данные не передаются
#    post_author = forms.ModelChoiceField(label='post_author', queryset=Author.objects.all())   # , required=True
#    category = forms.ModelMultipleChoiceField(label='Category', queryset=Category.objects.all(),)
#    header = forms.CharField(label='header')
#    text = forms.CharField(label='text', widget=forms.Textarea) #  Форма создаётся, данные не передаются
    class Meta:     # Через Meta указываются поля для такой генерации
        model = Post
        fields = [
            'type',
            'post_author',
            'category',
            'header',
            'text',
        ]
        widgets = {'type': forms.HiddenInput, # К сожалению, поле совсем исчезает из генерации, а не становится скрытым
                   'post_author': forms.HiddenInput,
                   }

# Попытка присвоить начальные значения полям
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].initial = 'NS'

# if you want to use a CreateView, you must use a ModelForm
#class PostForm(forms.Form): # При наследовании от forms.Form все поля создаются вручную
    # Для посылки не показываемых данных чероз POST используется
    # forms.HiddenInput - генерит скрытое поле <input type="hidden">
    # description = forms.CharField(min_length=20)
    #quantity = forms.IntegerField(label='Quantity')
    # price = forms.FloatField(label='Price')
    #category = forms.ModelChoiceField(label='Category', queryset=Category.objects.all(),)
#    type = forms.ChoiceField(label='type', choices=Post.POST_TYPE, initial='NS')#
#    post_author = forms.ModelChoiceField(label='post_author', queryset=Author.objects.all(), required=True)
#    category = forms.ModelMultipleChoiceField(label='Category', queryset=Category.objects.all(),)
#    header = forms.CharField(label='header')
#    text = forms.CharField(label='text', widget=forms.Textarea)



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
