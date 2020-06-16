import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='upfpy',
    version='0.0.2',
    author="Rick Honda",
    author_email="rickhonda7@gmail.com",
    description='Fully factors given integer: unique prime factorization',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rickhonda/upfpy",

# https://setuptools.readthedocs.io/en/latest/setuptools.html

#    py_modules=["upf"],
#    package_dir={'upf': 'src'},
#    packages=['upf'],
#    packages=setuptools.find_packages(),


    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    packages=["upfpy"],
#    python_requires='>=3.8',

)
