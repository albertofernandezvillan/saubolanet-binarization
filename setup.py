import os
import pkg_resources
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='sauvolanet',
    version='0.0.16',
    description='Sauvolanet binarization algorithm',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/albertofernandezvillan/sauvola-net',
    license='MIT',
    packages=['sauvolanet'],
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    include_package_data=True,
    package_dir={'sauvolanet': 'sauvolanet'},
    package_data={'sauvolanet': ['pretrained_models/weights.h5'],
                  'sauvolanet': ['dataset/*.png']
                  },
)
