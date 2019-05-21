from setuptools import setup, find_packages     # Use setuptools not dist_utils 


setup(
    name='widgetApp',
    version='0.1',
    author="Matthew Griffiths",
    author_email="griff@me3d.com.au",
    description="An example module",
    packages=find_packages(),           # This automatically discovers modules / submodules in the directory 
    install_requires=[],
    license="MIT",
    entry_points={                      # Entrypoints let us add a command to $PATH. Works great with venv & pipenv!
        'console_scripts': [
            'widgetApp = widgetApp.__main__:main',
        ],
    }
)
