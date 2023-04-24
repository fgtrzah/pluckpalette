import pandas as pd
import pytest

"""
TODO: Strong type
"""

FILENAME = "src/pluckpalatte/ansiitable.csv"


def rgba_to_xterm(rgba: str, df: pd.DataFrame = None):
    res = None
    if df:
        return df[df["RGBA"] == rgba]["Xterm Number"]
    else:
        import csv

        with open(FILENAME, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row.get("RGBA") == rgba.replace(" ", ""):
                    res = row.get("Xterm Number")
                    break
    return res


"""
[Link](https://stackabuse.com/how-to-print-colored-text-in-python/)"""


def colors_256(color_, rgbrep):
    num1 = str(color_)
    num2 = str(color_).ljust(3, " ")
    if color_ % 16 == 0:
        return f"\033[38;5;{num1}m {rgbrep}, {num2} \033[0;0m\n"
    else:
        return f"\033[38;5;{num1}m {rgbrep}, {num2} \033[0;0m"


@pytest.mark.skip(reason="Out of scope")
def test_ansiiutils():
    import csv, sys

    with open(FILENAME, newline="\n") as csvfile:
        reader = csv.DictReader(csvfile)
        try:
            for row in reader:
                print(colors_256(int(row["Xterm Number"]), row["RGBA"]))
        except csv.Error as e:
            sys.exit("file %s, line %d: %s" % (FILENAME, reader.line_num, e))

    assert True


def main():
    test_ansiiutils()


if __name__ == "__main__":
    main()
