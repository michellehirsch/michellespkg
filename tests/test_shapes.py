import pytest
import math
from unittest import mock

import michellespkg

# Test Area Calculation Functions


def test_area_rectangle_positive_values():
    assert michellespkg.area_rectangle(10, 5) == 50
    assert michellespkg.area_rectangle(7.5, 2) == 15.0


def test_area_rectangle_zero_values():
    assert michellespkg.area_rectangle(0, 5) == 0
    assert michellespkg.area_rectangle(10, 0) == 0
    assert michellespkg.area_rectangle(0, 0) == 0


def test_area_rectangle_negative_values():
    with pytest.raises(ValueError, match="Length and width must be non-negative."):
        michellespkg.area_rectangle(-10, 5)
    with pytest.raises(ValueError, match="Length and width must be non-negative."):
        michellespkg.area_rectangle(10, -5)
    with pytest.raises(ValueError, match="Length and width must be non-negative."):
        michellespkg.area_rectangle(-10, -5)


def test_area_circle_positive_radius():
    assert michellespkg.area_circle(1) == pytest.approx(math.pi)
    assert michellespkg.area_circle(7) == pytest.approx(math.pi * 49)


def test_area_circle_zero_radius():
    assert michellespkg.area_circle(0) == 0


def test_area_circle_negative_radius():
    with pytest.raises(ValueError, match="Radius must be non-negative."):
        michellespkg.area_circle(-5)


def test_area_triangle_positive_values():
    assert michellespkg.area_triangle(10, 4) == 20
    assert michellespkg.area_triangle(5.5, 3) == pytest.approx(8.25)


def test_area_triangle_zero_values():
    assert michellespkg.area_triangle(0, 5) == 0
    assert michellespkg.area_triangle(10, 0) == 0
    assert michellespkg.area_triangle(0, 0) == 0


def test_area_triangle_negative_values():
    with pytest.raises(ValueError, match="Base and height must be non-negative."):
        michellespkg.area_triangle(-10, 5)
    with pytest.raises(ValueError, match="Base and height must be non-negative."):
        michellespkg.area_triangle(10, -5)
    with pytest.raises(ValueError, match="Base and height must be non-negative."):
        michellespkg.area_triangle(-10, -5)


# Test Plotting Functions (basic "does it run" and error handling)


@mock.patch("matplotlib.pyplot.show")
def test_plot_rectangle_runs_with_valid_input(mock_show):
    """Tests if plot_rectangle runs without error for valid inputs."""
    michellespkg.plot_rectangle(length=10, width=5)
    mock_show.assert_called_once()  # Verifies plt.show() would have been called


@mock.patch("matplotlib.pyplot.show")
def test_plot_rectangle_runs_with_origin(mock_show):
    michellespkg.plot_rectangle(length=10, width=5, origin=(1, 1))
    mock_show.assert_called_once()


def test_plot_rectangle_invalid_input():
    with pytest.raises(
        ValueError, match="Length and width must be positive for visualization."
    ):
        michellespkg.plot_rectangle(length=-10, width=5)
    with pytest.raises(
        ValueError, match="Length and width must be positive for visualization."
    ):
        michellespkg.plot_rectangle(length=10, width=-5)
    with pytest.raises(
        ValueError, match="Length and width must be positive for visualization."
    ):
        michellespkg.plot_rectangle(length=0, width=5)
    with pytest.raises(
        ValueError, match="Length and width must be positive for visualization."
    ):
        michellespkg.plot_rectangle(length=10, width=0)


@mock.patch("matplotlib.pyplot.show")
def test_plot_circle_runs_with_valid_input(mock_show):
    """Tests if plot_circle runs without error for valid inputs."""
    michellespkg.plot_circle(radius=7)
    mock_show.assert_called_once()


@mock.patch("matplotlib.pyplot.show")
def test_plot_circle_runs_with_center(mock_show):
    michellespkg.plot_circle(radius=7, center=(2, 3))
    mock_show.assert_called_once()


def test_plot_circle_invalid_input():
    with pytest.raises(ValueError, match="Radius must be positive for visualization."):
        michellespkg.plot_circle(radius=-5)
    with pytest.raises(ValueError, match="Radius must be positive for visualization."):
        michellespkg.plot_circle(radius=0)


@mock.patch("matplotlib.pyplot.show")
def test_plot_triangle_runs_with_valid_input(mock_show):
    """Tests if plot_triangle runs without error for valid inputs."""
    michellespkg.plot_triangle(base=8, height=4)
    mock_show.assert_called_once()


@mock.patch("matplotlib.pyplot.show")
def test_plot_triangle_runs_with_origin(mock_show):
    michellespkg.plot_triangle(base=8, height=4, origin=(1, 1))
    mock_show.assert_called_once()


def test_plot_triangle_invalid_input():
    with pytest.raises(
        ValueError, match="Base and height must be positive for visualization."
    ):
        michellespkg.plot_triangle(base=-8, height=4)
    with pytest.raises(
        ValueError, match="Base and height must be positive for visualization."
    ):
        michellespkg.plot_triangle(base=8, height=-4)
    with pytest.raises(
        ValueError, match="Base and height must be positive for visualization."
    ):
        michellespkg.plot_triangle(base=0, height=4)
    with pytest.raises(
        ValueError, match="Base and height must be positive for visualization."
    ):
        michellespkg.plot_triangle(base=8, height=0)
