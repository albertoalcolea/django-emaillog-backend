import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-emaillog-backend",
    version = "0.1",
    url = '',
    license = 'BSD',
    description = "Django email backend that writes messages to logger instead of sending them by SMTP.",
    long_description = read('README.md'),
    author = 'Alberto Alcolea',
    author_email = 'me@albertoalcolea.com',

    install_requires=[
          'django>=1.2',
    ],

    packages=['django_emaillog_backend'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)