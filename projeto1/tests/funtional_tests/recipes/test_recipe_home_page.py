from unittest.mock import patch

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from tests.funtional_tests.recipes.base import RecipeBaseFunctionalTest


@pytest.mark.functional_test
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    def test_recipe_home_page_without_recipes_not_found_message(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, "body")
        self.assertIn('No recipes found here.', body.text)

    @patch('recipes.views.PER_PAGE', new=3)
    def test_recipe_search_input_can_find_correct_recipes(self):
        recipes = self.make_recipe_in_batch(qtd=20)

        title_needed = 'This is what I need'
        recipes[0].title = title_needed
        recipes[0].save()

        # User open a page
        self.browser.get(self.live_server_url)

        # See a search field with the text "Search for a recipe"
        search_input = self.browser.find_element(
            By.XPATH,
            '//input[@placeholder="Search for a recipe"]'
        )

        # Click on the input and type the search term to find the recipe
        # the desired title
        search_input.send_keys(title_needed)
        search_input.send_keys(Keys.ENTER)

        # The user see what he was looking for in the page
        self.assertIn(
            title_needed,
            self.browser.find_element(By.CLASS_NAME, "main-content-list").text,
        )
