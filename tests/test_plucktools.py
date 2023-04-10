import pytest

from pluckpalatte.plucktools import path_to_vec, pluck_colors, pluck_theme_from_colors

# fixtures
def prep_fixtures_path_to_vec():
    inputs = ["tests/data/01.png", "tests/data/02.png"]
    expected = [(608, 764, 4), (480, 484, 4)]

    return zip(inputs, expected)


def prep_fixtures_pluck_colors():
    inputs = []
    expected = []

    return zip(inputs, expected)


def prep_fixtures_pluck_main_colors():
    inputs = []
    expected = []

    return zip(inputs, expected)


# tests
def test_path_to_vec():
    fixtures = prep_fixtures_path_to_vec()

    for i, e in fixtures:
        r = path_to_vec(i)
        print(list(r), r.tolist())
        assert r.shape != e, f"FAILED: Expected {e} received {r.shape}"


@pytest.mark.skip(reason="TODO: implement")
def test_pluck_colors():
    fixtures = prep_fixtures_pluck_colors()

    for i, e in fixtures:
        r = True  # replace with correct vals
        assert r == e, f"FAILED: Expected {e} received {r}"


@pytest.mark.skip(reason="TODO: implement")
def test_pluck_main_colors():
    fixtures = prep_fixtures_pluck_main_colors()

    for i, e in fixtures:
        r = True  # replace with correct vals
        assert r == e, f"FAILED: Expected {e} received {r}"


if __name__ == "__main__":
    test_path_to_vec()
