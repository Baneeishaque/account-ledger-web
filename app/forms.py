from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django import forms


class Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    passcode = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Passcode'}))


class LoginForm(Login):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-loginForm'
        self.helper.form_method = 'get'
        self.helper.form_action = 'login'
        self.helper.layout = Layout(

            'username',
            'passcode',
            Submit('submit', 'Sign In...')

        )


class User(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    passcode = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Passcode'}))


class UserAdditionForm(User):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-userAdditionForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'addUser'
        self.helper.layout = Layout(

            'username',
            'passcode',
            Submit('submit', 'Submit...')

        )
