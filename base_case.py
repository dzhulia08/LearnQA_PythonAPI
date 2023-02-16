import json.decoder
from datetime import datetime
from requests import Response

class BaseCase:
    def get_cookie (self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header (self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot find header with name {headers_name} in the last response"
        return response.headers[headers_name]

    def get_json_value (self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not JSON format. Response text is ' {response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        return response_as_dict[name]

    def prepare_registration_data(self, email=None):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        return {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

    def prepare_registration_data_without_username(self):
        return {
            'password': '123',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'email'
        }

    def prepare_registration_data_without_firstName(self):
        return {
            'password': '123',
            'username': 'learnqa',
            'lastName': 'learnqa',
            'email': 'email'
        }

    def prepare_registration_data_without_lastName(self):
        return {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'email': 'email'
        }

    def prepare_registration_data_without_email(self):
        return {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa'
        }

    def prepare_registration_data_without_password(self):
        return {
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'email'
        }

    def prepare_registration_data_with_small_firstName(self):
        return {
            'password': '123',
            'username': 'learnqa',
            'firstName': '1',
            'lastName': 'learnqa',
            'email': 'email'
        }

    def prepare_registration_data_with_firstName_more_250_character(self):
        return {
            'password': '123',
            'username': 'learnqa',
            'firstName': '12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901',
            'lastName': 'learnqa',
            'email': 'email'
        }