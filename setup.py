import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="web-scraper-jcoliveira",
    version="0.0.1",
    author="Julio Cezar de Oliveira",
    author_email="jc.2013oliveira@gmail.com",
    description="Package used to improve data extraction from websites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="change_url",
    package=setuptools.find_packages(),
    classifiers=[
        "Programing Language :: Python :: 3",
        "License :: OSI Aproved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"

)
