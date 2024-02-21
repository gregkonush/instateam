FROM python:3.12

WORKDIR /app

# Install pipenv
RUN pip install pipenv

# Copy Pipfile and Pipfile.lock and install dependencies
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of the application code
COPY . /app/

# Expose the port
EXPOSE 8000

# Run the Django development server
CMD ["pipenv", "run", "python", "manage.py", "runserver", "8000"]
