# Django EmailLog Backend

[![Latest PyPI Version](https://img.shields.io/pypi/v/django-emaillog-backend.svg)](https://pypi.python.org/pypi/django-emaillog-backend)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/django-emaillog-backend.svg)](https://pypi.python.org/pypi/django-emaillog-backend)
[![PyPI - Django Version](https://img.shields.io/pypi/djversions/django-emaillog-backend)](https://pypi.python.org/pypi/django-emaillog-backend)

Simple email backend for Django that writes messages to logger instead of sending them to a SMTP server.

## Installation

Installation is easy using `pip`

```bash
pip install django-emaillog-backend
```

## Usage

To ensure that all emails sent using the send_mail function of Django are sent to a log you must add the following line to your `settings.py` file:

```python
EMAIL_BACKEND = 'django_emaillog_backend.backends.LoggerBackend'
```

You can specify the logger to which the logs will be sent adding it to the `settings.py` file

```python
EMAIL_LOGGER_NAME = 'your_logger_name'
```

For example, you can create a custom logger to test the correct behaviour of sending mails as follow:

```python
# Add a custom logger to test mails
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

# Configure the email backend
EMAIL_BACKEND = 'django_emaillog_backend.backends.LoggerBackend'

EMAIL_LOGGER_NAME = 'email_logger'
```

The default logger for `django-emaillog-backend` is the global Django logger called 'django'.

It is also possible to choose the severity level of messages sent to the logger adding the following to your `settings.py` file:

```python
EMAIL_LOGGER_LEVEL = logger_level
```

`EMAIL_LOGGER_LEVEL` expects an integer. We recommend using the severity levels of the logging module:

```python
logging.DEBUG (10)
logging.INFO (20)
logging.WARNING (30)
logging.ERROR (40)
logging.CRITICAL (50)
```

For example:

```python
import logging
EMAIL_LOGGER_LEVEL = logging.INFO
```

The default log level is `INFO`.
