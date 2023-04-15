import pandas as pd

"""
TODO: Strong type
"""


def ansii_query(fro: str, to: str, value: str, df: pd.DataFrame):
    return df.query("Quantity == 95 and UnitPrice(USD) == 182")


def main():
    import sys

    import csv

    with open("src/pluckpalatte/ansiitable.csv", newline="") as csvfile:
        print(sys.path)
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row["RGB"], row["Xterm Number"])


if __name__ == "__main__":
    main()
