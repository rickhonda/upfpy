from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='upf',
    version='0.0.4',
    description='Fully Factor integers and build a flatfile database; unique prime factorization',
    py_modules=["upf"],
    package_dir={'': 'src'},

    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],

        long_description=long_description,
        long_description_content_type="text/markdown",

    url="https://github.com/rickhonda/upfpy",
    author="Rick Honda",
    author_email="rickyhonda@gmail.com",
)
