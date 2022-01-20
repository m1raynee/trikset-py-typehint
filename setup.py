import setuptools

setuptools.setup(
    name="trikset-py-typehint",
    version="0.0.1",
    author="m1raynee",
    author_email="pechenko-7@ya.ru",
    description="A package that provides type signatures to all documented methods",
    url="https://github.com/m1raynee/trikset-py-typehint",
    project_urls={
        "Bug Tracker": "https://github.com/m1raynee/trikset-py-typehint/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: Russian",
        "Typing :: Typed",
    ],
    package_dir={"": "trik"},
    packages=setuptools.find_packages(where="trik"),
    python_requires=">=3.6",
)
