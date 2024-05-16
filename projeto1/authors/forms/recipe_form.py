from collections import defaultdict

from django.core.exceptions import ValidationError
from django.forms import FileInput, ModelForm, Select

from recipes.models import Recipe
from utils.django_forms import add_attr
from utils.strings import is_positive_number


class AuthorRecipeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)

        add_attr(self.fields.get('title'), 'class', 'span-2')
        add_attr(self.fields.get('description'), 'class', 'span-2')
        add_attr(self.fields.get('preparation_steps'), 'class', 'span-2')

    class Meta:
        model = Recipe
        fields = ['title', 'preparation_time', 'preparation_time_unit',
                  'servings', 'servings_unit', 'description',
                  'preparation_steps', 'cover',]

        widgets = {
            'cover': FileInput(
                attrs={
                    'class': 'span-2',
                }
            ),
            'servings_unit': Select(
                choices=(
                    ('Servings', 'Servings'),
                    ('Pieces', 'Pieces'),
                    ('People', 'People'),
                ),
            ),
            'preparation_time_unit': Select(
                choices=(
                    ('Minutes', 'Minutes'),
                    ('Hours', 'Hours'),
                    ('Days', 'Days'),
                ),
            ),
        }

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)

        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')

        if title == description:
            self._my_errors['description'].append(
                'Title and description must be different')
            self._my_errors['title'].append(
                'Title and description must be different')

        if self._my_errors:
            raise ValidationError(self._my_errors)

        return super_clean

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) < 5:
            self._my_errors['title'].append(
                'Title must have at least 5 caracteres')

        return title

    def clean_preparation_time(self):
        field_name = 'preparation_time'
        field_value = self.cleaned_data.get('preparation_time')
        if not is_positive_number(field_value):
            self._my_errors[field_name].append(
                'Preparation time must be a positive number'
            )

        return field_value

    def clean_servings(self):
        field_name = 'servings'
        field_value = self.cleaned_data.get('servings')
        if not is_positive_number(field_value):
            self._my_errors[field_name].append(
                'Servings must be a positive number'
            )

        return field_value
