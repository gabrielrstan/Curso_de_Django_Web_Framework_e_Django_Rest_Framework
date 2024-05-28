from collections import defaultdict

from django.forms import FileInput, ModelForm, Select, ValidationError

from authors.validators import AuthorRecipeValidator
from recipes.models import Recipe
from utils.django_forms import add_attr


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
        AuthorRecipeValidator(self.cleaned_data, ErrorClass=ValidationError)
        return super_clean
