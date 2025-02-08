from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="asimov-model",
    version="0.1.0",
    author="Dede Wiranto",
    author_email="dwiranto767@gmail.com",
    description="A humorous implementation of Asimov's Three Laws of Robotics for AI projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seclorum0/asimov-model",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Artistic Software",
        "Topic :: Games/Entertainment",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "spacy>=3.0.0",
    ],
)
