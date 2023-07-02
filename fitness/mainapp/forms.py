from django import forms
from .models import Category
from .models import Part_of_the_body


class CategoryForm(forms.ModelForm):

    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))

    approaches = forms.IntegerField(initial=50, widget=forms.NumberInput(
        attrs={
            'placeholder': 'максимальное колличество подходов',
            'class': 'form-control'
        }
    ))

    part_of_the_body = forms.ModelMultipleChoiceField(queryset=Part_of_the_body.objects.all(), widget=forms.CheckboxSelectMultiple(
        # attrs={'class': "form-check-input"}
    ))

    class Meta:
        model = Category
        # fields = '__all__'
        # fields = ('name', 'foods')
        exclude = ('is_active',)