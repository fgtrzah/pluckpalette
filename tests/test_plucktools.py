import pytest

from pluckpalatte.plucktools import path_to_img_array, pick_colors, show_key_colors

__author__ = "figtreez"
__copyright__ = "figtreez"
__license__ = "MIT"


def prep_fixtures():
    inputs = ["data/01.jpeg", "data/01.jpeg"]
    expected = [True, True]

    return zip(inputs, expected)


def test_pick_colors():
    fixtures = prep_fixtures()

    for i, e in fixtures:
        r = True  # replace with correct vals
        assert r == e, f"FAILED: Expected {e} received {r}"
