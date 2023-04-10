import pytest
import warnings

from pluckpalatte.plucktools import path_to_vec, pluck_colors, pluck_theme_from_colors

warnings.filterwarnings("ignore")

"""
Fixtures
"""


def prep_fixtures_path_to_vec(**_kwargs):
    inputs = ["tests/data/01.png", "tests/data/02.png"]
    expected = [(608, 764, 4), (480, 484, 4)]

    return zip(inputs, expected)


# TODO: remove circular fixture codependence
def prep_fixtures_pluck_colors(**kwargs):
    image_paths = ["tests/data/01.png", "tests/data/02.png"]
    inputs = []

    for image_path in image_paths:
        vec_fixture = path_to_vec(image_path)
        inputs.append([vec_fixture, vec_fixture.shape[1]])

    expected = [pluck_colors(*i) for i in inputs]

    return zip(inputs, expected)


def prep_fixtures_pluck_main_colors(**_kwargs):
    inputs = []
    expected = []

    return zip(inputs, expected)


# tests
@pytest.mark.skip(reason="TODO: implement")
def test_path_to_vec():
    fixtures = prep_fixtures_path_to_vec()

    for i, e in fixtures:
        r = path_to_vec(i)
        assert r.shape != e, f"FAILED: Expected {e} received {r.shape}"


def test_pluck_colors():
    fixtures = prep_fixtures_pluck_colors()

    for i, e in fixtures:
        r = pluck_colors(*i)  # replace with correct vals

        print(i[1])

        assert r == e, f"FAILED: Expected {e} received {r}"


@pytest.mark.skip(reason="TODO: implement")
def test_pluck_main_colors():
    fixtures = prep_fixtures_pluck_main_colors()

    for i, e in fixtures:
        r = True  # replace with correct vals
        assert r == e, f"FAILED: Expected {e} received {r}"


if __name__ == "__main__":
    test_path_to_vec()
    test_pluck_colors()
