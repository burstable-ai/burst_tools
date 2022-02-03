from setuptools import setup, find_packages
setup(
    name="burst_tools",
    version="0.1.2",
    install_requires=[
        "pynvml"
    ],
    scripts=['bin/burst', 'bin/burst-config', 'bin/burst-monitor'],
    python_requires='>=3',
)
