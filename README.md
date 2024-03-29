### Current dev workflow
```
docker compose -f ci/docker-compose-dev.yml down && \
docker compose -f ci/docker-compose-dev.yml up
```

right now both dev and production use:
```
docker compose -f ci/docker-compose.yml build
docker compose -f ci/docker-compose.yml up
```

and the installation script for docker is:
```
sudo -v
sudo apt-get -y install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" |  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get -y update
sudo apt-get -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo usermod -aG docker $USER
exec su -l $USER
docker --version
docker run hello-world
```





# linear-graph-project
making a y=mx+b software for a life insurance company presentation

### Prerequisites:
- Ubuntu 22.04 or similar Linux distribution

## Getting Started with the Project
This comprehensive guide provides a smooth and clear path for setting up the development environment with Pyenv and Poetry, ensuring developers have all the tools they need to get started.

This guide assumes [Pyenv](https://github.com/pyenv/pyenv) is installed on your system.  If you don't, as of 12-27-2023 on Ubuntu 22.04 the commands are:
```bash
#install pyenv
curl https://pyenv.run | bash
sudo apt-get update; sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
	libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
	libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
export PATH=$PATH:$HOME/.pyenv/bin/pyenv
```
And add these to your shells dotfile, such as .bashrc:
```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
This is useful for automatically using the local environment when you `cd` into the repo's directory, as seen below.

## Setting Up the Development Environment

Run `pre-commit install` to install pre-commit into your git hooks. pre-commit will now run on every commit. Every time you clone a project using pre-commit running pre-commit install should always be the first thing you do.  Linting is also done via actions each time you remote commit.

Occassionally run `pre-commit autoupdate` to get the latest repos for plugins, afterwhich you again run `pre-commit install`.

Pyenv allows you to easily switch between multiple versions of Python, and Poetry is a tool for dependency management and packaging in Python.

me: so it should end up being pyenv -> pip install poetry -> poetry install and run

### pyenv commands
```
pyenv install 3.12.1
pyenv virtualenv 3.12.1 linear-pyenv
pyenv local linear-pyenv
```

This project includes a `.python-version` file, which Pyenv uses to automatically activate the correct environment when you enter the project directory:
with a simple cd into this directory you should now be in the `linear-pyenv` environment.

### Step 3: Install and Set Up Poetry

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

### Step 3: Install and Set Up Poetry and dependencies

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on, and it will manage (install/update) them for you.

1. **Install Poetry**:
   Poetry can be installed in several ways, but one straightforward method is via pip. Since you're using Pyenv, that's the most appropriate route:
   ```bash
   pip install poetry
   ```

 Run the following command to install the dependencies specified in your `pyproject.toml` file:
   ```bash
   poetry install
```

### Step 5: Running the Application

To run the Dash application within the Poetry-managed environment, you can use the `poetry run` command. This ensures you're using the correct versions of Python and all dependencies.

```bash
poetry run python app.py
```

This command should be used each time you want to run your application, ensuring that the correct virtual environment is always utilized.

### Adding and Managing Dependencies

- **Adding New Dependencies**:
  If you need to add more packages to your project, use the `poetry add` command. For example, to add Flask:

  ```bash
  poetry add flask
  ```

- **Updating Dependencies**:
  To update your dependencies to their latest versions, use:

  ```bash
  poetry update
  ```

me: TODO - add dependabot and whatever to our pipeline to ensure security and robust tests.  This shouldn't take much time and will add value to this repo as a template for future projects.

### Understanding Poetry Files

- **pyproject.toml**: This is the primary configuration file for your project, which includes metadata and a list of dependencies. When you add a package with Poetry, it's automatically added here.

- **poetry.lock**: This file locks your dependencies to specific versions to ensure consistency across environments and deployments. You should commit this file to your version control system.

- **.venv**: This is the directory where Poetry creates the virtual environment for your project. It's typically located within your project directory (if you've configured Poetry to do so) and is activated automatically when using `poetry run` or `poetry shell`.

Remember, the virtual environment created by Poetry during the `poetry install` step persists and doesn't need to be recreated after restarting your PC. It ensures a consistent, isolated environment for your project's dependencies.


## Running the App in Production on AWS
