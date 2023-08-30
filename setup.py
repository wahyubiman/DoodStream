from setuptools import setup

setup(
    name="doodstream",
    version="1.0.0",
    description="Unofficial python api wrapper from https://doodstream.com",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    keywords="api, doodstream, video, hosting",
    url="http://github.com/wahyubiman/DoodStream",
    author="Wahyu Biman",
    author_email="wahyubiman@gmail.com",
    packages=["doodstream"],
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    zip_safe=False,
)
