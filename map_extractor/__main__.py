import os
from os.path import join
import argparse

from tqdm import tqdm
from bedrock import World

from .extractor import iter_colors_from_world, generate_map_image


def extract_map(world, output=""):
    maps = list(iter_colors_from_world(world))
    for id, colors in tqdm(maps):
        image = generate_map_image(colors)
        image.save(join(output, f"{id}.png"))


def main():
    parser = argparse.ArgumentParser(description="指定したワールドのマップを全て抽出します。")
    parser.add_argument("world", help="ワールドです。")
    parser.add_argument("-o", "--output", help="画像を保存するディレクトリです。", default=os.getcwd())

    args = parser.parse_args()
    with World(args.world) as world:
        extract_map(world, args.output)


if __name__ == "__main__":
    main()
