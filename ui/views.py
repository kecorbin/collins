# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View


def serve_static(request):

 return render(request, 'job_dashboard.html')

