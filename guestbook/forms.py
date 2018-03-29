from django import forms

class CommentForm(forms.Form):
	name = forms.CharField(max_length=100, 
		widget=forms.TextInput(attrs={'class':'form-control','placeholder' : 'Title of BookMark'}))
	comment = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Link and description of BookMark'}))