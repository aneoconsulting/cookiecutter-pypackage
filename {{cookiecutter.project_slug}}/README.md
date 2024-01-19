{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

{% set license_short_name = '' %}

{% if cookiecutter.open_source_license == "MIT license" %}
    {% set license_short_name = "MIT" %}
{% elif cookiecutter.open_source_license == "BSD license" %}
    {% set license_short_name = "BSD" %}
{% elif cookiecutter.open_source_license == "ISC license" %}
    {% set license_short_name = "ISC" %}
{% elif cookiecutter.open_source_license == "Apache Software License 2.0" %}
    {% set license_short_name = "Apache2" %}
{% elif cookiecutter.open_source_license == "GNU General Public License v3" %}
    {% set license_short_name = "GNU3" %}
{% endif %}

# {{ cookiecutter.project_slug }}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
[![License](https://img.shields.io/badge/license-{{ license_short_name }}-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-{{ cookiecutter.python_version }}%2B-blue.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![Docs](https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest)](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest)
{%- endif %}

## Overview

TODO

## Features

TODO

## Installation

### Prerequisites

- Python {{ cookiecutter.python_version }}
- pip (Python package installer)

### Setting up a Virtual Environment

It's a good practice to use a virtual environment to isolate your project dependencies. Create a virtual environment using `venv`:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

* On Windows:

```powershell
.\.venv\Scripts\activate
```

* On Unix or MacOS:

```bash
source .venv/bin/activate
```

### Installing the project using pip

Once the virtual environment is activated, you can install the project using pip.

```bash
pip install {{ cookiecutter.project_slug }}
```

This will install the project and its dependencies.

### Installing the project from sources

You can also intall the project from sources by cloning the repository.

```bash
git clone git@github.com:{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}.git
```

Navigate to the project directory and run:

```bash
pip install .
```

For development, you might want to install additional packages for testing, linting, etc. Install the development dependencies using:

```bash
pip install -e .[dev,tests]
```

{% if is_open_source %}

## Contributing

Contributions are always welcome!

See [CONTRIBUTING.md](CONTRIBUTING.md) for ways to get started.

## License

[{{ cookiecutter.open_source_license }}](LICENSE)

{%- endif %}
