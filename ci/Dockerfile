# Use the latest slim version of Debian
FROM debian:bookworm-slim

# Set environment variables to avoid Python buffering and ensure UTF-8 encoding
ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8

# Install essential packages and the latest Python version
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry in a global scope
RUN pip3 install poetry

# Set the working directory in the container
WORKDIR /app

# Copy only the files needed for Poetry to install dependencies
COPY pyproject.toml poetry.lock /app/

# Configure Poetry: Disable virtualenv creation and install dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev && \
    # Remove Poetry after dependencies installation to keep image lightweight
    pip3 uninstall --yes poetry

# Copy the rest of the application files into the container
COPY . /app

# The command to run the application
CMD ["python3", "app.py"]

