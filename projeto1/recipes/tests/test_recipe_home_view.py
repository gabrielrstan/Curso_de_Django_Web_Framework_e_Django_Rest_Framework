from django.urls import resolve, reverse

from recipes.tests.test_recipe_base import RecipeTestBase
from recipes.views import home


class RecipeHomeViewTest(RecipeTestBase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes found here',
            response.content.decode('utf-8'))

    def test_recipe_home_template_load_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        response_context_recipes = response.context['recipes']

        self.assertEqual(len(response_context_recipes), 1)
        self.assertEqual(
            response_context_recipes.first().title, 'Recipe Title')

        context = response.content.decode('utf-8')
        self.assertIn('Recipe Title', context)
        # self.assertIn('10 Minutos', context)
        # self.assertIn('5 Porções', context)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))

        self.assertIn(
            'No recipes found here',
            response.content.decode('utf-8'))
