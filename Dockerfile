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
#RUN poetry build

# Install dependencies and build the project using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

#RUN poetry build

#RUN ls -al /app/dist/

# Stage 2: Run environment with Distroless Python image
# I chose this image because its hosted on gcr.io and is viewable on Github
# Its the only distroless on gcr.io with python pre-installed
# The python version it uses can be found at https://github.com/GoogleContainerTools/distroless/blob/main/python3/testdata/debian12.yaml
# python version is 3.11.2 as off 29-dec-23
FROM gcr.io/distroless/python3-debian12:latest

# Copy only the built packages from the builder stage
#COPY --from=builder /app/dist/*.whl /app/
COPY --from=builder /app /app
COPY --from=builder /root/.local /root/.local

# Set the working directory in the distroless image
WORKDIR /app

# Install the package using pip
# Note: Distroless images do not have a shell, pip or other tools,
# so we use an external tool to install the package.
#COPY --from=builder /root/.pyenv/versions/3.11.2/bin/pip /usr/local/bin/pip
#COPY --from=builder /root/.pyenv/versions/3.11.2/ /usr/local/lib/python3.11/

#RUN python --version && pip --version

#RUN ["/usr/local/bin/pip", "install", "/app/*.whl"]

# Default command to run the app
CMD ["lgp/app.py"]
