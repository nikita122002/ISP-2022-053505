from setuptools import setup

setup(
    name='dump_library',
    packages=[
        'dump_library',
        'dump_library/parsers',
        'dump_library/parsers/json',
        'dump_library/parsers/toml',
        'dump_library/parsers/yaml',
    ],
    version='1.0.0',
    author='nikita122002',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.3'],
    test_suite='tests',
    scripts=['dump_library/dump_console.py']
)