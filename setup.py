from setuptools import setup
setup(
    name='layx',
    packages=['layx', 'layx.playlist'],
    author='Roshan Lamichhane',
    author_email='lamichhaner40@gmail.com',
    description='Search and play any song from terminal.',
    long_description='Search and play any song from terminal seamlessly.',
    url='http://github.com/roshancode/layx',
    entry_points={
        'console_scripts': [
            'layx = layx.main:main'
        ]
    },
    version='1.0.0',
    install_requires=['youtube_dl', 'requests', 'beautifulsoup4', 'selenium', 'lxml'],
)
