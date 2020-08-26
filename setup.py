import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reproducibility-pkg-Vrishab-Commuri", # Replace with your own username
    version="1.0.1",
    author="Vrishab Commuri",
    author_email="vrishabcommuri@gmail.com",
    description="A small example package demonstrating a reproducibility issue",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)