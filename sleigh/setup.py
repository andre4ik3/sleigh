import setuptools

with open("../README.md", "r") as fp:
    long_description = fp.read()

setuptools.setup(
    name="sleigh-internal",
    version="0.0.1",
    author="andre4ik3",
    author_email="andrey@andre4ik3.dev",
    description="Sleigh Internal Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andre4ik3/sleigh",
    project_urls={
        "Bug Tracker": "https://github.com/andre4ik3/sleigh/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
)
