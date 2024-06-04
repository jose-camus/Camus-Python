# Camus-Python Project

This project is a FastAPI application. Below are the steps to set up and run the project.

## Clone Project

First, clone the repository to your local machine.

```
git clone git@github.com:jose-camus/Camus-Python.git
```

## Create Virtual Environment for FastAPI
Create a virtual environment to manage dependencies for the project.

```
python3 -m venv env
```

## Activate Virtual Environment
Activate the virtual environment.

```
source env/bin/activate
```

# Install Dependencies
## Poetry
Poetry is a tool for dependency management and packaging in Python. It should always be installed in a dedicated virtual environment.

Install Poetry using pip.

```
pip3 install poetry
```

Initialize Poetry in the project directory.

```
poetry init
```

This will create a pyproject.toml file which is used to manage the project's dependencies and settings.


## Add Dependencies
Add the necessary dependencies for the project using Poetry.

```
poetry add fastapi uvicorn sqlalchemy psycopg2-binary pydantic python-dotenv
```

# Run the Application
To start the application on localhost, activate the virtual environment and run the following command.

```
source env/bin/activate

uvicorn app.main:app --reload
```

This will start the FastAPI application with auto-reload enabled, which is useful for development.


# Additional Information

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **Uvicorn**: A lightning-fast ASGI server implementation, using uvloop and httptools.
- **SQLAlchemy**: The Python SQL toolkit and Object-Relational Mapping (ORM) library.
- **Psycopg2-binary**: A PostgreSQL database adapter for Python.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **python-dotenv**: Reads key-value pairs from a .env file and can set them as environment variables.

Feel free to reach out if you have any questions or need further assistance!
