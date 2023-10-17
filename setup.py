import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "reverse",
    version = "0.0.1",
    author = "lephuduc",
    author_email = "lephuduc111@gmail.com",
    description = "Reversing module",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/lephuduc/reverse",
    project_urls = {
        "Bug Tracker": "https://github.com/lephuduc/reverse/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.7"
)