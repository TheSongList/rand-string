from setuptools import setup

with open("README.md", "r") as f:
  readme = f.read()

setup(
  name = "rand-string",
  packages = ["rand_string"],
  version = "0.40",
  license="MIT",
  description = "Generates a random string of a specified length.",
  long_description=readme,
  long_description_content_type="text/markdown",
  author = "TheSongList",
  author_email = "the@songlist.moe",
  url = "https://github.com/TheSongList/random-string",
  download_url = "https://github.com/TheSongList/random-string/archive/v0.1.tar.gz",
  keywords = ["RANDOM", "STRING", "GENERATOR"],
  install_requires=[
      ],
  classifiers=[
    "Development Status :: 3 - Alpha",

    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",

    "License :: OSI Approved :: MIT License",

    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
  ],
)
