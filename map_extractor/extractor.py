from io import BytesIO

from PIL import Image
import numpy as np
import amulet_nbt


__all__ = (
    "iter_colors_from_world",
    "generate_map_image"
)

MAP_WIDTH  = 128
MAP_HEIGHT = 128


def iter_colors_from_world(world):
    for key, value in world.iterKeys():
        if not key.startswith(b"map_"):
            continue

        compound = amulet_nbt.load(value, compressed=False, little_endian=True)
        colors = compound["colors"]
        if len(set(colors)) <= 1:
            continue
        yield compound["mapId"].value, colors


def generate_map_image(colors):
    array = np.fromiter(colors, np.uint8)
    image = array.reshape((MAP_WIDTH, MAP_HEIGHT, 4))
    return Image.fromarray(image)
