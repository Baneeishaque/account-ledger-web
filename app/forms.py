from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django import forms


# STATES = (
#     ('', 'Choose...'),
#     ('MG', 'Minas Gerais'),
#     ('SP', 'Sao Paulo'),
#     ('RJ', 'Rio de Janeiro')
# )


class Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    passcode = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Passcode'}))
    # address_1 = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}))
    # address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'}))
    # city = forms.CharField()
    # state = forms.ChoiceField(choices=STATES)
    # zip_code = forms.CharField(label='Zip')
    # check_me_out = forms.BooleanField(required=False)


class LoginForm(Login):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-loginForm'
        self.helper.form_method = 'get'
        self.helper.form_action = 'login'
        self.helper.layout = Layout(

            # Row(
            #     Column('email', css_class='form-group col-md-6 mb-0'),
            #     Column('password', css_class='form-group col-md-6 mb-0'),
            #     css_class='form-row'
            # ),
            # 'address_1',
            # 'address_2',
            # Row(
            #     Column('city', css_class='form-group col-md-6 mb-0'),
            #     Column('state', css_class='form-group col-md-4 mb-0'),
            #     Column('zip_code', css_class='form-group col-md-2 mb-0'),
            #     css_class='form-row'
            # ),
            # 'check_me_out',
            # Submit('submit', 'Sign in')

            'username',
            'passcode',
            Submit('submit', 'Sign In...')

        )
