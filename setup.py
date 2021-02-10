from setuptools import setup
__version__ = "0.0.1"


setup(
    name="SCTransformPy",
    version=__version__,
    author="Alexander Tarashansky",
    author_email="atarashansky@illumina.com",
    url="",
    description="Python port of SCTransform from the Seurat package.",
    install_requires=[
        "numpy",
        "scipy",
        "statsmodels",
        "KDEpy",
        "pandas",
        "anndata",        
    ],
    packages=[''],
)
