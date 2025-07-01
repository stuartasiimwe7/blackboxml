from setuptools import setup, find_packages

setup(
    name='tracingML',
    version='0.1.1',
    author='Stuart Asiimwe',
    author_email='stuartgabriel@ymail.com',
    description="Automatically logs Keras training metrics.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/stuartasiimwe7/traceml',
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