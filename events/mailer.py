from django.core import mail
from django.core.mail import EmailMessage
from django.conf import settings
import os
import codecs

registration_template = codecs.open("events/Registration_message.html", 'r').read()
transaction_template = codecs.open("events/Transaction Id Received Message.html", 'r').read()

class Mailer:
    """
    Send email messages helper class
    """

    def __init__(self, from_email="Breeze 2020 <no-reply@snu-breeze.com>"):
        self.connection = mail.get_connection()
        self.from_email = from_email

    def send_messages(self, subject, message_type, email_data, to_emails):
        messages = self.__generate_messages(subject, message_type, email_data, to_emails)
        self.__send_mail(messages)

    def __send_mail(self, mail_messages):
        """
        Send email messages
        :param mail_messages:
        :return:
        """
        self.connection.open()
        self.connection.send_messages(mail_messages)
        self.connection.close()

    def __generate_messages(self, subject, message_type, email_data, to_emails):
        """
        Generate email message from Django template
        :param subject: Email message subject
        :param template: Email template
        :param to_emails: to email address[es]
        :return:
        """
        messages = []

        if message_type == 'Registration':
            message_content = registration_template
            message_content = message_content.replace('(id)', str(email_data[0]))
            message_content = message_content.replace('(name)', str(email_data[1]))
            message_content = message_content.replace('(college)', str(email_data[2]))
        elif message_type == 'Transaction':
            message_content = transaction_template
            message_content = message_content.replace('(id)', str(email_data[0]))

        
        for recipient in to_emails:
            message = EmailMessage(subject, message_content, to=[recipient], from_email=self.from_email, reply_to=['no-reply'])
            message.content_subtype = 'html'
            messages.append(message)

        return messages
