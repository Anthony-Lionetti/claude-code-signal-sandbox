"""
Run tests by level:
    uv run pytest code/test_simulation.py -k "level_1" -v
    uv run pytest code/test_simulation.py -k "level_2" -v
    uv run pytest code/test_simulation.py -k "level_3" -v
    uv run pytest code/test_simulation.py -k "level_4" -v

Run all tests:
    uv run pytest code/test_simulation.py -v
"""

import pytest
# from simulation import ClassName


class TestLevel1:
    """Tests for... """

    def test_level_1_(self):
        assert True

class TestLevel2:
    """Tests for... """

    def test_level_2_(self):
        assert True

class TestLevel3:
    """Tests for... """

    def test_level_3_(self):
        assert True

class TestLevel4:
    """Tests for... """

    def test_level_4_(self):
        assert True