from setuptools import setup, find_packages

setup(
    name='blackboxml',
    version='0.1.0',
    author='Stuart Asiimwe'
    description='An Auto-metric logger library for Machine Learning workflows, even when you forget.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
     install_requires=[
        'tensorflow>=2.0.0',
        'scikit-learn',
        'matplotlib',
        'numpy',
        'pandas',
    ],
    
)