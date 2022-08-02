from setuptools import setup, find_packages

setup(
    name="doodstream",
    version="0.1.2",
    description="Unofficial python api wrapper from https://doodstream.com",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    keywords="api doodstream video hosting unlimited",
    url="http://github.com/wahyubiman/DoodStream",
    author="Wahyu Biman",
    author_email="wahyubiman@gmail.com",
    packages=["doodstream"],
    install_requires=[
        "requests",
        "click",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "console_scripts": ["doodstream=doodstream.doodstream:main"],
    },
    zip_safe=False,
)
