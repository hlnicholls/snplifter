from setuptools import setup, find_packages

setup(
    name='snplifter',
    version='0.1.0',
    packages=find_packages(),
    description='SNP liftover tool for converting SNP coordinates between genome builds.',
    author='Hannah Nicholls',
    author_email='hannahnicholls@qmul.ac.uk',
    entry_points={
        'console_scripts': [
            'snplifter=snplifter.modules.cli_handles:run_liftover',
        ],
    },
    install_requires=[
        'pandas',
        'hail',
    ],
    python_requires='>=3.6',
)
