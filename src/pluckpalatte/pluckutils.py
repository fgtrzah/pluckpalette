import argparse, os
import numpy as np

from pathlib import Path, PurePath
from PIL import Image, ImageDraw
from numpy import ndarray as NDArray
from sklearn.cluster import KMeans


def path_to_vec(path: str) -> NDArray:
    try:
        return np.array(Image.open(path, mode="r"))
    except ValueError:
        print("Unable to parse default format, broadening scope")
        return np.array(Image.open(path, mode="r", formats=["PNG"]))


def pluck_colors(vec, num_colors=4) -> NDArray:
    vec = vec.reshape(-1, num_colors)
    model = KMeans(n_clusters=num_colors, n_init="auto").fit(vec)
    return model.cluster_centers_


def pluck_theme_from_colors(color_list):
    n = len(color_list)
    # TODO: refactor Image related configs
    im = Image.new("RGBA", (10 * n, 10))
    draw = ImageDraw.Draw(im, mode="RGBA")
    colors = []

    for idx, color in enumerate(color_list):
        color = tuple([int(x) for x in color])
        draw.rectangle(
            [(10 * idx, 0), (10 * (idx + 1), 10 * (idx + 1))], fill=tuple(color)
        )
        colors.append(color)

    return {"im": im, "colors": get_theme_representation(colors), "rawrgba": colors}


def get_theme_representation(colors_list):
    res = sorted(colors_list, key=lambda x: x[0])
    return [f"rgba{color}" for color in res]


ARG_DESC = """
    🎨🪄plug-palette:
    --------------------------
    This tool accepts relative paths to images
    on disk and outputs the dominant colors
    in rgba format.
"""


def validate_file(f):
    if not os.path.exists(f):
        raise argparse.ArgumentTypeError("{0} does not exist".format(f))
    return f


def get_parsed_args():
    """
    TODO:
        change design to utilize
        args obj model -> docstring
        dont need to over-engineer in
        favor of reduced bloat
    """
    parser = argparse.ArgumentParser(
        description=ARG_DESC, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-p",
        "--path",
        dest="filename",
        required=False,
        type=validate_file,
        help="input file",
        metavar="FILE",
    )
    parser.add_argument(
        "--url",
        type=str,
        default=None,
        required=False,
        help="Url to image",
    )

    return parser.parse_args()


def main():
    try:
        import sys

        # get cli args
        args = get_parsed_args()
        # translate path to vector
        vec = path_to_vec(f"{args.filename}")
        # read theme
        conf = pluck_colors(vec)
        theme = pluck_theme_from_colors(conf)
        # normalize for representation
        rgba_colors_from_theme = theme.get("rawrgba")
        for c in rgba_colors_from_theme:
            r, g, b, _a = list(c)
            print(f"\033[48;2;{r};{g};{b}m rgba{c} \033[0m")

    except ValueError:
        print("Error sourcing image")
        sys.exit(2)


if __name__ == "__main__":
    main()
