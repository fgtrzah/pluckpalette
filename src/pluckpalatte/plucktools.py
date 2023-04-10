from PIL import Image, ImageDraw

import numpy as np
from sklearn.cluster import KMeans


def path_to_vec(path) -> np.ndarray:
    return np.array(Image.open(path))


def pluck_colors(vec, num_colors) -> np.ndarray:
    vec = vec.reshape(-1, num_colors)
    model = KMeans(n_clusters=num_colors).fit(vec)
    return model.cluster_centers_


def pluck_theme_from_colors(colorList):
    n = len(colorList)
    im = Image.new("RGBA", (100 * n, 100))
    draw = ImageDraw.Draw(im)

    for idx, color in enumerate(colorList):
        color = tuple([int(x) for x in color])
        print(color)
        draw.rectangle(
            [(100 * idx, 0), (100 * (idx + 1), 100 * (idx + 1))], fill=tuple(color)
        )

    return im


def avg_rgb(picVec):
    fn = lambda arr, i: int(np.average(arr[:, :, i]))
    return fn(picVec, 0), fn(picVec, 1), fn(picVec, 2)
