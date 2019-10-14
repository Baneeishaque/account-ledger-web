from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import FormView

from app.forms import LoginForm


class LoginFormView(FormView):
    def get(self, request, *args, **kwargs):
        if 'submit' not in request.GET:
            return render_to_response('app/login.html', dict(form=LoginForm, template_name='app/login.html'))
        else:
            username = request.GET['username']
            passcode = request.GET['passcode']
            return HttpResponse(username + ' ' + passcode)
