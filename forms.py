from django import forms
from models import Page
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

class PageForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget() )

    class Meta:
        model   = Page
        fields  = ['url','title','content','published','access','template']
        widgets = { 'url': forms.TextInput(attrs={'class': 'field px2'}),
                    'title': forms.TextInput(attrs={'class': 'field px2'}),
                    'access': forms.Select(attrs={'class': 'field px2'}),
                    'template': forms.Select(attrs={'class': 'field px2'})
                   }

