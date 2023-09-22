from django import forms
from django.forms import BaseInlineFormSet

from catalog.models import Product, Version


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form_control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


    def clean_product_name(self):
        cleaned_data = self.cleaned_data.get('product_name')
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in words:
            if word in cleaned_data:
                raise forms.ValidationError('Недопустимое название продукта')
            return cleaned_data

    def clean_descriptions(self):
        cleaned_data = self.cleaned_data.get('descriptions')
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in words:
            if word in cleaned_data:
                raise forms.ValidationError('Недопустимое описание продукта')
            return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class VersionBaseInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        active_list = [form.cleaned_data['is_active'] for form in self.forms if 'is_active' in form.cleaned_data]
        if active_list.count(True) > 1:
            raise forms.ValidationError("У товара уже есть активная версия,вы не можете выбрать более одной активной версии.")
