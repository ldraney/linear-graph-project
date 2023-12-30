# Use the latest slim version of Debian
FROM python:3.12.1-bookworm

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy only the files needed for installing dependencies to avoid cache busting
COPY pyproject.toml poetry.lock* /app/

# Install dependencies in a virtual environment
RUN poetry config virtualenvs.create true \
    && poetry config virtualenvs.in-project true \
    && poetry install --no-dev

# Copy the rest of the code
COPY . /app/

# Build the project as a wheel
#RUN poetry build

## Stage 2: Copy the built wheel and install it in a clean Python environment
#FROM python:3.9-slim
#WORKDIR /app

## Copy the wheel from the builder stage
#COPY --from=builder /app/dist/*.whl /app/

## Install the application
#RUN pip install *.whl && rm *.whl

## The command to run your application, adjust as needed
#CMD ["python", "-m", "your_package_name"]
