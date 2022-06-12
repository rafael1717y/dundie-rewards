"""Setup for dundie.
"""

import os

from setuptools import find_packages, setup


def read(*paths):
    """Read the contents of a text file safely.
    >> read("dundie", "VERSION")
    '0.1.0'
    """
    rootpath = os.path.dirname(__file__)  # retorna o caminho do setup.py
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        return file_.read().strip()


def read_requirements(path):
    """Return a list of requirements from a text file."""
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(("#", "git+", '"', "-"))
    ]


setup(
    name="dundie",
    version="0.1.1",
    # Semantic Versioning
    # Major.Minor.Patch
    # X.Y.Z [razões mudar x -> quebra de compatibilidade ou marketing]
    # Y -> adicionar funcionalidade mas manter compatibilidade
    description="Reward Point System for Dunder Mifflin",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Rafael Gomes",
    python_requires=">=3.8",
    packages=find_packages(exclude=['integration']),
    include_package_data=True,
    entry_points={
        "console_scripts": ["dundie = dundie.__main__:main"]},
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "test": read_requirements("requirements.test.txt"),
        "dev": read_requirements("requirements.dev.txt"),
    },
)
