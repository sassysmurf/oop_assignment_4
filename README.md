# User Management System

## 1. Project Description

This project is a simple User Management System developed in Python using Object-Oriented Programming (OOP) principles.

It allows users to be created, stored, searched, updated, and deleted. It also provides utility methods for generating user IDs, passwords, and email addresses, as well as validating email addresses and password strength.

The project consists of three main classes:

- `User` – represents an individual user.
- `UserService` – manages the collection of users.
- `UserUtil` – provides utility methods for generating and validating user information.

## 2. Project Structure

```
oop_assignment_4/
│
├── main.py
├── README.md
└── test.main.py
```

## 3. Classes and Methods

### 3.1 User

The `User` class represents an individual user and stores their personal information.

**Attributes:**

| Attribute | Description |
|---|---|
| `user_id` | Unique identifier of the user |
| `name` | User's first name |
| `surname` | User's surname |
| `email` | User's email address |
| `password` | User's password |
| `birthday` | User's date of birth, stored as a `datetime` object |

**Methods:**

| Method | Description |
|---|---|
| `__init__()` | Initializes a user with their ID, name, surname, email, password, and birthday |
| `get_details()` | Returns a formatted string containing the user's information |
| `get_age()` | Calculates the user's current age based on their birthday |

### 3.2 UserService

The `UserService` class manages users using a class-level dictionary called `users`. The user's ID is used as the dictionary key.

**Methods:**

| Method | Description |
|---|---|
| `add_user(user)` | Adds a user to the dictionary |
| `find_user(user_id)` | Searches for a user by ID and returns the user if found |
| `delete_user(user_id)` | Deletes a user using their ID |
| `update_user(user_id, user_update)` | Updates an existing user's information |
| `get_number()` | Returns the total number of stored users |

The methods use the `@classmethod` decorator because they operate on the shared class-level user collection.

### 3.3 UserUtil

The `UserUtil` class contains static utility methods for generating and validating user information.

**Methods:**

| Method | Description |
|---|---|
| `generate_user_id()` | Generates a user ID using the current year and random digits |
| `generate_password()` | Generates a password containing uppercase letters, lowercase letters, digits, and special characters |
| `is_strong_password(password)` | Checks whether a password meets the required strength criteria |
| `generate_email(name, surname, domain)` | Generates an email address using the user's name, surname, and domain |
| `validate_email(email)` | Checks whether an email address matches the project's email format |

The methods use the `@staticmethod` decorator because they do not require access to an instance or class-level data.

## 4. UML Class Diagram

The UML class diagram illustrates the structure of the three classes and their relationships.

classDiagram
    class UserService {
        +dict~int, User~ users
        +add_user(user: User) void
        +find_user(user_id: int) User
        +delete_user(user_id: int) void
        +update_user(user_id: int, user_update: User) void
        +get_number() int
    }

    class UserUtil {
        <<utility>>
        +generate_user_id() int
        +generate_password() str
        +is_strong_password(password: str) bool
        +generate_email(name: str, surname: str, domain: str) str
        +validate_email(email: str) bool
    }

    class User {
        +user_id: int
        +name: str
        +surname: str
        +email: str
        +password: str
        +birthday: datetime
        +__init__(user_id: int, name: str, surname: str, email: str, password: str, birthday: datetime)
        +get_details() str
        +get_age() int
    }

    UserService "1" o-- "0..*" User : users
    UserService ..> UserUtil : uses
    UserUtil ..> User : creates data for

Relationships

Aggregation: UserService manages multiple User objects through its users dictionary. One UserService can manage zero or more users.

Dependency: UserService uses UserUtil methods when working with user information.

Dependency: UserUtil generates and validates data used by the User class.

The UserUtil class is marked with the utility stereotype because it contains static utility methods.

## 5. Requirements

- Python 3
- Standard Python libraries:
  - `datetime`
  - `random`
  - `secrets`
  - `string`
  - `re`

No external packages are required.

## 6. How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/sassysmurf/oop_assignment_4.git
   ```

2. Navigate to the project directory:

   ```bash
   cd oop_assignment_4
   ```

3. Run the Python file:

   ```bash
   python main.py
   ```

   If your system uses `python3`, run:

   ```bash
   python3 main.py
   ```

## 7. Sample Input and Output

The following example demonstrates creating a user, storing the user, retrieving their details, and checking the generated password and email.

### Sample input

```python
user_id = UserUtil.generate_user_id()

password = UserUtil.generate_password()

email = UserUtil.generate_email(
    "John",
    "Doe",
    "gmail.com"
)

user1 = User(
    user_id,
    "John",
    "Doe",
    email,
    password,
    datetime(2000, 5, 15)
)

UserService.add_user(user1)

found_user = UserService.find_user(user_id)

print(found_user.get_details())
print("Age:", found_user.get_age())
print("Strong password:", UserUtil.is_strong_password(password))
print("Valid email:", UserUtil.validate_email(email))
print("Total users:", UserService.get_number())
```

### Sample output

*The generated ID and password will vary each time the program runs.*

```text
Name: John
Surname: Doe
User ID: 2612345678
Email: john.doe@gmail.com
Birthday: 2000-05-15 00:00:00

Age: 26
Strong password: True
Valid email: True
Total users: 1
```

### Additional functionality examples

The following examples demonstrate updating and deleting users.

**Updating a user:**

```python
updated_user = User(
    user_id,
    "John",
    "Smith",
    "john.smith@gmail.com",
    password,
    datetime(2000, 5, 15)
)

UserService.update_user(user_id, updated_user)

print(UserService.find_user(user_id).surname)
```

Expected output:

```text
Smith
```

Deleting a user:

```python
UserService.delete_user(user_id)

print(UserService.get_number())
```

Expected output:

```text
0
```

## 8. Concepts Demonstrated

This project demonstrates the following Python concepts:

- Object-Oriented Programming
- Classes and objects
- Constructors and instance attributes
- Class methods and static methods
- Class-level attributes
- Dictionaries
- String formatting
- Date and time calculations
- Random and secure password generation
- Regular expressions
- Basic input validation

## 9. Conclusion

This project demonstrates how Python OOP principles can be used to create a basic user management system. It separates user data, user management operations, and utility functionality into three classes, making the code easier to understand and maintain.
