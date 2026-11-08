# 4. Unit Testing
# Create a TestUser, TestUserService, TestUserUtil classes that includes
# test cases for methods.

from main import User
from main import UserService
from main import UserUtil
from datetime import datetime

# Generate user details
user_id = UserUtil.generate_user_id()
password = UserUtil.generate_password()
email = UserUtil.generate_email("John", "Doe", "gmail.com")

# Create a user
user1 = User(
    user_id,
    "John",
    "Doe",
    email,
    password,
    datetime(2000, 5, 15)
)

# Add user to UserService
UserService.add_user(user1)

# Find user
found_user = UserService.find_user(user_id)

# Print results
print(found_user.get_details())
print("Age:", found_user.get_age())
print("Strong password:", UserUtil.is_strong_password(password))
print("Valid email:", UserUtil.validate_email(email))
print("Total users:", UserService.get_number())

