
import re

from django.contrib.auth.models import User
from django.forms import CharField, ModelForm, PasswordInput, ValidationError


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
            code='Invalid'
        )


class RegisterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_placeholder(self.fields['last_name'], 'Ex.: Smith')
        add_placeholder(self.fields['password'], 'Your password')
        add_placeholder(self.fields['password2'], 'Repeat your password')

    password = CharField(
        required=True,
        widget=PasswordInput(),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text=(
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
        validators=[strong_password]
    )

    password2 = CharField(
        label='Confirm Password',
        required=True,
        widget=PasswordInput()
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'E-mail',
            'password': 'Password',
        }

        help_texts = {
            'email': 'The e-mail must be valid',
        }

        error_messages = {
            'username': {
                'required': 'This field must not be empty',
            }
        }

    def clean_password(self):
        data = self.cleaned_data.get('password')

        if 'atenção' in data:
            raise ValidationError(
                'Não digite %(pipoca)s no campo password',
                code='invalid',
                params={'pipoca': 'atenção'}
            )

        return data

    def clean(self):
        clean_data = super().clean()
        password = clean_data.get('password')
        password2 = clean_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password': 'Password and password2 must be the same',
                'password2': 'Password and password2 must be the same'
            }
            )
