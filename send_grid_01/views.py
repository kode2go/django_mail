# emailsender/views.py

from django.core.mail import send_mail
from django.shortcuts import render
from .forms import EmailForm

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


sg = SendGridAPIClient('API_KEY')

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            message = Mail(
            from_email='xxx@gmail.com',
            to_emails = form.cleaned_data['to_email'],
            subject = form.cleaned_data['subject'],
            html_content = form.cleaned_data['message'])

            try:
                response = sg.send(message)
                return render(request, 'emailsender/success.html')
            except Exception as e:
                return render(request, 'emailsender/error.html', {'error_message': str(e)})
    else:
        form = EmailForm()

    return render(request, 'emailsender/send_email.html', {'form': form})
