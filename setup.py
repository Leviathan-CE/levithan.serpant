import setuptools


with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "InterfaceTools",
    version = "1.0.2",
    author = "Leviathan-CE",
    author_email = "leviathanCE@outlook.com",
    description = "allows for @interface class partail behavoiur decorator",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Leviathan-CE/InterfaceTools",
    project_urls = {
        "bug Tracker ": "https://github.com/Leviathan-CE/InterfaceTools/issues",
        "repository": "https://github.com/Leviathan-CE/InterfaceTools"
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "tools"},
    packages = setuptools.find_packages(where="tools"),
    python_requires = ">=3.11"
)
