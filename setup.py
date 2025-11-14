from setuptools import setup, find_packages

setup(
    name="lightml",
    version="0.1.0",
    author="Shahzeb Khoso",
    author_email="your.email@example.com",
    description="A lightweight machine learning library built from scratch using NumPy.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MrShahzebKhoso/ML_FromScratch",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.20.0",
        "scipy>=1.5.0",
    ],
    python_requires=">=3.8",
)
