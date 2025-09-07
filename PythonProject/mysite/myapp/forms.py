from django import forms
from django.forms.widgets import ChoiceWidget

from .models import ShavarmaStore, Food, Ingredients
from django_select2 import forms as s2forms

class IngredientsWindget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ['name__icontains']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs.setdefault('data-minimum-input-length', 0)

class AddShavarmaStoreForm(forms.ModelForm):
    rating = forms.IntegerField(min_value=0, max_value=5, label="Оценка")
    logo = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = ShavarmaStore
        fields = '__all__'
        labels = {
            'network': 'Сетевое ли заведение'
        }

class AddFoodForm(forms.ModelForm):
    shavarma_store = forms.ModelChoiceField(
        queryset=ShavarmaStore.objects.all(),
        empty_label=None,
        label="Шаурмечная",
        widget=forms.Select(attrs={'class': 'shawarma_store_input'})
    )
    rating = forms.IntegerField(min_value=0, max_value=5, label="Оценка")
    class Meta:
        model = Food
        fields = '__all__'
        widgets = {
            'ingredients': IngredientsWindget(
                model=Ingredients,
                attrs={
                    'class': 'ingredients-windget',
                }
            ),
        }
        labels = {
            'ingredients': 'Ингредиенты'
        }

    def __init__(self, *args, **kwargs):
        self.store = kwargs.pop('store', None)
        super().__init__(*args, **kwargs)
        if self.store:
            self.fields['shavarma_store'].queryset = ShavarmaStore.objects.filter(pk=self.store)


class CloudForm(forms.Form):
    file = forms.FileField(label="Файл")