
from time import sleep

import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from selenium.webdriver.common.by import By

from tests.functional_tests.authors.base import AuthorsBaseTest


@pytest.mark.functional_test
class AuthorLoginTest(AuthorsBaseTest):
    def test_user_valid_data_can_login_successfully(self):
        string_password = 'pass'
        user = User.objects.create_user(
            username='my_user', password=string_password
        )

        # User opens login page
        self.browser.get(self.live_server_url + reverse('authors:login'))

        # User sees login form
        form = self.browser.find_element(By.CLASS_NAME, 'main-form ')
        username_field = self.get_by_placeholder(form, 'Type your username')
        password_field = self.get_by_placeholder(form, 'Type your password')

        # User types his username and password
        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        # User submits the form
        form.submit()

        # User sees message success login and his username
        sleep(5)
        self.assertIn('Login successfully completed.',
                      self.browser.find_element(By.TAG_NAME, 'body').text
                      )
        self.assertIn(f'You are logged in with {user.username}.',
                      self.browser.find_element(By.TAG_NAME, 'body').text
                      )

    def test_login_create_raises_404_if_not_POST_method(self):
        self.browser.get(
            self.live_server_url + reverse('authors:login_create')
        )

        self.assertIn('Not Found', self.browser.find_element(
            By.TAG_NAME, 'body').text
        )

    def test_form_login_is_invalid(self):
        # User opens login page
        self.browser.get(
            self.live_server_url + reverse('authors:login')
        )

        # User sees login form
        form = self.browser.find_element(By.CLASS_NAME, 'main-form ')

        # And tries send empty values
        username = self.get_by_placeholder(form, 'Type your username')
        password = self.get_by_placeholder(form, 'Type your password')
        username.send_keys(' ')
        password.send_keys(' ')

        # User submits the form
        form.submit()

        # User sees error message
        self.assertIn('Invalid username or password.',
                      self.browser.find_element(By.TAG_NAME, 'body').text
                      )

    def test_login_invalid_credentials(self):
        # User opens login page
        self.browser.get(
            self.live_server_url + reverse('authors:login')
        )

        # User sees login form
        form = self.browser.find_element(By.CLASS_NAME, 'main-form ')

        # And tries to send values that don't match
        username = self.get_by_placeholder(form, 'Type your username')
        password = self.get_by_placeholder(form, 'Type your password')
        username.send_keys('invalid_user')
        password.send_keys('invalid_password')

        # User submits the form
        form.submit()

        # User sees error message
        self.assertIn('Invalid credentials.',
                      self.browser.find_element(By.TAG_NAME, 'body').text
                      )
