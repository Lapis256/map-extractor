from setuptools import setup

setup(
    name="map-extractor",
    version="1.1.0",
    install_requires=[
        "Pillow>=9.0.1,<9.1.0",
        "nbtlib>=2.0.4,<2.1.0",
        "tqdm>=4.62.3,<4.63.0"
    ],
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
