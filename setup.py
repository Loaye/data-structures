"""Setup file for http-server package."""


from setuptools import setup


setup(
    name="linked_list",
    description="Python linked list.",
    author=["Michael Shinners", "Jacob Carstens", "Brendan Davis"],
    author_email=["michaelshinners@gmail.com", "jr.carstens00@gmail.com",
                  "brendanmd@gmail.com"],
    license="MIT",
    py_modules=["client", "server"],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
    entry_points={
    }
)
