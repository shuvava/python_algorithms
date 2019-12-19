from setuptools import setup

setup(
    name='snake',
    entry_points={
        'console_scripts': [
            'snake = snake:main',
        ],
        'snake_types': [
            'normal = snake:normal_snake',
            'fancy = snake:fancy_snake',
            'cute = snake:cute_snake',
        ],
    }
)
