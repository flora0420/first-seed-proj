"""Test first_seed_prog functions."""

from first_seed_prog import app


def test_app():
    """Test app.main function."""
    assert app.main("ah ", 3) == "ah ah ah "
