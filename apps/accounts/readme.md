# 🔒 Accounts App Documentation

The `accounts` app manages user authentication and profile features for the Django REST Store project.

## Features

- User registration and login
- Password management (reset, change)
- User profile management
- Token-based authentication (e.g., JWT)

## 📦 Model

### `User`
Represents a User

- `id`: Auto-incremented primary key.
- `username`: Unique username for the user.
- `first_name`: User's first name.
- `last_name`: User's last name.
- `email`: User's email address.
- `is_staff`: Designates whether the user can access the admin site.
- `is_active`: Designates whether this user account should be considered active.
- `date_joined`: The date and time when the user joined.

## API Endpoints

### List endpoint

| Endpoint                | Method | Description                |
|-------------------------|--------|----------------------------|
| `/api/v1.0/account/register/` | POST   | Register a new user        |
| `/api/v1.0/account/login/`    | POST   | User login                 |
| `/api/v1.0/account/user/profile/`  | GET    | Retrieve user profile      |
| `/api/v1.0/account/user/profile/`  | PUT    | Update user profile        |
| `/api/v1.0/account/change-password/` | PUT | Request change password   |
| `/api/v1.0/account/password-reset/` | POST | Request forget password   |



#### Register a new user
```http
  POST /api/v1.0/account/register/
```
| Request Body | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. The username for the new account |
| `email ` | `string` | **Required**. The email for the new account |
| `first_name ` | `string` | **Required**. The first name for the new account |
| `last_name ` | `string` | **Required**. The last name for the new account |
| `password ` | `string` | **Required**. The password for the new account |
| `password_confirm ` | `string` | **Required**. Confirmation of the password|

#### User login
```http
  POST /api/v1.0/account/login/
```
| Request Body | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. The username of the account |
| `password ` | `string` | **Required**. The password for the account |

#### Retrieve user Profile
```http
  GET /api/v1.0/account/user/profile/
```

| Headers | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `Bearer Token (string)` | **Required**. The access token of the account |

#### Update username Profile
```http
  PUT /api/v1.0/account/user/profile/
```

| Request Body | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. The new username of the acoount |

| Headers | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `Bearer Token (string)` | **Required**. The access token of the account |

#### Update password Profile
```http
  PUT /api/v1.0/account/user/change-password/
```
| Request Body | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `old_password` | `string` | **Required**. The old password of the acoount |
| `new_password` | `string` | **Required**. The new password for the acoount |

| Headers | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `Bearer Token (string)` | **Required**. The access token of the account |


#### Reset password profile

```http
  POST /api/v1.0/account/password-reset/
```
| Request Body | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. The email of the account for reset password |

Send email with URL for reset password.
