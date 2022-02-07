from setuptools import setup

setup(
    name="map-extractor",
    version="1.0.0",
    install_requires=[ "Pillow", "more-itertools", "nbtlib", "tqdm" ],
    extras_require={
        ":sys_platform == 'linux' and platform_machine == 'aarch64'": [
            "bedrock@git+https://github.com/Lapis256/bedrock@master"
        ],
        ":platform_machine != 'aarch64'": [
            "bedrock@git+https://github.com/BluCodeGH/bedrock@master"
        ]
    },
    packages=[ "map_extractor" ],
    entry_points={
        "console_scripts": [
            "map_extractor = map_extractor.__main__:main"
        ]
    }
)
