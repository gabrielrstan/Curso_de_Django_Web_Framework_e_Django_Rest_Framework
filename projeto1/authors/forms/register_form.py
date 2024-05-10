from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import CharField, EmailField, ModelForm, PasswordInput

from utils.django_forms import add_placeholder, strong_password


class RegisterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_placeholder(self.fields['last_name'], 'Ex.: Smith')
        add_placeholder(self.fields['password'], 'Your password')
        add_placeholder(self.fields['password2'], 'Repeat your password')

    first_name = CharField(
        error_messages={'required': 'Write your first name'},
        label='First Name'
    )

    last_name = CharField(
        error_messages={'required': 'Write your last name'},
        label='Last Name'
    )

    username = CharField(
        label='Username',
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Username must have at least 4 characters',
            'max_length': 'Username must have less than 150 characters'
        },
        help_text=(
            'Username must have letters, numbers or one of those @.+-_. '
            'The length should be between 4 and 150 characters.'
        ),
        min_length=4,
        max_length=150,
    )

    email = EmailField(
        error_messages={'required': 'E-mail is required'},
        label='E-mail',
        help_text='The e-mail must be valid',

    )

    password = CharField(
        widget=PasswordInput(),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text=(
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
        validators=[strong_password],
        label='Password'
    )

    password2 = CharField(
        label='Confirm Password',
        widget=PasswordInput(),
        error_messages={
            'required': 'Repeat your password'
        },
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exist = User.objects.filter(email=email).exists()

        if exist:
            raise ValidationError(
                'This e-mail is already registered', code='invalid',
            )

        return email

    def clean(self):
        clean_data = super().clean()
        password = clean_data.get('password')
        password2 = clean_data.get('password2')

        if password != password2:
            raise ValidationError(
                {
                    'password': 'Password and password2 must be the same',
                    'password2': 'Password and password2 must be the same'
                }
            )
