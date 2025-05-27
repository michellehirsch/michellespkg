# michellespkg

A simple Python library for computing the area and visualizing common two-dimensional shapes.

## Overview

`michellespkg` provides easy-to-use functions to:
*   Calculate the area of rectangles, circles, and triangles.
*   Generate basic visualizations of these shapes with their dimensions using `matplotlib`.

This package is primarily intended as a demonstration or for simple geometric calculations and visualizations.

## Features

*   **Area Calculations:**
    *   `area_rectangle(length, width)`
    *   `area_circle(radius)`
    *   `area_triangle(base, height)`
*   **Shape Visualization:**
    *   `plot_rectangle(length, width, origin=(x,y))`
    *   `plot_circle(radius, center=(x,y))`
    *   `plot_triangle(base, height, origin=(x,y))` (for right-angled triangles)

## Installation

This package is not yet available on PyPI. To install it for development or local use:

1.  **Clone the repository (if you haven't already):**
    ```bash
    # If you have the project locally, skip this step
    git clone <your-repository-url>
    cd michellespkg
    ```

2.  **Create a virtual environment and install dependencies using `uv`:**
    It's highly recommended to use a virtual environment. `uv` can manage this for you.

    *   To install the package with its core dependencies:
        ```bash
        uv pip install -e .
        ```
    *   To include development dependencies (like `pytest` for running tests):
        ```bash
        uv pip install -e ".[dev]"
        ```

    If you have a `uv.lock` file and want to ensure an exact reproduction of the environment:
    ```bash
    uv venv  # Ensure a virtual environment exists or create one
    uv pip sync uv.lock
    # Then, if you also want it editable for development:
    uv pip install -e . --no-deps # --no-deps because sync already handled them
    ```

## Try it out in a Jupyter notebook:

Explore `michellespkg` interactively with our Jupyter Notebook tutorial. You can run it directly in your browser using Google Colab:

[!Open In Colab](https://colab.research.google.com/github/michellehirsch/michellespkg/blob/main/examples/tutorial.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/michellehirsch/michellespkg/HEAD?urlpath=%2Fdoc%2Ftree%2Fexamples%2Ftutorial.ipynb)

## Usage

Once installed, you can import and use the functions in your Python scripts:

```python
import michellespkg

# Calculate areas
rect_area = michellespkg.area_rectangle(10, 5)
print(f"Area of rectangle: {rect_area}")  # Output: 50

circ_area = michellespkg.area_circle(7)
print(f"Area of circle: {circ_area}")  # Output: ~153.938

tri_area = michellespkg.area_triangle(8, 4)
print(f"Area of triangle: {tri_area}")  # Output: 16.0

# Visualize shapes (this will open matplotlib plot windows)
michellespkg.plot_rectangle(length=12, width=6)
michellespkg.plot_circle(radius=5, center=(1, 1))
michellespkg.plot_triangle(base=9, height=3, origin=(0,0))
```

### Example Script

An example script demonstrating the usage can be found in `examples/example.py`. You can run it (after installation) using `uv`:

```bash
uv run python examples/example.py
```

## Dependencies

*   `matplotlib`: For plotting the shapes.

## Running Tests

Tests are written using `pytest`. To run the tests:

1.  Ensure you have installed the development dependencies:
    ```bash
    uv pip install -e ".[dev]"
    ```
    Or, if using a lock file that includes dev dependencies:
    ```bash
    uv pip sync uv.lock
    ```

2.  Run pytest using `uv`:
    ```bash
    uv run pytest
    ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.