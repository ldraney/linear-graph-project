# Use a specific version of Python provided by an official image
FROM debian:bookwork-slim

# Set environment variables to:
# - Ensure Python outputs all logs to the terminal
# - Set the location where Poetry will be installed
# - Ensure poetry is in the shell's PATH
ENV PYTHONDONTWRITEBYTECODE=1 \
    POETRY_HOME="/opt/poetry" \
    PATH="$POETRY_HOME/bin:$PATH"

# Create and switch to a new user
RUN adduser -u 1001 -D myuser
USER myuser
WORKDIR /home/myuser

# Install Poetry in an isolated environment
RUN python3 -m venv $POETRY_HOME \
    && $POETRY_HOME/bin/pip install --upgrade pip \
    && $POETRY_HOME/bin/pip install poetry==1.7.0

# Copy only the files needed for Poetry to install dependencies
COPY --chown=myuser pyproject.toml poetry.lock ./

# Disable virtualenv creation by Poetry and install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev  # Add --no-dev if you don't want dev dependencies

# Copy the rest of the application files into the container
COPY --chown=myuser . .

# The command to run the application
CMD ["python", "app.py"]
