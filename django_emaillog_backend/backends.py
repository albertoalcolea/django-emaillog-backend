"""
Email backend that writes messages to logger instead of sending them.
"""
import logging

from django.core.mail.backends.base import BaseEmailBackend
from django.conf import settings


class LoggerBackend(BaseEmailBackend):
    def __init__(self, *args, **kwargs):
        if 'logger_name' in kwargs:
            self._logger_name = kwargs.pop('logger_name')
        else:
            self._logger_name = getattr(settings, 'EMAIL_LOGGER_NAME', 'django')
        if 'log_level' in kwargs:
            self.log_level = kwargs.pop('log_level')
        else:
            self.log_level = getattr(settings, 'EMAIL_LOGGER_LEVEL', logging.INFO)
        self.logger = logging.getLogger(self._logger_name)
        super(LoggerBackend, self).__init__(*args, **kwargs)

    def write_message(self, message):
        msg = message.message()
        log = 'Email sent\n{0}'.format(msg)
        self.logger.log(self.log_level, log)

    def send_messages(self, email_messages):
        msg_count = 0
        for message in email_messages:
            self.write_message(message)
            msg_count += 1
        return msg_count
