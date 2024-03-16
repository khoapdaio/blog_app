from django import forms

from Blog.models import Category


# Create your models here.
class PostSearchForm(forms.Form):
	category = forms.ModelChoiceField(queryset=Category.objects,label="Category")
	title = forms.CharField(label="Title",max_length=255)
	date = forms.DateField(label="Date")
