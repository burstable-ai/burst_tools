from setuptools import setup, find_packages
setup(
    name="burst_tools",
    version="0.1.2",
    install_requires=[
        "pynvml"
    ],
    scripts=['bin/gpumem'],
    python_requires='>=3',
)
