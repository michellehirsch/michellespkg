# Installation

This page guides you through installing `michellespkg`.

## Prerequisites

- Python 3.8 or higher.

## Installing with pip

You can install `michellespkg` directly from PyPI (once published) using pip:

```bash
pip install michellespkg
```

If you have specific optional dependencies (e.g., for development or extra features), you might install them like so (assuming they are defined in your `pyproject.toml`):
```bash
pip install michellespkg[dev]
```

## Installing from Source

To install `michellespkg` from its source code:

1.  Clone the repository:
    ```bash
    git clone https://github.com/michellehirsch/michellespkg.git
    cd michellespkg
    ```
2.  Install using pip (use `-e` for an editable/development install):
    ```bash
    pip install -e .
    ```