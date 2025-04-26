from setuptools import setup, find_packages

setup(
    name='blackboxml',
    version='0.1.0',
    author='Stuart Asiimwe',
    author_email='stuartgabriel@ymail.com',
    description='An Auto-metric logger library for Machine Learning workflows, even when you forget.',
    long_description=open('README.md').read(),
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