from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from feedback.forms import FeedbackForm, FibonacciForm
from feedback.tasks import fibonacci_task


class FeedbackFormView(FormView):
    template_name = 'feedback/feedback.html'
    form_class = FeedbackForm
    success_url = 'success/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form=form)


class SuccessView(TemplateView):
    template_name = 'feedback/success.html'


class FibonacciView(FormView):
    template_name = 'feedback/fibonacci.html'
    form_class = FibonacciForm
    success_url = 'success/'

    def form_valid(self, form):
        n = form.cleaned_data['n']
        result = fibonacci_task.delay(n)
        return HttpResponse(f"Task ID: {result.id} started for Fibonacci({n}). Check Celery logs for the result.")