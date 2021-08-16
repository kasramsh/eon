from setuptools import setup

install_requires = ["pandas>=0.25.0"]

tests_requires = ["pytest>=4.0.2"]

setup(
    name="src",
    version="0.0.1",
    description="basic project structure example for EON",
    author="Kasra Mani",
    author_email="manshaei@ieee.org",
    install_requires=install_requires,
    tests_require=tests_requires,
    packages=["src"],
)
