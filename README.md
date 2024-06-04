# Camus-Python

# First Steps

# Clone Project

git clone git@github.com:jose-camus/Camus-Python.git

# Create virtual env for FastAPI

python3 -m venv env

# Activate Virtual Env

source env/bin/activate

# Install dependencies

# Poetry

Poetry is a tool for dependency management and packaging in Python.
Poetry should always be installed in a dedicated virtual environment

pip3 install poetry

poetry init

pyproject.toml -> created

poetry add fastapi uvicorn sqlalchemy psycopg2-binary pydantic python-dotenv