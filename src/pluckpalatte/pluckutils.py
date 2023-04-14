import argparse
import numpy as np

from typing import Optional
from PIL import Image, ImageDraw
from numpy import ndarray as NDArray
from sklearn.cluster import KMeans


def path_to_vec(path) -> NDArray:
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


def get_desc_doc():
    # TODO: change design to utilize
    # args obj model -> docstring
    # dont need to over-engineer in
    # favor of reduced bloat
    arg_desc = """\
            Usage:
            --------------------------------

                This tool accepts relative paths to images
                on disk and outputs the dominant colors
                in rgba format.
            """
    parser = (
        argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter, description=arg_desc
        )
        .add_argument_group("-u", "--url", help="URL of input image")
        .add_argument("-f", "--url", help="Local file path of input image")
        .add_argument("-h", "--help", help="Displays this help message")
    )

    return parser


def main():
    parser = get_desc_doc()
    args = parser.parse_args()

    return args


if __name__ == "__name__":
    main()
