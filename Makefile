# Magic Makefile Help
.PHONY: help all clean
help:
	@cat $(MAKEFILE_LIST) | grep -e "^[a-zA-Z_\-]*: *.*## *" | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# Files and Directories
PY_VERSION := 3.7.13

# Setup virtualenv and install packages
setup:
	pyenv install -s $(PY_VERSION)
	PYENV_VERSION=$(PY_VERSION) python -m venv .venv
	source .venv/bin/activate && \
		pip install --upgrade pip && \
		pip install -r book/requirements.txt

# View Jupyter-Book config
config:
	jupyter-book config

# Clean up Jupyter files
clean:
	jupyter-book clean

# Build Jupyter book
build:
	jupyter-book build book/

# Preview book HTML
preview:
	open book/_build/html/index.html