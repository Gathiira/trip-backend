from django.conf import settings
from django.core.mail import EmailMessage

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

    def broad_cast_system_notification(self, payload):
        subject = payload['email_subject']
        body = payload['email_body']
        receiver = payload['to_email']
        
        email = EmailMessage(subject=subject, body=body, to=receiver)
        email.send()
