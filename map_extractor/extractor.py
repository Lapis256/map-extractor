from io import BytesIO

from nbtlib import Compound
from more_itertools import chunked
from PIL import Image


__all__ = (
    "iter_colors_from_world",
    "generate_map_image"
)

MAP_WIDTH  = 128
MAP_HEIGHT = 128


def _to_rgba(color):
    return tuple(map(lambda c: c.as_unsigned, color))


def _iter_map_color(colors):
    chunked_color_list = list(chunked(colors, 4))
    for x in range(MAP_WIDTH):
        for y in range(MAP_HEIGHT):
            color = chunked_color_list[x + y * MAP_WIDTH]
            yield (x, y), _to_rgba(color)


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
    image = Image.new("RGBA", (MAP_WIDTH, MAP_HEIGHT))
    for coords, color in _iter_map_color(colors):
        image.putpixel(coords, color)
    return image
