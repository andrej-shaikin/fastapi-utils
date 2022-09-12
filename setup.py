from setuptools import find_packages, setup

__version__ = "0.0.2"

setup(
    name='fastapi-utils',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/andrej-shaikin/fastapi-utils',
    author='Andrey Shaikin',
    author_email='kiwibon@yandex.ru',
    python_requires='>3.9',
    install_requires=[
      "fastapi",
      "environs",
      "ormar[postgresql]",
    ]
)
