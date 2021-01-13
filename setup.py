import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SyroQT-Calculator",
    version="0.0.1",
    author="Titas Janusonis",
    description="A simple calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={'': 'src'},
    url="https://github.com/SyroQT/TC-Calculator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
