from setuptools import setup

with open('miio/version.py') as f: exec(f.read())

setup(
    name='python-miio',

    version=__version__,
    description='Python library for miio',
    url='https://github.com/SchumyHao/python-mirobo',

    author='SchumyHao',
    author_email='bob-hjl@126.com',

    license='GPLv3',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],

    keywords='xiaomi, miio',

    packages=["miio"],

    install_requires=['construct', 'click', 'cryptography'],
    entry_points={
        'console_scripts': [
            'miio=miio.cli:cli',
        ],
    },
)
