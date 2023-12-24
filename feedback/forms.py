from time import sleep

from django import forms
from django.conf import settings
from django.core.mail import send_mail

from feedback.tasks import send_email_task


class FeedbackForm(forms.Form):
    email = forms.EmailField(label='Email Address')
    message = forms.CharField(
        label='Message', widget=forms.Textarea(attrs={'rows': 5})
    )

    def send_email(self):
        # sleep(20)
        # send_mail(
        #     subject='Your feedback',
        #     message=f'{self.cleaned_data["message"]}\n\nThank You!',
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     recipient_list=[self.cleaned_data['email']],
        #     fail_silently=False
        # )
        send_email_task.delay(email=self.cleaned_data['email'], message=self.cleaned_data['message'])


class FibonacciForm(forms.Form):
    n = forms.IntegerField(label='Enter the Fibonacci number')