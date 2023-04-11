from PIL import Image, ImageDraw

import numpy as np
from numpy import ndarray as NDArray
from sklearn.cluster import KMeans


def path_to_vec(path, **kwargs) -> NDArray:

    return np.array(Image.open(path, mode="r", formats=["PNG"]))


def pluck_colors(vec, num_colors=4) -> NDArray:
    vec = vec.reshape(-1, num_colors)
    model = KMeans(n_clusters=num_colors).fit(vec)
    return model.cluster_centers_


def pluck_theme_from_colors(color_list) -> Image:
    n = len(color_list)
    im = Image.new("RGBA", (100 * n, 100))
    draw = ImageDraw.Draw(im)

    for idx, color in enumerate(color_list):
        color = tuple([int(x) for x in color])
        draw.rectangle(
            [(100 * idx, 0), (100 * (idx + 1), 100 * (idx + 1))], fill=tuple(color)
        )

    return im


#
# def avg_rgb(vec):
#     fn = lambda arr, i: int(np.average(arr))
#     return fn(vec, 0), fn(vec, 1), fn(vec, 2)
