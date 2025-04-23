# Django REST Store

This project is a RESTful API built with Django REST Framework to manage an online store. It provides endpoints to handle products, categories, users, orders, and more.

## Features

- CRUD for products and categories.
- User management and authentication.
- Endpoints to place orders.
- Pagination, filtering, and search.
- API documentation with Swagger/OpenAPI.

## Requirements

- Python 3.8+
- Django 4.x
- Django REST Framework 3.x

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/django-rest-store.git
    cd django-rest-store
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Docker

You can also run the project using Docker:

1. Build the Docker image:
    ```bash
    docker build -t django-rest-store .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 8000:8000 django-rest-store
    ```

3. Access the API at `http://127.0.0.1:8000/api/`. If Swagger is enabled, you can view the interactive documentation at `http://127.0.0.1:8000/swagger/`.

## Usage

Access the API at `http://127.0.0.1:8000/api/`. If Swagger is enabled, you can view the interactive documentation at `http://127.0.0.1:8000/swagger/`.

## Project Structure

```
django-rest-store/
├── manage.py
├── requirements.txt
├── Dockerfile
├── store/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
└── README.md
```

## Contributions

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.