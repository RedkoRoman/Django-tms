from django.urls import path

from feedback.views import FeedbackFormView, SuccessView, FibonacciView

app_name = 'feedback'

urlpatterns = [
    path('', FeedbackFormView.as_view(), name='feedback'),
    path('success/', SuccessView.as_view(), name='success'),
    path('fibonacci', FibonacciView.as_view(), name='fibonacci')
]