from django import forms
from .models import News
import re
from django.forms import ValidationError
# связанная с моделью форма
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    # кастомный валидатор который проверяет заголовок на наличие цифры в начале

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title


"""
форма не связанная с моделью 

class NewsForm(forms.Form):
    title = forms.CharField(label='Заголовок',widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}),label='Контент')
    image = forms.ImageField(label='Изображение')
    is_published = forms.BooleanField(label='Опубликовать', initial=True)
    category = forms.ModelChoiceField(Category.objects,label='Категория')
"""