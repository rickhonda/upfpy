import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='upfpy',
    version='0.0.10',
    author="Rick Honda",
    author_email="rickhonda7@gmail.com",
    description='Fully factors given integer: unique prime factorization',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rickhonda/upfpy",

    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],

    packages=["upfpy"],
    entry_points={
        "console_scripts": [
            "upfpy=upfpy.__main__:main",
            ]
        },
    extras_require={
        "dev": [
            "pytest>=3.8",
            ],
        },
    )
