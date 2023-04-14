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
    model = KMeans(n_clusters=num_colors).fit(vec)
    return model.cluster_centers_


def pluck_theme_from_colors(color_list):
    n = len(color_list)
    im = Image.new("RGBA", (10 * n, 10))
    draw = ImageDraw.Draw(im, mode="RGBA")
    colors = []

    for idx, color in enumerate(color_list):
        color = tuple([int(x) for x in color])
        draw.rectangle(
            [(100 * idx, 0), (100 * (idx + 1), 100 * (idx + 1))], fill=tuple(color)
        )
        colors.append(color)

    return {"im": im, "colors": get_theme_representation(colors)}


def get_theme_representation(colors_list):
    res = sorted(colors_list, key=lambda x: x[0])
    return res


ARG_DESC = """
    🎨🪄plug-palette:
    --------------------------
    This tool accepts relative paths to images
    on disk and outputs the dominant colors
    in rgba format.
"""


def validate_file(f):
    if not os.path.exists(f):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("{0} does not exist".format(f))
    return f


def get_parser():
    """
    TODO: change design to utilize
    args obj model -> docstring
    dont need to over-engineer in
    favor of reduced bloat
    """
    parser = argparse.ArgumentParser(
        description=ARG_DESC, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=Path(__file__).absolute(),
        help="Posix path to image",
    )
    parser.add_argument(
        "--url",
        type=str,
        default=None,
        help="Url to image",
    )
    parser.add_argument(
        "-i",
        "--input",
        dest="filename",
        required=True,
        type=validate_file,
        help="input file",
        metavar="FILE",
    )

    return parser


def main():
    import sys

    # get cli args
    raw_argv = sys.argv[1:]
    p = get_parser()
    args = p.parse_args(args=raw_argv)

    try:
        # get file path
        args = p.parse_args()

        # translate path to vector
        vec = path_to_vec(f"{Path(__file__).parent}/{args.path}")
        conf = list(pluck_colors({"vec": vec, "num_colors": vec.shape[-1]}))
        # read theme
        theme = pluck_theme_from_colors(conf, num_colors=4)
        # normalize for representatino
        print(get_theme_representation(theme))
    except ValueError:
        print("Error sourcing image")
        sys.exit(2)


if __name__ == "__main__":
    main()
