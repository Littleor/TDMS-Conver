import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TDMS-Conver",
    version="0.0.1",
    author="Littleor",
    license='MIT',
    author_email="me@littleor.cn",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'pandas>=1.1.5',
        'openpyxl>=3.0.7',
        'npTDMS>=1.3.0'
    ],
    url="https://github.com/Littleor/TDMS-Conver.git",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': [
            'tdms-conver=conver.main:main',
        ]
    }
)
