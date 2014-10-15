Django EmailLog Backend
=======================

Simple email backend for Django that writes messages to logger instead of sending them to a SMTP server.

Installation is easy using ``pip`` and will install all required libraries.


Installation
------------

Installation is easy using ``pip``

    $ pip install django-emaillog-backend

or get it from source

    $ git clone https://github.com/albertoalcolea/django-emaillog-backend
    $ cd django-emaillog-backend
    $ python setup.py install


Usage
-----

To ensure that all emails sent using the send_mail function of Django are sent to a log should add the following to your ``settings.py`` file:

    EMAIL_BACKEND = 'emaillog_backend.LoggerBackend'


You can specify the logger to which the logs will be sent adding in your ``settings.py`` file

    EMAIL_LOGGER_NAME = 'your_logger_name'

For example, you can create a custom logger to test sending emails as follow:

Add a custom logger in your ``settings.py`` file:

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            ...
        },
        'handlers': {
            ...
        },
        'loggers': {
            ...
            'email_logger': {
                'handlers': ['your_handler'],
                'propagate': True,
                'level': 'DEBUG',
            },
        }
    }

In your ``settings.py`` file select the email backend and set the EMAIL_LOGGER_NAME constant:

    EMAIL_BACKEND = 'django-emaillog-backend.backends.LoggerBackend'

    EMAIL_LOGGER_NAME = 'email_logger'

The default logger for ``django-emaillog-backend`` is the global Django logger called 'django'.

It is also possible to choose the severity level of messages sent to the logger adding the following to your ``settings.py`` file:

    EMAIL_LOGGER_LEVEL = logger_level

where ``EMAIL_LOGGER_LEVEL`` is an integer. We recommend using the severity levels of module logging:

    logging.DEBUG (10)
    logging.INFO (20)
    logging.WARNING (30)
    logging.ERROR (40)
    logging.CRITICAL (50)

For example:

    import logging
    EMAIL_LOGGER_LEVEL = logging.INFO

The default log level is INFO.