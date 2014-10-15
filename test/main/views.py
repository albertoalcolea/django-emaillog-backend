# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import send_mail


def _send_dumb_mail():
	send_mail('Subject here', 'Here is the message ó ios mío.', 'from@example.com',
    	['to@example.com'], fail_silently=False)


def index(request):
	_send_dumb_mail()
	return HttpResponse('This is a test')