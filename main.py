# This is an object-oriented solution for managing user records

# Instructions:
#
# 1. User Class (Instance Variables & Methods)
#
# Create a class User that represents a user with the following attributes
# and methods:
# Instance Variables:
# user_id (integer) – Unique identifier for the user.
# name (string) – First name of the user.
# surname (string) – Last name of the user.
# email (string) – Email of the user.
# password(string) – Password of the user.
# birthday (datetime) – Birthday of the user.

import random
import secrets
import string
import re
from datetime import datetime

class User:

# Methods:
# __init__(self, user_id, name, surname, birthday): Initializes the user's details.

    def __init__(self, user_id, name, surname, email, password, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.birthday = birthday



# get_details(self): Returns a formatted string containing user details.
    def get_details(self):
        return (f"Name: {self.name}\n"
                f"Surname: {self.surname}\n"
                f"User ID: {self.user_id}\n"
                f"Email: {self.email}\n"
                f"Birthday: {self.birthday}\n"
        )

# get_age(self): Computes and returns the user’s age.
    def get_age(self):
        today = datetime.now()
        age = today.year - self.birthday.year
        if today.month < self.birthday.month or (
            today.month == self.birthday.month
            and today.day < self.birthday.day
        ):
            age -=1

        return age

# 2. UserService Class (Class Methods & Class Attribute)
# Create a UserService class that manages users.

class UserService:

# Class Attribute:
# users – A dictionary to store all User objects. key is the user_id, value is an
# User object.
    users = {}

# Class Methods:
# add_user(cls, user): Adds a User object to users.
    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user

# find_user(cls, user_id): Searches for a user by user_id and returns the user
# object if found.
    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id)

# delete_user(cls, user_id): Removes a user from users by user_id.
    @classmethod
    def delete_user(cls, user_id):
        cls.users.pop(user_id, None)

# update_user(cls, user_id, user_update): Updates student attributes using
# user_update object arguments.
    @classmethod
    def update_user(cls, user_id, user_update):
       if user_id in cls.users:
           existing_user = cls.users[user_id]
           existing_user.name = user_update.name
           existing_user.surname = user_update.surname
           existing_user.email = user_update.email
           existing_user.password = user_update.password
           existing_user.birthday = user_update.birthday

# get_number(cls): Returns number of students in a users
    @classmethod
    def get_number(cls):
        return len(cls.users)

# 3. UserUtil Class (Static Methods)
# Create a UserUtil class that provides utility functions.

class UserUtil:

# Static Methods:
# generate_user_id(): Generates unique new user_id with 9 digits.
# The first two digits are taken from the current year (e.g., "24" for 2024).
# The remaining digits are randomly generated.

    @staticmethod
    def generate_user_id():
        year = datetime.now().year % 100
        random_digits = random.randint(1000000,9999999)

        return int(str(year) + str(random_digits))

# generate_password(): Generates new password. Minimum 8 characters long.
# At least 1 uppercase, 1 lowercase, 1 digit, and 1 special character.

    @staticmethod
    def generate_password():
        uppercase = secrets.choice(string.ascii_uppercase)
        lowercase = secrets.choice(string.ascii_lowercase)
        digit = secrets.choice(string.digits)
        special = secrets.choice(string.punctuation)

        password_list = [uppercase, lowercase, digit, special]

        all_characters = (
            string.ascii_uppercase +
            string.ascii_lowercase +
            string.digits +
            string.punctuation
        )
        for i in range(4):
            password_list.append(secrets.choice(all_characters))
        secrets.SystemRandom().shuffle(password_list)

        password = ''.join(password_list)
        return password


# is_strong_password(password): checks if a given password is at least 8
# characters long and includes uppercase and lowercase letters,
# numbers, and special characters.
    @staticmethod
    def is_strong_password(password):

        if len(password) < 8:
            return False

        has_uppercase = any(char.isupper() for char in password)
        has_lowercase = any(char.islower() for char in password)
        has_digits = any(char.isdigit() for char in password)
        has_special = any(char in string.punctuation for char in password)

        if has_uppercase and has_lowercase and has_digits and has_special:
            return True
        else:
            return False

# generate_email(name, surname, domain): Generates an email address using
# the user’s name and surname in lowercase (e.g., "john.doe@domain.com").
    @staticmethod
    def generate_email(name, surname, domain):
        email = f"{name.lower()}.{surname.lower()}@{domain}"
        return email


# validate_email(email) – Checks if the given email is in a valid format
# (e.g., follows the pattern name.surname@domain.com).
    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z]+\.[a-zA-Z]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))
