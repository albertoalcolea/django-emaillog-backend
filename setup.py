import re
from setuptools import setup


with open('django_emaillog_backend/__init__.py', 'r') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]+)[\'"]',
                        f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')


with open('README.md', 'r') as f:
    readme = f.read()


setup(
    name='django-emaillog-backend',
    version=version,
    description="Django email backend that writes messages to logger instead of sending them by SMTP.",
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Alberto Alcolea',
    author_email='me@albertoalcolea.com',
    url='http://github.com/albertoalcolea/django-emaillog-backend',
    project_urls={
        'Source': 'http://github.com/albertoalcolea/django-emaillog-backend'
    },
    license='MIT',
    keywords=[
        'django mail',
        'django log',
        'django logger',
        'django mail backend',
        'django mail log backend',
        'django mail logger backend',
        'django plugin',
    ],
    packages=['django_emaillog_backend'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
          'django>=1.2',
    ],
    extras_require={
        'dev': [
            'flake8>=4.0.1',
            'twine>=4.0.0',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
