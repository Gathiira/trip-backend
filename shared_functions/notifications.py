from django.conf import settings

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

    def broad_cast_system_notification(self, incoming_payload, auth_headers):
        payload = incoming_payload
        # send emails
        send_emails = True
        if send_emails:
            return True
        else:
            return False
