# emailsender/forms.py

from django import forms

class EmailForm(forms.Form):
    to_email = forms.EmailField(label='To Email')
    subject = forms.CharField(max_length=100, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')
