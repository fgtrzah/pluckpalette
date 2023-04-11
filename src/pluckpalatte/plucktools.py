from typing import Optional
from PIL import Image, ImageDraw

import numpy as np
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
