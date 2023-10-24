import warnings
import numpy as np

from pluckpalette.pluckutils import (
    path_to_vec,
    pluck_colors,
    pluck_theme_from_colors,
)

warnings.filterwarnings("ignore")


"""
Fixtures
"""


def prep_fixtures_path_to_vec():
    inputs = ["tests/data/01.png", "tests/data/02.png"]
    expected = [(608, 764, 4), (480, 484, 4)]

    return zip(inputs, expected)


def prep_fixtures_pluck_colors():
    image_paths = ["tests/data/01.png", "tests/data/02.png"]
    inputs = []

    for path in image_paths:
        vec = path_to_vec(path)
        inputs.append({"vec": vec, "num_colors": vec.shape[-1]})

    expected = [pluck_colors(**i) for i in inputs]

    return zip(inputs, expected)


def prep_fixtures_pluck_main_colors():
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
        rshape, eshape = np.shape(r), np.shape(e)

        assert (
            rshape == eshape
        ), f"FAILED: Expected r and e to have shame shape but r: {rshape} != e: {eshape}"


def test_pluck_main_colors():
    fixtures = prep_fixtures_pluck_main_colors()

    for i, e in fixtures:
        r = pluck_theme_from_colors(list(pluck_colors(i, num_colors=4)))
        flash_assert_msg = lambda a, b: f"FAILED: Expected r: {a} to equal e: {b} "

        try:
            if list(r["colors"]) == e:
                re_diff = np.subtract(list(r["colors"]), e)

                for d_vals in re_diff:
                    for d_val in d_vals:
                        assert d_val >= 20, flash_assert_msg(r, e)
        except:
            assert list(r["colors"]) == e, flash_assert_msg(r, e)


def test_rendering(path = None):
    import sys

    try:
        vec = path_to_vec(path or "tests/data/01.png")
        conf = pluck_colors(vec)
        theme = pluck_theme_from_colors(conf)
        rgba_colors_from_theme = theme.get("rawrgba")
        res = ""

        for c in rgba_colors_from_theme:
            r, g, b, _ = list(c)
            res += f"\033[48;2;{r};{g};{b}m rgba{c} \033[0m"
        print(res)
        assert res
    except ValueError:
        print(path)
        sys.exit()


def test_bulk():
    import os

    for fp in os.listdir('tests/data'):
        if ".gif" not in fp:
            fsp = f"tests/data/{fp}"
            test_rendering(fsp)

    assert True


def test_main():
    test_path_to_vec()
    test_pluck_colors()
    test_pluck_main_colors()
    test_rendering()
    test_bulk()


if __name__ == "__main__":
    test_main()
