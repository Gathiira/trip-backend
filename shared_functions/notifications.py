from django.conf import settings
from django.core.mail import EmailMessage

from shared_functions import utility_functions

utility_function = utility_functions


class NotificationClass:

    def __init__(self):
        self.communication_message_templates = \
            settings.NOTIFICATION_MESSAGE_TEMPLATES
        self.start_trip_notification_message = \
            self.communication_message_templates[
                'START_TRIP_NOTIFICATION_MESSAGE']
        self.end_trip_notification_message = \
            self.communication_message_templates[
                'END_TRIP_NOTIFICATION_MESSAGE']
        self.trip_notification_subject = \
            self.communication_message_templates[
                'TRIP_NOTIFICATION_SUBJECT']

    def broad_cast_system_notification(self, payload):
        subject = payload['email_subject']
        body = payload['email_body']
        receiver = payload['to_email']
        pdf = utility_function.generate_pdf(subject, body)

        email = EmailMessage(subject=subject, body=body, to=receiver)
        email.attach('smokinace.pdf', pdf, 'application/pdf')
        email.content_subtype = "html"
        email.send()
