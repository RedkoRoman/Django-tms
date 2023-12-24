from django.contrib.auth.models import UserManager as BaseUserManager

from authentication.tasks import send_activation_email_task


class UserManager(BaseUserManager):

    def create_user(self, username, email=None, password=None, **extra_fields):
        response = super().create_user(username, email, password, **extra_fields)
        send_activation_email_task.delay(email=email, message='Activate')

        # message_1 = (
        #     'Test',
        #     'Activate',
        #     settings.DEFAULT_FROM_EMAIL,
        #     [email, ],
        # )
        # message_2 = (
        #     'Test 2',
        #     'Activate 2',
        #     settings.DEFAULT_FROM_EMAIL,
        #     [email, ],
        # )
        # send_mass_mail((message_1, message_2))

        return response