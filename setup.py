from setuptools import setup
__version__ = "0.0.1"


setup(
    name="SCTransform",
    version=__version__,
    author="Alexander Tarashansky",
    author_email="tarashanst@gmail.com",
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
   py_modules=['SCTransform'],
)
