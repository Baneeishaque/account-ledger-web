from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import FormView

from app.forms import LoginForm
from app.models import TLogin


# TODO : Add Section logic

class LoginFormView(FormView):
    def get(self, request, *args, **kwargs):
        if 'submit' not in request.GET:
            return render_to_response('app/login.html',
                                      dict(form=LoginForm, template_name='app/login.html'))
        else:
            query_result = TLogin.objects.filter(username=request.GET['username']).filter(
                passcode=request.GET['passcode'])
            if len(query_result) == 0:
                return render_to_response('app/login.html',
                                          dict(form=LoginForm, template_name='app/login.html', alert_flag=True))
            else:
                return HttpResponse('Success')
