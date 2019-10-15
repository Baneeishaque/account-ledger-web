from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.views.generic import FormView

from app.forms import LoginForm, UserAdditionForm
from app.models import TLogin


# TODO : Add Section logic

class LoginFormView(FormView):

    def get(self, request, *args, **kwargs):

        parameters = dict(form=LoginForm, template_name='app/login.html', title='Account Ledger : Authentication')

        if 'submit' not in request.GET:
            return render_to_response('app/login.html', parameters)
        else:
            query_result = TLogin.objects.filter(username=request.GET['username']).filter(
                passcode=request.GET['passcode'])
            if len(query_result) == 0:
                parameters.update(error_flag=True, error='Error...')
                return render_to_response('app/login.html', parameters)
            else:
                return redirect('addUser')


class AddUserFormView(FormView):
    form_class = UserAdditionForm
    template_name = 'app/login.html'
    extra_context = dict(title='Account Ledger : Add User')

    def post(self, request, *args, **kwargs):
        return HttpResponse(request.POST['username'] + request.POST['passcode'])
