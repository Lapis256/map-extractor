from io import BytesIO

from nbtlib import Compound
from PIL import Image
import numpy as np


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

        compound = Compound.parse(BytesIO(value), "little")[""]
        colors = compound["colors"]
        if len(set(colors)) <= 1:
            continue
        yield compound["mapId"].unpack(), colors


def generate_map_image(colors):
    array = np.uint8(np.fromiter(colors, int))
    image = array.reshape((MAP_WIDTH, MAP_HEIGHT, 4))
    return Image.fromarray(image)
