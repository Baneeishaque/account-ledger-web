import requests
from django.shortcuts import redirect, render
from django.views.generic import FormView

from app.forms import LoginForm, UserAdditionForm
from app.models import TLogin


# TODO : Add Section logic

class LoginFormView(FormView):

    def get(self, request, *args, **kwargs):

        parameters = dict(form=LoginForm, template_name='app/login.html', title='Account Ledger : Authentication')

        if 'submit' not in request.GET:
            # return render_to_response('app/login.html', parameters)
            return render(request, 'app/login.html', parameters)
        else:
            query_result = TLogin.objects.filter(username=request.GET['username']).filter(
                passcode=request.GET['passcode'])
            if len(query_result) == 0:
                parameters.update(error_flag=True, error='Error...')
                return render(request, 'app/login.html', parameters)
            else:
                return redirect('addUser')


class AddUserFormView(FormView):
    form_class = UserAdditionForm
    template_name = 'app/login.html'
    extra_context = dict(title='Account Ledger : Add User')

    def post(self, request, *args, **kwargs):

        # TODO : Function - API URL Creation from Method Name
        # TODO : Function - Execute POST & return JSON
        # TODO : Function - Execute POST, check error & return JSON
        # TODO : Logout Functionality
        # TODO : Extend Layout Files
        # TODO : Keep Inputs On Error

        api_endpoint = "http://adgarage.co/wp-production/account_ledger_server/http_API/insertUser.php"
        api_response = requests.post(api_endpoint,
                                     dict(username=request.POST['username'], passcode=request.POST['passcode']))
        api_response = api_response.json()
        if api_response['status'] == '1':
            return render(request, 'app/login.html', dict(form=UserAdditionForm, template_name='app/login.html',
                                                          title='Account Ledger : Add User', error_flag=True,
                                                          error=api_response['error']))
        elif api_response['status'] == '0':
            return render(request, 'app/login.html', dict(form=UserAdditionForm, template_name='app/login.html',
                                                          title='Account Ledger : Add User', success_flag=True,
                                                          success='User Addition Success...'))
