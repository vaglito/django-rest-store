# Use the official Python image from the Docker Hub
FROM python:3.12.6

# Set the working directory
WORKDIR /code

# Install dependencies
COPY /docs/dependencies.txt /code/
RUN pip install -r dependencies.txt

# Copy the project files
COPY . /code/

# Expose the port the app runs on
EXPOSE 7000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:7000"]