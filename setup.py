from setuptools import setup, find_packages

setup(
    name='blackboxml',
    version='0.1.1',
    author='Stuart Asiimwe',
    author_email='stuartgabriel@ymail.com',
    description="Automatically logs Keras training metrics—now deprecated and renamed to traceml.",
    long_description=(
        "\u26a0\ufe0f DEPRECATION NOTICE: This package has been renamed to 'traceml'. "
        "Please install and use 'traceml' instead. "
        "This package will no longer be maintained under the old name.\n\n"
        + open('README.md').read()
    ),
    long_description_content_type='text/markdown',
    url='https://github.com/stuartasiimwe7/blackboxml',
    packages=find_packages(),
     install_requires=[
        'tensorflow>=2.0.0',
        'scikit-learn',
        'matplotlib',
        'numpy',
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
    
)