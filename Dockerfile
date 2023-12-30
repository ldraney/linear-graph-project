# /path/to/Dockerfile

# Stage 1: Build environment with Ubuntu and Python
FROM ubuntu:latest as builder

# Set a non-interactive frontend during the build to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies required for Pyenv
RUN apt-get update && apt-get install -y --no-install-recommends \
    make \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libxml2-dev \
    libxmlsec1-dev \
    libffi-dev \
    liblzma-dev \
	ca-certificates \
	git

# Install Pyenv
RUN curl https://pyenv.run | bash

## Set environment variables for Pyenv
ENV HOME=/root
ENV PYENV_ROOT=$HOME/.pyenv
ENV PATH="$PYENV_ROOT/bin:$PATH"

RUN pyenv install 3.11.2

# for the location of pip
ENV PATH="$PYENV_ROOT/versions/3.11.2/bin:$PATH"
# to get rid of annoying error for using pip as root
# see https://stackoverflow.com/questions/68673221/warning-running-pip-as-the-root-user
ENV PIP_ROOT_USER_ACTION=ignore

# Install Poetry
RUN pip install poetry==1.7

## Copy application to container
COPY . /app
WORKDIR /app

# Build the project using Poetry
RUN poetry install --without test

ENTRYPOINT ["poetry", "run", "python", "-m", "app/app.py"]

## Stage 2: Run environment with Distroless Python image
## I chose this image because its hosted on gcr.io and is viewable on Github
## Its the only distroless on gcr.io with python pre-installed
## The python version it uses can be found at https://github.com/GoogleContainerTools/distroless/blob/main/python3/testdata/debian12.yaml
## python version is 3.11.2 as off 29-dec-23
#FROM gcr.io/distroless/python3-debian12:latest

## Copy only the built packages from the builder stage
#COPY --from=builder /app/dist /app

## Set the working directory
#WORKDIR /app

## Default command to run the Flask app, to be overridden by Kubernetes' gunicorn command
#CMD ["python3", "app.py"]
