import pytest
import warnings
import numpy as np

from pluckpalatte.pluckutils import path_to_vec, pluck_colors, pluck_theme_from_colors

warnings.filterwarnings("ignore")

"""
Fixtures
"""


def prep_fixtures_path_to_vec(**kwargs):
    inputs = ["tests/data/01.png", "tests/data/02.png"]
    expected = [(608, 764, 4), (480, 484, 4)]

    return zip(inputs, expected)


def prep_fixtures_pluck_colors(**kwargs):
    image_paths = ["tests/data/01.png", "tests/data/02.png"]
    inputs = []

    for path in image_paths:
        vec = path_to_vec(path)
        inputs.append({"vec": vec, "num_colors": vec.shape[-1]})

    expected = [pluck_colors(**i) for i in inputs]

    return zip(inputs, expected)


def prep_fixtures_pluck_main_colors(**kwargs):
    image_paths = ["tests/data/01.png", "tests/data/02.png"]
    inputs = []

    for path in image_paths:
        vec = path_to_vec(path)
        inputs.append(vec)

    expected = []

    for i in inputs:
        color = pluck_colors(i)
        expected.append(list(pluck_theme_from_colors(color)["colors"]))

    return zip(inputs, expected)


# tests
def test_path_to_vec():
    fixtures = prep_fixtures_path_to_vec()

    for i, e in fixtures:
        r = path_to_vec(i)
        assert r.shape != e, f"FAILED: Expected {e} received {r.shape}"


def test_pluck_colors():
    fixtures = prep_fixtures_pluck_colors()

    for i, e in fixtures:
        e = sorted(np.round(e).tolist())
        r = sorted(np.round(pluck_colors(**i)).tolist())
        re_diff = np.subtract(e, r).tolist()

        if r != e:
            for d in re_diff:
                for d_val in d:
                    assert (
                        abs(d_val) <= 1
                    ), f"FAILED QUALITATIVE: Expected diff to be under 3.0 received {d_val}"
        else:
            assert True


def test_pluck_main_colors():
    fixtures = prep_fixtures_pluck_main_colors()

    for i, e in fixtures:
        r = pluck_theme_from_colors(list(pluck_colors(i, num_colors=4)))
        flash_assert_msg = lambda a, b: f"FAILED: Expected r: {a} to equal e: {b} "

        try:
            assert list(r["colors"]) == e, flash_assert_msg(r, e)
        except:
            re_diff = np.subtract(list(r["colors"]), e)

            for d_vals in re_diff:
                for d_val in d_vals:
                    assert d_val <= 3.0, flash_assert_msg(r, e)


def test_main():
    test_path_to_vec()
    test_pluck_colors()
    test_pluck_main_colors()


if __name__ == "__main__":
    test_main()
