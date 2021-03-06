from setuptools import find_packages, setup

setup(
    name='py_cppstd',
    version='0.2.1',
    description=[
        'Using cpp std iostream lib in py'
    ],
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Cyan_Changes',
    author_email='1491326171@qq.com',
    maintainer='Cyan_Changes',
    maintainer_email='1491326171@qq.com',
    license='Apache 2.0',
    packages=find_packages(),
    platforms=['all'],
    url='https://github.com/Chinese-Cyq20100313/py_cppstd',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Printing"
    ]
)